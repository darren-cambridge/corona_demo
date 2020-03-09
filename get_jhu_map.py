#Doen't work because everything rendered with JS in browser
#import requests
#from bs4 import BeautifulSoup

#page = requests.get("https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
#print(page.status_code)
#print(page.content)

#soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#map_div = soup.find_all(id="esri.Map_1_gc")
#map_div = soup.select("div#esri.Map_1_layers")
#print(map_div)

from selenium import webdriver
driver = webdriver.PhantomJS()
driver.set_window_size(1120, 550)
driver.get("https://duckduckgo.com/")
driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
driver.find_element_by_id("search_button_homepage").click()
print(driver.current_url)
driver.quit()