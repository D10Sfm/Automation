from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class Firefox:
    global driver
    def __init__(self,base_url="https://www.google.com/"):
        self.base_url = base_url
    def openBrowser(self):
        driver = webdriver.Firefox(executable_path="C:\\Users\\Dell\\Desktop\\AutoMation Subjects\\Selenium\\WebDriver(Browsers)\FireFox\\geckodriver.exe")
        f = driver.get(self.base_url)

    def find_element(self,identifier='',typeof=''):
        if identifier == '':
            raise Exception("Need To enter an identifier")
        else:
            if typeof == 'class name':
                s = driver.find_element(by=By.CLASS_NAME, value=identifier)
                return s
            elif typeof == 'id':
                s = driver.find_element(by=By.ID, value=identifier)
                return s
            elif typeof == 'css_selector':
                s = driver.find_element(by=By.CSS_SELECTOR, value=identifier)
                return s
            elif typeof == 'name':
                s = driver.find_element(by=By.NAME, value=identifier)
                return s
            elif typeof == 'xpath':
                s = driver.find_element(by=By.XPATH, value=identifier)
                return s
            elif typeof == 'partial_link_text':
                s = driver.find_element(by=By.PARTIAL_LINK_TEXT, value=identifier)
                return s
            elif typeof == 'tag name':
                s = driver.find_element(by=By.TAG_NAME, value=identifier)
                return s
            else:
                raise Exception(f"There is not finder like {typeof}")


    def action(self,x='',action=''):
        f = self.find_element()
        if action == 'click':
            f.click()
        elif action == 'send keys':
            f.send_keys(x)
        else:
            raise TypeError


