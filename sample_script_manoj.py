import requests
from bs4 import BeautifulSoup

url = "http://www.ebay.com/sch/"
file = 'keywords.txt'


def get_keywords(kw_file):
    # type: (object) -> object
    with open(kw_file) as file:
        keyword = [line.split('|')[0].rstrip('\r\n') for line in file]
        return keyword

#keyword = get_keywords(file)
#print keyword

def get_all_listings_urls(kw_url):
    for word in get_keywords(kw_file):
        listings_url = kw_url + word.rstrip('\r\n')
        page = requests.get(kw_url)
        response = page.status_code
        content = page.content
        print response  #--200 suucess response
        print content
        soup = BeautifulSoup(content, 'html.parser')
        hrefs = [d["href"] for d in soup.select(".lvtitle a")]
        return hrefs


def get_listing_info(category_url):
    for link in hrefs:
        # Check the response for URL connectivity and Reading the content of the URL
        sub_page = requests.get(link)
        sub_response = sub_page.status_code
        sub_content = sub_page.content
        #print sub_content
        sub_soup = BeautifulSoup(sub_content, 'html.parser')
        #print sub_soup

        title = sub_soup.find_all('span', id='vi-lkhdr-itmTitl')[0].get_text()
        return title

        price = sub_soup.find_all('span', id='prcIsum')[0].get_text()
        return price

        seller_name = sub_soup.find_all('span', class_='mbg-nw')[0].get_text()
        return seller_name

        seller_fdbck = sub_soup.find_all('div', id='si-fb')[0].get_text()
        return seller_fdbck

