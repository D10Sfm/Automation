import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from colorama import Fore
from colorama import Style

import Tests.Utitlitis.GlobalFunctionETC.documents as DO
import Tests.Utitlitis.ContactUs.root as R


def test_ui_top_page():
    driver = R.initroot()
    driver.implicitly_wait(12)
    navbar = driver.find_element(By.XPATH,
                                 "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div[2]").text.split(
        "\n")
    count = 0
    flag = True
    try:
        for element, expected in zip(navbar, DO.navbar_validetion):
            if element == expected:
                count += 1
        if count == 7:
            print(f"{navbar}\n The above navbar is stands on demands!")
        else:
            print(f"{navbar}\nThe above navbar is not stands on demands!")
        search_logo = driver.find_element(By.XPATH,
                                          "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div[1]/div["
                                          "3]/div[2]/div[1]/div[1]/a[1]")
        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of(search_logo)
            )
        except:
            print("The search bar logo is not stands on demands! ")

        sum_price_cart_logo = driver.find_element(By.XPATH,
                                                  "//header/div[@id='ast-desktop-header']/div[1]/div[1]/div[1]/div["
                                                  "1]/div[3]/div[3]/div[1]/div[1]")
        try:
            WebDriverWait(driver, 15).until(
                EC.visibility_of(sum_price_cart_logo)
            )
        except:
            print("The cart logo or the price are not stands on demands! ")
        h1_page_title = driver.find_element(By.XPATH, "//h1[contains(text(),'Contact Us')]").text
        assert h1_page_title == 'Contact Us'
        accessibility_icon = driver.find_element(By.XPATH, "/html[1]/body[1]/nav[1]/div[1]/a[1]")
        try:
            WebDriverWait(driver, 10).until(
                EC.visibility_of(accessibility_icon)
            )
        except:
            print("The accessibility icon not stands on demends!")
    except:
        flag += False
    if flag:
        print(Fore.BLUE + Style.DIM + "Test Pass Succesfully!" + Style.RESET_ALL)
    else:
        print(Fore.RED + Style.DIM + "not all tests pass!" + Style.RESET_ALL)


def test_ui_mid_page():
    driver = R.initroot()
    left_col_title = driver.find_element(By.XPATH, "//h3[contains(text(),'You tell us. We listen.')]").text
    left_col_email = driver.find_element(By.XPATH, "//span[contains(text(),'hello@atid.store')]").text
    left_col_schedule = driver.find_element(By.XPATH,
                                            "//span[contains(text(),'Sunday to Thursday - 9:00 am to 7:00 pm')]").text
    left_col_friday_schedule = driver.find_element(By.XPATH,
                                                   "//span[contains(text(),'Friday - 8:00 am to 3:00 pm')]").text
    left_col_help_title = driver.find_element(By.XPATH, "//h4[contains(text(),'Need Help? Call Us.')]").text
    left_col_phone_number = driver.find_element(By.XPATH, "//h3[contains(text(),'972-52-1234567')]").text
    left_col_elements_txt = [left_col_title, left_col_email, left_col_schedule, left_col_friday_schedule,
                             left_col_help_title, left_col_phone_number]
    validetion_left_col_txt = [i for i in left_col_elements_txt]
    assert left_col_elements_txt == validetion_left_col_txt
    time.sleep(2)
    right_col_title = driver.find_element(By.XPATH,
                                          "/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/article[1]/div["
                                          "1]/div[1]/div[1]/section[2]/div[1]/div[2]/div[1]/div[1]/div[1]/h3[1]").text
    right_col_name_field = driver.find_element(By.ID, "wpforms-15-field_0")
    right_col_subject_field = driver.find_element(By.ID, "wpforms-15-field_5")
    right_col_email_field = driver.find_element(By.ID, "wpforms-15-field_4")
    right_col_text_field = driver.find_element(By.ID, "wpforms-15-field_2")
    send_buttom = driver.find_element(By.ID, "wpforms-submit-15")
    form = [right_col_title, right_col_name_field, right_col_subject_field, right_col_email_field, right_col_text_field,
            send_buttom]
    assert form[0] == "Have any Queries? We're here to help."
    for i in form[1:]:
        WebDriverWait(driver, 10).until(
            EC.visibility_of(i)
        )


def test_ui_bottom_page():
    driver = R.initroot()
    img_contact_1 = driver.find_element(By.XPATH,
                                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article["
                                        "1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div["
                                        "1]/figure[1]/img[1]")
    img_contact_2 = driver.find_element(By.XPATH,
                                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article["
                                        "1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                                        "1]/figure[1]/img[1]")
    img_contact_3 = driver.find_element(By.XPATH,
                                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article["
                                        "1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div["
                                        "1]/figure[1]/img[1]")
    img_contact_4 = driver.find_element(By.XPATH,
                                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article["
                                        "1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div["
                                        "1]/figure[1]/img[1]")
    box_contact_1 = driver.find_element(By.XPATH,
                                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article["
                                        "1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div["
                                        "1]/div[1]").text
    box_contact_2 = driver.find_element(By.XPATH,
                                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article["
                                        "1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[2]/div[1]/div[1]/div[1]/div["
                                        "1]/div[1]").text
    box_contact_3 = driver.find_element(By.XPATH,
                                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article["
                                        "1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[3]/div[1]/div[1]/div[1]/div["
                                        "1]/div[1]").text
    box_contact_4 = driver.find_element(By.XPATH,
                                        "//body/div[@id='page']/div[@id='content']/div[1]/div[1]/main[1]/article["
                                        "1]/div[1]/div[1]/div[1]/section[3]/div[1]/div[4]/div[1]/div[1]/div[1]/div["
                                        "1]/div[1]").text
    img_ls = [img_contact_1, img_contact_2, img_contact_3, img_contact_4]
    contact_ls = [box_contact_1, box_contact_2, box_contact_3, box_contact_4]
    for i in img_ls:
        WebDriverWait(driver, 10).until(
            EC.visibility_of(i)
        )

    for i, j in zip(contact_ls, DO.contact_buttom_page):
        assert i == j


def test_ui_contact_page():
    test_ui_top_page()
    test_ui_mid_page()
    test_ui_bottom_page()
