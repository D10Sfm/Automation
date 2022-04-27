import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import Tests.Utitlitis.GlobalFunctionETC.documents as DO
import Tests.Utitlitis.ContactUs.root as R
import Tests.Utitlitis.ContactUs.linkTest as Lnk
import Tests.Utitlitis.ContactUs.uiTesting as Ui
import Tests.Utitlitis.GlobalFunctionETC.driverInit as DR
import Tests.Utitlitis.ContactUs.functionalityTesting as Co
import Tests.Utitlitis.Men.functionalityTesting as Me
import Tests.Utitlitis.Women.functionalityTesting as Wo
import Tests.Utitlitis.Accessories.functionalityTesting as Ac
import Tests.Utitlitis.AboutUs.uiTesting as AbUi


def test_search_products_no_exist(page):
    if page == 'store':
        driver = R.init_home_page()
        store = driver.find_element(by=By.XPATH,
                                    value="//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                          "1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")
        store.click()
        time.sleep(3)
        search_input = driver.find_element(by=By.ID, value="wc-block-search__input-1")
        search_input.send_keys("Leo Messi!")
        time.sleep(2)
        search_button = driver.find_element(by=By.CLASS_NAME, value="wc-block-product-search__button")
        search_button.click()
        value = driver.find_element(By.XPATH,
                                    "//body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/p[1]").get_attribute(
            'innerHTML')
        assert value == 'No products were found matching your selection.'
        print(f"The text to be present: \n{value}")
    elif page == 'men':
        driver = R.init_home_page()
        men = driver.find_element(by=By.XPATH,
                                  value="//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                        "1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]")
        men.click()
        time.sleep(3)
        search_input = driver.find_element(by=By.ID, value="wc-block-search__input-1")
        search_input.send_keys("Leo Messi!")
        time.sleep(2)
        search_button = driver.find_element(by=By.CLASS_NAME, value="wc-block-product-search__button")
        search_button.click()
        value = driver.find_element(By.XPATH,
                                    "//body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/p[1]").get_attribute(
            'innerHTML')
        assert value == 'No products were found matching your selection.'
        print(f"The text to be present: \n{value}")
    elif page == 'women':
        driver = R.init_home_page()
        women = driver.find_element(by=By.XPATH,
                                    value="//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div["
                                          "2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]")
        women.click()
        time.sleep(3)
        search_input = driver.find_element(by=By.ID, value="wc-block-search__input-1")
        search_input.send_keys("Leo Messi!")
        time.sleep(2)
        search_button = driver.find_element(by=By.CLASS_NAME, value="wc-block-product-search__button")
        search_button.click()
        time.sleep(3)
        value = driver.find_element(By.XPATH,
                                    "//body[1]/div[1]/div[1]/div[1]/div[2]/main[1]/div[1]/p[1]").get_attribute(
            'innerHTML')
        assert value == 'No products were found matching your selection.'
        print(f"The text to be present: \n{value}")


def test_search_exist_product_has_quantity1(page):
    driver = R.init_home_page()
    if page == 'men':
        men = driver.find_element(by=By.XPATH,
                                  value="//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                        "1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]")
        men.click()
        time.sleep(3)
        search_input = driver.find_element(by=By.ID, value="wc-block-search__input-1")
        search_input.send_keys('Anchor Bracelet')
        search_button = driver.find_element(by=By.CLASS_NAME, value="wc-block-product-search__button")
        search_button.click()
        value_product_title = driver.find_element(By.XPATH, "//h1[contains(text(),'Anchor Bracelet')]").get_attribute(
            "innerText")
        assert value_product_title == 'Anchor Bracelet'
        print(f"The title of product: \n{value_product_title}")
        value_product_price = driver.find_element(By.XPATH,
                                                  "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div["
                                                  "2]/div[2]/p[1]/span[1]/bdi[1]").get_attribute(
            'innerText')
        assert value_product_price == '250.00 ₪'
        print(f"The price of product: \n{value_product_price}")
        value_product_desc = driver.find_element(By.XPATH,
                                                 "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main["
                                                 "1]/div[1]/div[2]/div[2]/div[2]").get_attribute(
            'innerText')
        assert value_product_desc == DO.desc
        print(f"The description of product: \n{value_product_desc}")
        time.sleep(2)
    elif page == 'store':
        store = driver.find_element(by=By.XPATH,
                                    value="//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div["
                                          "1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[2]/a[1]")
        store.click()
        time.sleep(3)
        search_input = driver.find_element(by=By.ID, value="wc-block-search__input-1")
        search_input.send_keys('Anchor Bracelet')
        search_button = driver.find_element(by=By.CLASS_NAME, value="wc-block-product-search__button")
        search_button.click()
        value_product_title = driver.find_element(By.XPATH, "//h1[contains(text(),'Anchor Bracelet')]").get_attribute(
            "innerText")
        assert value_product_title == 'Anchor Bracelet'
        print(f"The title of product: \n{value_product_title}")
        value_product_price = driver.find_element(By.XPATH,
                                                  "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div["
                                                  "2]/div[2]/p[1]/span[1]/bdi[1]").get_attribute(
            'innerText')
        assert value_product_price == '250.00 ₪'
        print(f"The price of product: \n{value_product_price}")
        value_product_desc = driver.find_element(By.XPATH,
                                                 "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main["
                                                 "1]/div[1]/div[2]/div[2]/div[2]").get_attribute(
            'innerText')
        assert value_product_desc == DO.desc
        print(f"The description of product: \n{value_product_desc}")
        time.sleep(2)
    elif page == 'women':
        women = driver.find_element(by=By.XPATH,
                                    value="//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div["
                                          "2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[4]/a[1]")
        women.click()
        time.sleep(3)
        search_input = driver.find_element(by=By.ID, value="wc-block-search__input-1")
        search_input.send_keys('Anchor Bracelet')
        search_button = driver.find_element(by=By.CLASS_NAME, value="wc-block-product-search__button")
        search_button.click()
        value_product_title = driver.find_element(By.XPATH, "//h1[contains(text(),'Anchor Bracelet')]").get_attribute(
            "innerText")
        assert value_product_title == 'Anchor Bracelet'
        print(f"The title of product: \n{value_product_title}")
        value_product_price = driver.find_element(By.XPATH,
                                                  "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div["
                                                  "2]/div[2]/p[1]/span[1]/bdi[1]").get_attribute(
            'innerText')
        assert value_product_price == '250.00 ₪'
        print(f"The price of product: \n{value_product_price}")
        value_product_desc = driver.find_element(By.XPATH,
                                                 "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main["
                                                 "1]/div[1]/div[2]/div[2]/div[2]").get_attribute(
            'innerText')
        assert value_product_desc == DO.desc
        print(f"The description of product: \n{value_product_desc}")
        time.sleep(2)


def test_addToCart():
    Me.test_addToCartMen()
    Wo.test_addToCartWomen()
    Ac.test_addToCartAccessories()


def test_func():
    Co.test_func_contact_page()


def test_link():
    Lnk.test_links_contact_page()


def test_ui():
    Ui.test_ui_contact_page()


def sanity():
    x = input("Enter page: ")
    test_search_products_no_exist(x)
    y = input("Enter page: ")
    test_search_exist_product_has_quantity1(y)


def end_2_end():
    test_ui()
    test_link()
    test_func()
    test_addToCart()

def test():
    AbUi.test_ui_top_page()