# -*- coding: utf-8 -*-

import requests
import re
from bs4 import BeautifulSoup
import urllib2 as urllib
import pdfquery
import lxml
import time
import string
import os
from cStringIO import StringIO
import pyodbc
from microsofttranslator import Translator
translator = Translator('665*******************', 'oWifM+43B6AV*********************')


site = 'http://www.mhlw.go.jp'
url = 'http://www.mhlw.go.jp/seisakunitsuite/bunya/kenkou_iryou/iyakuhin/yakubuturanyou/shiteiyakubutsu.html'
base_url = 'http://www.mhlw.go.jp/seisakunitsuite/bunya/kenkou_iryou/iyakuhin/yakubuturanyou/'
#dl/shiteiyakubutsu160309_02.pdf

final_opfile = open('med_names.txt','w+')

TARGET_CHARS = string.ascii_letters + string.digits + string.punctuation + string.whitespace

def get_element_text(elem, delim=' ', default=''):
    text = []
    def add_text(tag, no_tail=False):
        if tag.text and not isinstance(tag, lxml.etree._Comment):
            text.append(tag.text)
        for child in tag.getchildren():
            add_text(child)
        if not no_tail and tag.tail:
            text.append(tag.tail)

    add_text(elem, no_tail=True)
    return delim.join([t.strip() for t in text if t.strip()])	

def main(): 
	pdf_urls = set()
	# Track the pdf file link: 
	page1 = requests.get(url)
	content1 = BeautifulSoup(page1.content,"html.parser") 
	
	for all_data in content1.find_all("a"): 
		all_link = all_data.get("href")
		#print 'Link: ',all_link
		if len(all_link) > 12 and '.pdf' in all_link: 
			#print base_url +str(all_link)
			pdf_urls.add(base_url +str(all_link)) 
		else:
			continue

	for pdf_url_link in pdf_urls:
		print 'The URL is: ', pdf_url_link
		
		pdf_url_req = urllib.urlopen(pdf_url_link)
		page_available = pdf_url_req.getcode()
		if page_available != 200: 
			print pdf_url_link, 'not available, skipping.'
			continue
		resp_bytes = pdf_url_req.read()
		resp_stringio = StringIO(resp_bytes)
		pdf = pdfquery.PDFQuery(resp_stringio)
		
		# print 'Type: ', type(pdf_url), ' :and: ', pdf_url
		
		pdf.load()
		label = pdf.pq('LTTextLineHorizontal')
		left_corner = float(label.attr('x0'))
		bottom_corner = float(label.attr('y0'))

		elem_list = pdf.pq('LTTextLineHorizontal')
		for i, elem in enumerate(elem_list):
			a = get_element_text(elem)
			#print i, a
			if i < 5 or len(a) < 3 or a.isdigit(): 
				#print 'Filter this: ', i, get_element_text(elem)
				continue
			else: 
				#mod_name = romkan.to_roma(a)
				# import pdb; pdb.set_trace()
				#print 'The Medical Name is: ', a
				if all([char in TARGET_CHARS for char in a]):
					mod_name = a
				else:
					mod_name = translator.translate(a, from_lang='ja', to_lang='en')

				b = a.encode('utf8')
				print 'Final Record: ', i, ' :val: ', b, ' :mod: ', mod_name.encode('utf8')
				final_opfile.write('|'.join([load_dt, pdf_url_link, b, mod_name.encode('utf8')]))
				final_opfile.write('\n')
		#text = elem.text()
		
		#print text
		#import pdb;pdb.set_trace()
		print 'Next file'
	final_opfile.close()

def load_data():
	print 'In Fastload Process: '
	try:
		os.system(r'fastload -c UTF8 < D:\Jegan_Work\Projects_with_python\scrape_pdf\J000_step2_scrape_pdf_fastload.txt > D:\Jegan_Work\Projects_with_python\scrape_pdf\med_names.txt.log')
	except Exception as e:
		print 'Exception 1: ', e

def load_td_table():
	print 'Loading the TD Base table'
	sql1 = """DELETE FROM pp_oap_brm_t.J000_SCRAPE_PDF_MHLW_GO_ALL WHERE LOAD_DT = '"""+load_dt+"""';"""
	sql2 = """INSERT INTO pp_oap_brm_t.J000_SCRAPE_PDF_MHLW_GO_ALL
              SELECT CAST(src.LOAD_DT AS DATE FORMAT 'YYYY-MM-DD') AS LOAD_DT 
                    ,TRIM(src.URL) AS URL 
					,TRIM(src.MED_NAME) AS MED_NAME
					,TRIM(src.MOD_MED_NAME) AS MOD_MED_NAME
                FROM pp_oap_brm_t.J000_SCRAPE_PDF_MHLW_GO_01 src
            GROUP BY 1,2,3,4;"""

	conx1 = pyodbc.connect('DRIVER={Teradata};DBCNAME=simba.vip.paypal.com;UID=PP_COMPLIANCE_BRM_USER;PWD=3peZ_pet+U;QUITEMODE=YES;')
	conntd = conx1.cursor()
	conntd.execute(sql1)
	conntd.execute(sql2)

	conntd.commit()
	conntd.close()

if __name__ == '__main__':
	load_dt = time.strftime('%Y-%m-%d')
	main()
	print 'In Fastload Process: '
	load_data()
	load_td_table()
