"""Basic automation i did in asos"""
''' the import section'''
# the command line that import the webdriver directory from selenium
from selenium import webdriver
# the command line that import the by method from common directory
from selenium.webdriver.common.by import By
# the command line that import the implicitly wait function from ui directory
from selenium.webdriver.support.ui import WebDriverWait
# the command line that import the expected condition function from support directory
from selenium.webdriver.support import expected_conditions as EC
# the command line that import the keys function from keys directory
from selenium.webdriver.common.keys import Keys
# creat an variable for the chrome driver that install in the computer
driver = webdriver.Chrome(executable_path="C:\Program Files\SeleniumDrivers\Chrom\chromedriver.exe")
# use the get method to load the base url in the chrom driver(browser)
driver.get("https://www.asos.com/men/")
# use the implicitly wait method to ensure waiting for loading element or if don't need to wait it do the action immediatly
driver.implicitly_wait(8)
# define variable for the search bar
main_search = driver.find_element(by=By.CLASS_NAME,value="Cyuazsm")
# use the send_keys method to type in the element
main_search.send_keys("barcelona")
# define variable for the search button
search_button = driver.find_element(by=By.CLASS_NAME,value="kH5PAAC")
# use the click method to type in the element
search_button.click()
# define variable for the wish item
my_element = driver.find_element(by=By.CLASS_NAME,value="_2r9Zh0W")
# use the click method to type in the element
my_element.click()
# define variable for the like button
like_button = driver.find_element(by=By.CLASS_NAME,value="i5hAj")
# use the click method to type in the element
like_button.click()
