import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import Tests.Utitlitis.GlobalFunctionETC.documents as DO
import Tests.Utitlitis.ContactUs.root as R
import Tests.Utitlitis.GlobalFunctionETC.driverInit as DR


def form_input_contact_us(field='', valid=True):
    if valid:
        if field == '':
            driver = R.initroot()
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, subject_field, email_field, text_field]
            for i in form:
                i.send_keys(DO.test_details[form.index(i)])
            time.sleep(2)
            send_buttom.click()
        elif field == 'name':
            driver = R.initroot()
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [subject_field, email_field, text_field]
            for i in form:
                i.send_keys(DO.test_details[form.index(i) + 1])
            time.sleep(2)
            send_buttom.click()
        elif field == 'subject':
            driver = R.initroot()
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, email_field, text_field]
            x = [i for i in DO.test_details if i != "Ballon d'Or"]
            for i in form:
                i.send_keys(x[form.index(i)])
            time.sleep(2)
            send_buttom.click()
        elif field == 'email':
            driver = R.initroot()
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, subject_field, text_field]
            x = [i for i in DO.test_details if i != "leom.1091@email.com"]
            for i in form:
                i.send_keys(x[form.index(i)])
            send_buttom.click()
        elif field == 'text':
            driver = R.initroot()
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, subject_field, email_field]
            x = [i for i in DO.test_details if DO.test_details.index(i) != -1]
            for i in form:
                i.send_keys(x[form.index(i)])
            time.sleep(2)
            send_buttom.click()
    elif not valid:
        if field == '':
            raise Exception("Must Enter an field for invalid test!")
        elif field == 'name':
            driver = R.initroot()
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [subject_field, email_field, text_field]
            name_field.send_keys(input("Enter your test keys: "))
            for i in form:
                i.send_keys(DO.test_details[form.index(i) + 1])
            time.sleep(2)
            send_buttom.click()
        elif field == 'subject':
            driver = R.initroot()
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            form = [name_field, email_field, text_field]
            x = [i for i in DO.test_details if i != "Ballon d'Or"]
            subject_field.send_keys(input("Enter your test keys: "))
            for i in form:
                i.send_keys(x[form.index(i)])
            time.sleep(2)
            send_buttom.click()
        elif field == 'email':
            driver = R.initroot()
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            form = [name_field, subject_field, text_field]
            x = [i for i in DO.test_details if i != "leom.1091@email.com"]
            email_field.send_keys("")
            for i in form:
                i.send_keys(x[form.index(i)])
            WebDriverWait(driver, 8).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, "#wpforms-15-field_4-error"),
                    DO.email_err_msg[1]
                )
            )
            send_buttom.click()
        elif field == 'text':
            driver = R.initroot()
            name_field = driver.find_element(By.ID, "wpforms-15-field_0")
            subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
            email_field = driver.find_element(By.ID, "wpforms-15-field_4")
            send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
            text_field = driver.find_element(By.ID, "wpforms-15-field_2")
            form = [name_field, subject_field, email_field]
            x = [i for i in DO.test_details if DO.test_details.index(i) != -1]
            text_field.send_keys(input("Enter your test keys: "))
            for i in form:
                i.send_keys(x[form.index(i)])
            time.sleep(2)
            send_buttom.click()


def test_func_contact_page():
    x = input("Enter field: ")
    z = bool(input("Enter False\\True: "))
    form_input_contact_us(x, z)
