# Importing necessary modules
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import codecs

# WebDriver Chrome
driver = webdriver.Chrome()
val = input('Enter a url: ')

#wait = WebDriverWait(driver, 10)

driver.get(val)


#get_url = driver.current_url
#wait.until(EC.url_to_be(val))


#if get_url == val:
page_source = driver.page_source
    
soup = BeautifulSoup(page_source,features='html.parser')
title = soup.title.text

# Target URL
#driver.get("https://www.geeksforgeeks.org/competitive-programming-a-complete-guide/")
# To load entire webpage
time.sleep(5)

# Printing the whole body text
page_data = driver.find_element(By.XPATH, "/html/body").text
file=codecs.open('link1.txt', 'a+')
file.write(title+'\n')
file.write(str(page_data)+'\n')
file.close()
# Closing the driver
driver.close()
