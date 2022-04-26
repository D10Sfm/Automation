import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from documents import *
from root import initroot, init_home_page

def test_link_contact_page_top():
    driver = initroot()
    driver.get("https://atid.store/contact-us/")
    logo_link = driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]")
    home_link = driver.find_element(By.ID,"menu-item-381")
    store = driver.find_element(By.ID,"menu-item-45")
    men = driver.find_element(By.ID,"menu-item-266")
    women = driver.find_element(By.ID,"menu-item-267")
    accessories = driver.find_element(By.ID,"menu-item-671")
    about = driver.find_element(By.ID,"menu-item-828")
    contact_us = driver.find_element(By.ID,"menu-item-829")
    search_link = driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[2]/div[1]/div[1]/a[1]")
    cart_link = driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]/div[3]/div[1]/div[1]/a[1]")
    navbar_link = [search_link,logo_link,home_link,store,men,women,accessories,about,contact_us,cart_link]


test_link_contact_page_top()