from selenium import webdriver


def initroot():
    driver = webdriver.Chrome(
        executable_path='C:/Users/Dell/Desktop/AutoMation Subjects/Selenium/WebDriver(Browsers)/Chrome/chromedriver.exe')
    return driver


def init_home_page():
    driver = webdriver.Chrome(
        executable_path='C:/Users/Dell/Desktop/AutoMation Subjects/Selenium/WebDriver(Browsers)/Chrome/chromedriver.exe')

    driver.get("https://atid.store/")
    driver.maximize_window()
    return driver

# # def test_search_exist_product_has_quantity1_EC(page):
# #     driver = init()
# #     if page == 'men':
# #         men = driver.find_element(by=By.XPATH,
# #                                   value="//body[1]/div[1]/header[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/nav[1]/div[1]/ul[1]/li[3]/a[1]")
# #         men.click()
# #         time.sleep(3)
# #         search_input = driver.find_element(by=By.ID, value="wc-block-search__input-1")
# #         search_input.send_keys('Anchor Bracelet')
# #         search_button = driver.find_element(by=By.CLASS_NAME, value="wc-block-product-search__button")
# #         search_button.click()
# #         WebDriverWait(driver,5).until(
# #             EC.text_to_be_present_in_element(
# #                 (By.XPATH,"//h1[contains(text(),'Anchor Bracelet')]"),
# #                 'anchor Bracelet'
# #             )
# #         )
# #         time.sleep(2)
