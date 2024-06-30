from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.daily_rent_button = (By.XPATH, '//div//a[@href="/posutochno/"]')
        self.search_button = (By.XPATH, '//span//a[@href="https://www.cian.ru/snyat-kvartiru-posutochno/"]')

    def click_daily_rent_button(self):
        elem = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.daily_rent_button)
        )
        elem.click()

    def click_search_button(self):
        button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.search_button)
        )
        button.click()
