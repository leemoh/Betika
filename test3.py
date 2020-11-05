import selenium
from bs4 import BeautifulSoup
import csv
from csv import reader

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
l=[]
f=open("urls.csv",'r')
csvr=csv.reader(f)
for r in csvr:
    for k in range(30):
        time.sleep(5)
        driver.get(r[k])
        time.sleep(5)
        dy=len(driver.find_elements_by_xpath("/html/body/div[2]/main/div/div[2]/table[2]/tbody/tr"))
        for c in range(1,dy+1):
            value=driver.find_element_by_xpath("/html/body/div[2]/main/div/div[2]/table[2]/tbody/tr["+str(c)+"]").text
            for v in value:
                outf=open('w2.csv','w')
                writer=csv.writer(outf)
                writer.writerow([v])
                driver.close()
                
outf.close()
             

            
        
