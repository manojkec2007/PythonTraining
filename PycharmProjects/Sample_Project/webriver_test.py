"""
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

url = "http://www.ebay.com/sch/" + "Actnovate"
print url

driver = webdriver.Firefox()
driver_out = driver.get(url)

print driver_out
html = driver.page_source
soup = BeautifulSoup(html)

print html
print soup
"""

#from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
driver.get("http://m.imdb.com/feature/bornondate")

list = driver.find_element_by_xpath("//section[@class='posters list'] / a[@class='poster']/ ")

#print str(len(list)) + " Items Found"

for i in list:
    print i.text


a.quit()
