import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from documents import *
from root import initroot, init_home_page


def test_search_products_no_exist(page):
    if page == 'store':
        driver = init_home_page()
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
        driver = init_home_page()
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
        driver = init_home_page()
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
    driver = init_home_page()
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
        assert value_product_desc == desc
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
        assert value_product_desc == desc
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
        assert value_product_desc == desc
        print(f"The description of product: \n{value_product_desc}")
        time.sleep(2)


def form_input_contact_us(field='', valid=True):
    if valid:
        if field == '':
            driver = initroot()
            driver.get('https://atid.store/contact-us/')
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, subject_field, email_field, text_field]
            for i in form:
                i.send_keys(test_details[form.index(i)])
            time.sleep(2)
            send_buttom.click()
        elif field == 'name':
            driver = initroot()
            driver.get('https://atid.store/contact-us/')
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [subject_field, email_field, text_field]
            for i in form:
                i.send_keys(test_details[form.index(i) + 1])
            time.sleep(2)
            send_buttom.click()
        elif field == 'subject':
            driver = initroot()
            driver.get('https://atid.store/contact-us/')
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, email_field, text_field]
            x = [i for i in test_details if i != "Ballon d'Or"]
            for i in form:
                i.send_keys(x[form.index(i)])
            time.sleep(2)
            send_buttom.click()
        elif field == 'email':
            driver = initroot()
            driver.get('https://atid.store/contact-us/')
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, subject_field, text_field]
            x = [i for i in test_details if i != "leom.1091@email.com"]
            for i in form:
                i.send_keys(x[form.index(i)])
            send_buttom.click()
        elif field == 'text':
            driver = initroot()
            driver.get('https://atid.store/contact-us/')
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, subject_field, email_field]
            x = [i for i in test_details if test_details.index(i) != -1]
            for i in form:
                i.send_keys(x[form.index(i)])
            time.sleep(2)
            send_buttom.click()
    elif not valid:
        if field == '':
            raise Exception("Must Enter an field for invalid test!")
        elif field == 'name':
            driver = initroot()
            driver.get('https://atid.store/contact-us/')
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [subject_field, email_field, text_field]
            name_field.send_keys(input("Enter your test keys: "))
            for i in form:
                i.send_keys(test_details[form.index(i) + 1])
            time.sleep(2)
            send_buttom.click()
        elif field == 'subject':
            driver = initroot()
            driver.get('https://atid.store/contact-us/')
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            form = [name_field, email_field, text_field]
            x = [i for i in test_details if i != "Ballon d'Or"]
            subject_field.send_keys(input("Enter your test keys: "))
            for i in form:
                i.send_keys(x[form.index(i)])
            time.sleep(2)
            send_buttom.click()
        elif field == 'email':
            driver = initroot()
            driver.get('https://atid.store/contact-us/')
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, subject_field, text_field]
            x = [i for i in test_details if i != "leom.1091@email.com"]
            email_field.send_keys("")
            for i in form:
                i.send_keys(x[form.index(i)])
            WebDriverWait(driver, 8).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, "#wpforms-15-field_4-error"),
                    email_err_msg[1]
                )
            )
            send_buttom.click()
        elif field == 'text':
            driver = initroot()
            driver.get('https://atid.store/contact-us/')
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            form = [name_field, subject_field, email_field]
            x = [i for i in test_details if test_details.index(i) != -1]
            text_field.send_keys(input("Enter your test keys: "))
            for i in form:
                i.send_keys(x[form.index(i)])
            time.sleep(2)
            send_buttom.click()
