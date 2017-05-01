"""
Python module for searching given items in ebay site
and print the Listings URLs, Seller Information, Item Price

"""
__author__ = "Manoj K V"

# -*- coding: utf-8 -*-
import requests
import pandas as pd

from bs4 import BeautifulSoup

# Reading the keywords file  -first column
with open('keywords.txt') as file:
    keyword = [line.split('|')[0] for line in file]
#print keyword



for word in keyword:
    #url = "http://www.ebay.com/sch/" + word.rstrip('\r\n')
    url = "http://www.ebay.com/sch/" + "Actnovate"
    # Check the response for URL connectivity and Reading the content of the URL
    page = requests.get(url)
    response = page.status_code
    content = page.content
    #print response  #--200 suucess response
    #print content
    soup = BeautifulSoup(content, 'html.parser')
    #print soup

    #print soup
    #soup1= soup.find_all('a', class_='vip')[0].get_text()
    #soup2= soup.find_all('a', class_='vip')


    hrefs = [d["href"] for d in soup.select(".lvtitle a")]
    #print hrefs

    for link in hrefs:
        # Check the response for URL connectivity and Reading the content of the URL
        sub_page = requests.get(link)
        sub_response = sub_page.status_code
        sub_content = sub_page.content
        #print sub_content
        sub_soup = BeautifulSoup(sub_content, 'html.parser')
        #print sub_soup

        title = sub_soup.find_all('span', id='vi-lkhdr-itmTitl')[0].get_text()
        print title

        price = sub_soup.find_all('span', id='prcIsum')[0].get_text()
        print price

        seller_name = sub_soup.find_all('span', class_='mbg-nw')[0].get_text()
        print seller_name

        seller_fdbck = sub_soup.find_all('div', id='si-fb')[0].get_text()
        print seller_fdbck



        # print hrefs

        #exit(0)
    # soup1 = soup.find_all('h3', class_='lvtitle')
    #
    # #print soup1
    # href = soup1[0]
    #
    # print href
    #
    # url_link = href.find("a")
    # link = url_link['href']
    #
    # print link

    #href = list(soup1)[2]

    #print href
    #print soup1
    #print soup2

    #soup3 = soup.find_all('h3', class_='lvtitle')
    #print soup3

    #link = soup3.find("a")
    #href = link['href']

    #print href

    #print (soup.prettify())
    #print list(soup.children)
    #print soup1
    #print [type(item) for item in list(soup1)]
    exit(0)




