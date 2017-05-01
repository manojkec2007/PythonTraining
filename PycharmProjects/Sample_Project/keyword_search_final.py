"""
Python module for searching given items in ebay site
and print the Listings URLs, Seller Information, Item Price

"""
__author__ = "Manoj K V"

# -*- coding: utf-8 -*-
import requests

from bs4 import BeautifulSoup

# Reading the keywords file  -first column
with open('keywords.txt') as file:
    keyword = [line.split('|')[0] for line in file]
    #print keyword


for word in keyword:
    url = "http://www.ebay.com/sch/" + word.rstrip('\r\n')
    #url = "http://www.ebay.com/sch/" + "Actnovate"
    # Check the response for URL connectivity and Reading the content of the URL

    #print url
    page = requests.get(url)
    response = page.status_code
    content = page.content
    #print response  #--200 success response
    # print content

    if response == 200:
        soup = BeautifulSoup(content, 'html.parser')
        hrefs = [d["href"] for d in soup.select(".lvtitle a")]
        #print hrefs

        if len(hrefs)== 0:
            print "No results Found for '%s'" %word.rstrip('\r\n')
        for sub_link in hrefs:
            # Check the response for URL connectivity and Reading the content of the URL
            print sub_link
            sub_page = requests.get(sub_link)
            sub_response = sub_page.status_code
            sub_content = sub_page.content
            # print sub_response  #--200 success response
            # print sub_content

            sub_soup = BeautifulSoup(sub_content, 'html.parser')
            #print sub_soup

            #Listing Title
            try:
                title = sub_soup.find_all('span', id='vi-lkhdr-itmTitl')[0].get_text()
                print title
            except IndexError:
                print ""

            # Item Price
            try:
                price = sub_soup.find_all('span', id='prcIsum')[0].get_text()
                print price
            except IndexError:
                print ""

            # Seller Name
            try:
                seller_name = sub_soup.find_all('span', class_='mbg-nw')[0].get_text()
                print seller_name
            except IndexError:
                print ""

            # Seller Feedback
            try:
                seller_fdbck = sub_soup.find_all('div', id='si-fb')[0].get_text()
                print seller_fdbck
            except IndexError:
                print ""
