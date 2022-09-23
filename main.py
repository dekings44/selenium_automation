import os
from selenium import webdriver
from selenium.webdriver.common.by import By


#os.environ['PATH'] += r"C:/Users/kings/SeleniumDrivers"
driver = webdriver.Chrome()
driver.get('https://blog.dekings.dev/')
driver.implicitly_wait(5)
my_element = driver.find_element(By.LINK_TEXT, 'How To Efficiently Load Data Into Postgres Using Python')
my_element.click()