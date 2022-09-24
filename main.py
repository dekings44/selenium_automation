import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.get('https://www.amazon.co.uk/')
driver.implicitly_wait(30)

search = driver.find_element(By.ID, 'twotabsearchtextbox')
search.send_keys('laptops')

search.send_keys(Keys.RETURN)
# 
# my_element = driver.find_element(By.LINK_TEXT, 'How To Efficiently Load Data Into Postgres Using Python')
# my_element.click()