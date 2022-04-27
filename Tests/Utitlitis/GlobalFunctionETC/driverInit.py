import Tests.Utitlitis.GlobalFunctionETC.documents as DO
from selenium import webdriver

def initroot():
    driver = webdriver.Chrome(
        executable_path=DO.driver_executable_path)
    return driver


def init_home_page():
    driver = webdriver.Chrome(
        executable_path=DO.driver_executable_path)

    driver.get(DO.base_url)
    driver.maximize_window()
    return driver