import requests
from bs4 import BeautifulSoup
import urllib2

base_url = "http://www.ebay.com/sch/"
file_name = "keywords.txt"


def get_keywords(kw_file):
    """
    # type: (object) -> object
    # type: (object) -> object
    """
    with open(kw_file) as file:
        keyword = [line.split('|')[0].rstrip('\r\n') for line in file]
        return keyword


def get_all_listings_urls(kw_file, kw_url):
    """
    # type: (object, object) -> object
    """
    return_href = []
    for word in get_keywords(kw_file):
        listings_url = (kw_url + word)
        # print listings_url
        page = requests.get(listings_url)
        # print page
        response = page.status_code
        # print response  #--200 success response
        if response == 200:
            content = page.content
            # print content
            soup = BeautifulSoup(content, 'html.parser')
            # print soup
            href = [d["href"] for d in soup.select(".lvtitle a")]
            return_href.append(href)
            # print href
        else:
            print word, "Error: Page not found"
    return return_href



keyword = get_keywords(file_name)
print "keyword", keyword
hrefs = get_all_listings_urls(file_name, base_url)
print hrefs

"""
if len(hrefs) == 0:
    print '%s : No results Found' % word
else:
    print '%s : %s' % (word, hrefs)
else:
print "Page not found"
"""