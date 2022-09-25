import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)

driver.maximize_window()

driver.get('https://www.konga.com/')
driver.implicitly_wait(30)

option1 = Options()
option1.add_argument("--disable-notifications")

# search = driver.find_element(By.ID, 'jsSearchInput')
# search.send_keys('laptops')

# search.send_keys(Keys.RETURN)
# 
# my_element = driver.find_element(By.LINK_TEXT, 'How To Efficiently Load Data Into Postgres Using Python')
# my_element.click()