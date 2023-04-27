from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import csv

driver = webdriver.Chrome(executable_path=
                          '/usr/lib/chromium-browser/chromedriver')

driver.get('https://www.geeksforgeeks.org/selenium-python-tutorial/')
driver.implicitly_wait(10)
driver.maximize_window()
r = 1
templist = []

while (1):
    try:
        method = driver.find_element_by_xpath('//*[@id="post-427949"]\
		/div[3]/table[2]/tbody/tr[' + str(r) + ']/td[1]').text
        Desc = driver.find_element_by_xpath('//*[@id="post-427949"]/\
		div[3]/table[2]/tbody/tr[' + str(r) + ']/td[2]').text

        Table_dict = {'Method': method,
                      'Description': Desc}

        templist.append(Table_dict)
        df = pd.DataFrame(templist)

        r += 1

    # if there are no more table data to scrape
    except NoSuchElementException:
        break

# saving the dataframe to a csv
df.to_csv('table.csv')
driver.close()