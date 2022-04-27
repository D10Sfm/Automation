import time
from selenium.webdriver.common.by import By
import Tests.Utitlitis.ContactUs.root as R
from selenium.webdriver.support.ui import Select
import Tests.Utitlitis.GlobalFunctionETC.documents as DO

def test_link_contact_page_top():
    driver = R.initroot()
    driver.get(DO.contact_us_url)
    logo_link = driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/span[1]/a[1]")
    nav_container = driver.find_element(By.ID,"ast-hf-menu-1")
    nav_links = nav_container.find_elements(By.TAG_NAME,"a")
    cart_search_link = driver.find_element(By.XPATH,"//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[3]")
    cart_links = cart_search_link.find_elements(By.TAG_NAME,"a")
    logo_link.is_enabled()
    for i in nav_links:
        i.is_enabled()
    for i in cart_links:
        i.is_enabled()


def test_link_contact_page_footer():
    driver = R.initroot()
    driver.get(DO.contact_us_url)
    driver.implicitly_wait(65)
    quick_links_cont = driver.find_element(By.ID,"menu-quick-links")
    quick_links = quick_links_cont.find_elements(By.TAG_NAME,"a")
    for_her_ul = driver.find_element(By.ID,"menu-for-her")
    for_her_links = for_her_ul.find_elements(By.TAG_NAME,"a")
    for_him_ul = driver.find_element(By.ID,"menu-for-him")
    for_him_links = for_him_ul.find_elements(By.TAG_NAME,"a")
    for i in quick_links:
        i.is_enabled()
    for i in for_her_links:
        i.is_enabled()
    for i in for_him_links:
        i.is_enabled()


def select():
    driver = R.initroot()
    driver.get(DO.contact_us_url)
    select = Select(driver.find_element(By.XPATH,"//main[1]/div[1]/form[1]/select[1]"))
    # options = select.find_elements(By.TAG_NAME,"option")
    select.select_by_index(2)
    time.sleep(2)
    prod = driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]")
    items = prod.find_elements(By.TAG_NAME,"li")
    items[4].click()
    time.sleep(4)


def test_links_contact_page():
    test_link_contact_page_top()
    test_link_contact_page_footer()












    # for i in quick_links:
    #     if i == contact_us:
    #         i.click()
    #     else:
    #         i.click()
    #         driver.back()
    #         time.sleep(2)
    #
    # for i in for_her_links:
    #     i.click()
    #     time.sleep(2)
    #     driver.back()
    # for i in for_him_links:
    #     i.click()
    #     time.sleep(2)
    #     driver.back()
