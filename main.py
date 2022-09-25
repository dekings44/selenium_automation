import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options



chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument('--headless')
chrome_options.add_argument('--hide-scrollbars')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("--log-level=3")  # fatal




#page = 0

PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH, options=chrome_options)

driver.maximize_window()


# url = "https://www.konga.com/category/electronics-5261"
# browser.get(url)

# while page < 51:

#     page = page + 1


#     next_page = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.LINK_TEXT, str(page))))
#     next_page.click()


#     print("page " + str(page))

#     element = WebDriverWait(browser, 15).until(
#         EC.presence_of_element_located((By.CLASS_NAME, "af885_1iPzH")))
#     print(element.text)
driver.get('https://www.konga.com/')
element = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "search")))




# search = driver.find_element(By.NAME, 'search')
element.send_keys('laptops')

element.send_keys(Keys.RETURN)
# 
# my_element = driver.find_element(By.LINK_TEXT, 'How To Efficiently Load Data Into Postgres Using Python')
# my_element.click()