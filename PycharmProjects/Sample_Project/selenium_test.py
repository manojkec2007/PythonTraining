from selenium import webdriver

a = webdriver.Chrome("C:\Program Files (x86)\chromedriver_win32\chromedriver.exe")
a.get("http://www.ebay.com/")
a.maximize_window()

a.find_element_by_xpath("//input[@id='gh-ac']").send_keys("Actnovate")
a.find_element_by_xpath("//input[@type='submit']").click()
list = a.find_element_by_xpath("//li[@class='lvprice prc']/ span")

#str(len(href)) + " Items Found"


for i in list:
    print i.text


a.quit()
