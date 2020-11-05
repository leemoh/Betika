import selenium
from bs4 import BeautifulSoup
import csv

import time
import pandas
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options =webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/home/mclnerney/Betika')

driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=options)
driver.get('https://www.betika.com/mobile/#/virtuals/results?season=1947814&matchday=')

#columns=len(driver.find_elements_by_xpath("/html/body/div[2]/main/div/div[2]/table[2]/tbody/"))
rows=len(driver.find_elements_by_xpath("/html/body/div[2]/main/div/div[2]/table[2]/tbody/tr"))



dy=len(driver.find_elements_by_xpath("/html/body/div[2]/main/div/div[2]/table[2]/tbody/tr"))
res=len(driver.find_elements_by_xpath("/html/body/div[2]/main/div/div[2]/table[2]/tbody/tr[6]/td"))
#print(dy)
#print(res)
for c in range(1,dy+1):
    value=driver.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/table[2]/tbody/tr["+str(c)+"]").text
    outf=open('w.csv','w')
    writer=csv.writer(outf)
    for v in value:
        writer.writerow(v)
outf.close()
    #print(value)

        