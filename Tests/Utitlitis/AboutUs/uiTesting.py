import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from colorama import Fore
from colorama import Style


import Tests.Utitlitis.GlobalFunctionETC.documents as DO
import Tests.Utitlitis.ContactUs.root as R
import Tests.Utitlitis.GlobalFunctionETC.driverInit as DR



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
    driver = DR.initroot()
    driver.get(DO.about_us_url)
    left_contact = driver.find_element(By.XPATH,"//section[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]")
    right_hero_img = driver.find_element(By.XPATH,"//section[1]/div[1]/div[2]/div[1]/div[2]/div[1]/img[1]")
    buttom_head_hero = driver.find_element(By.XPATH,"//section[3]/div[1]/div[1]/div[1]/div[2]")
    buttom_contact_hero = driver.find_element(By.XPATH,"//section[3]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]")
    top_hero_section = driver.find_element(By.XPATH,"//section[3]/div[1]/div[1]/div[1]/section[1]/div[1]")
    buttom_hero_section = driver.find_element(By.XPATH,"//section[3]/div[1]/div[1]/div[1]/section[2]/div[1]")
    section_images = [top_hero_section.find_elements(By.TAG_NAME,"img"),buttom_hero_section.find_elements(By.TAG_NAME,"img")]
    contact_hero_header = [top_hero_section.find_elements(By.TAG_NAME,"h4"),buttom_hero_section.find_elements(By.TAG_NAME,"h4")]
    contact_hero_para = [top_hero_section.find_elements(By.TAG_NAME,"p"),buttom_hero_section.find_elements(By.TAG_NAME,"p")]
    contact = [left_contact,buttom_head_hero,buttom_contact_hero]
    # for i,j in zip(contact,):
    print(left_contact.text)

def test_ui_bottom_page():
    driver = DR.initroot()
    driver.get(DO.about_us_url)
    img_contact_1 = driver.find_element(By.XPATH,"//section[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/figure[1]/img[1]")
    img_contact_2 = driver.find_element(By.XPATH,"//section[5]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/figure[1]/img[1]")
    img_contact_3 = driver.find_element(By.XPATH,"//section[5]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/figure[1]/img[1]")
    img_contact_4 = driver.find_element(By.XPATH,"//section[5]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/figure[1]/img[1]")
    box_contact_1 = driver.find_element(By.XPATH,"//section[5]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]").text
    box_contact_2 = driver.find_element(By.XPATH,"//section[5]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]").text
    box_contact_3 = driver.find_element(By.XPATH,"//section[5]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]").text
    box_contact_4 = driver.find_element(By.XPATH,"//section[5]/div[1]/div[4]/div[1]/div[1]/div[1]/div[1]/div[1]").text
    img_ls = [img_contact_1, img_contact_2, img_contact_3, img_contact_4]
    contact_ls = [box_contact_1, box_contact_2, box_contact_3, box_contact_4]
    for i in img_ls:
        WebDriverWait(driver, 10).until(
            EC.visibility_of(i)
        )

    for i, j in zip(contact_ls, DO.contact_buttom_page):
        assert i == j

test_ui_mid_page()

