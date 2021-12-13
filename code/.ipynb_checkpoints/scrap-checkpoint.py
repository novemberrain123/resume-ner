#!/usr/bin/env python
# coding: utf-8

# In[91]:


import os
import selenium
from selenium import webdriver
import time
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

import argparse

parser = argparse.ArgumentParser(description='Query')
parser.add_argument('email', type=str)
parser.add_argument('pw', type=str)
parser.add_argument('query', type=str)

args = parser.parse_args()
print(args.email)
print(args.pw)
print(args.query)
# In[92]:


#Install Driver
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()


# In[93]:


#Specify Search URL 
search_url="https://www.linkedin.com/login"

driver.get(search_url)
time.sleep(1)


# In[94]:


username = driver.find_element_by_id('username')
password = driver.find_element_by_id('password')


# In[95]:

#PUT IN OWN LOGIN INFO
username.send_keys(args.email)
password.send_keys(args.pw)


# In[96]:


username.submit()


# In[97]:


search_url="https://www.linkedin.com/search/results/people/?keywords={q}&origin=CLUSTER_EXPANSION&sid=~1J"

#CHANGE q TO DIFFERENT VALUE, IT IS THE SEARCH TERM
driver.get(search_url.format(q=args.query))
time.sleep(1)


# In[98]:

#WHEN IT STARTS, POP UP WILL OCCUR FOR MULTIPLE FILE DOWNLOAD, CLICK ALLOW
for i in range(10):
    profile = driver.find_elements_by_css_selector(".app-aware-link[aria-hidden='false']")[i]
    driver.execute_script("arguments[0].click();", profile)
    time.sleep(2)
    element = driver.find_element_by_css_selector("[aria-label='More actions']")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(2)
    element = driver.find_element_by_css_selector("[data-control-name='save_to_pdf']")
    driver.execute_script("arguments[0].click();", element)
    time.sleep(1)
    driver.back()
    driver.back()
    time.sleep(1)





