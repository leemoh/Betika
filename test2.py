
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
driver.get('https://www.betika.com/mobile/#/virtuals/results?')
url='https://www.betika.com/mobile/#/virtuals/results?season=%s&matchday='
sn=len(driver.find_elements_by_xpath("/html/body/div[2]/main/div/div[2]/table[1]/tr[2]/td[1]/select/option"))
seasons=set()
for sn in range(1,sn+1):
    valu= driver.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/table[1]/tr[2]/td[1]/select/option["+str(sn)+"]").text
    value=valu[13:]
    seasons.add(value)
list_url=[]
for ur in seasons:
    
        url_test=(url%ur)
        list_url.append(str(url_test))
        #print(url_test)
f=open('urls.csv','w',newline='')
y=[]
for x in (range(1,30)):
    for k in list_url:
        y.append(k+str(x))
for l in y:
        

    writer=csv.writer(f)
    writer.writerow([l])
#f.writelines(list_url)
    
f.close()       
#print(list_url[1])

     