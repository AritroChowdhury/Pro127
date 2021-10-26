from selenium import webdriver
from bs4 import BeautifulSoup
import time 
import csv

START_URL="https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
browser=webdriver.Chrome("/path/to/chromedriver")
browser.get(START_URL)
time.sleep(10)

soup=BeautifulSoup(browser.page_source,"html.parser")
for ul_tag in soup.find_all("ul",attrs=("class","Sun")):
    li_tags=ul_tag.find_all("li")

temp_list=[]
for index,li_tags in enumerate(li_tags):
    if index==0:
        temp_list.append(li_tag.find_all("a")[0].contents[0])
    else:
        try:
            temp_list.append(li_tag.contents[0])
        except:
            temp_list.append("")

sun_data.append(temp_list)

browser.find_element_by_xpath("https://en.wikipedia.org/wiki/Sun").click()

with open("scrapper2.csv","w")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(sun_data)