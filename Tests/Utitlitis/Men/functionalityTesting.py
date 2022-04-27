import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import Tests.Utitlitis.GlobalFunctionETC.documents as DO
import Tests.Utitlitis.ContactUs.root as R
import Tests.Utitlitis.GlobalFunctionETC.driverInit as DR




def test_addToCartMen():
    driver = DR.initroot()
    driver.get(DO.men_url)
    prod_ul = driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]")
    products = prod_ul.find_elements(By.TAG_NAME,"li")
    products[0].click()
    time.sleep(2)
    cart_btn = driver.find_element(By.XPATH,"//button[contains(text(),'Add to cart')]")
    cart_btn.click()
    driver.back()
    driver.back()
    time.sleep(3)
    prod_ul = driver.find_element(By.XPATH,"//main[1]/div[1]/ul[1]")
    products = prod_ul.find_elements(By.TAG_NAME,"li")
    products[2].click()
    cart_btn = driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
    cart_btn.click()
    time.sleep(3)
    cart_view = driver.find_element(By.XPATH,"//main[1]/div[1]/div[1]/div[1]/a[1]")
    cart_view.click()
    products_nams = [driver.find_element(By.XPATH,"//tbody/tr[1]/td[3]"),driver.find_element(By.XPATH,"//tbody/tr[2]/td[3]")]
    products_prices = [driver.find_element(By.XPATH, "//tbody/tr[1]/td[4]/span[1]").text,
                       driver.find_element(By.XPATH, "//tbody/tr[2]/td[4]/span[1]").text]
    for i,j in zip(products_nams,DO.prod_names_test_men):
        assert i.text == j
    for i,j in zip(products_prices,DO.prod_price_test_men):
        assert i == j