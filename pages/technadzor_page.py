from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TechnadzorPage:
    def __init__(self, driver):
        self.driver = driver
        self.check_house_button = (By.XPATH, '//div[@data-elem-id=1616497237967]')
        self.name_input = (By.XPATH, '//input[@id="nm-1531306243545"]')
        self.telephone_input = (By.XPATH, '(//input[@name="tildaspec-phone-part[]"])[2]')
        self.submit_button = (By.XPATH, '(//button[@type="submit"])[2]')
        self.privacy_policy_link = (By.XPATH, '(//div//a[@href="https://promo.cian.ru/technadzor/privacy-policy"])[2]')
        self.politika_konfidencialnosti_link = (By.XPATH, '(//div//a[@href="https://www.cian.ru/legal-documents/politika_konfidencialnosti_0/"])[2]')

    def click_check_house_button(self):
        check_house_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.check_house_button)
        )
        check_house_button.click()

    def enter_name(self, name):
        name_input = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.name_input)
        )
        name_input.send_keys(name)

    def enter_telephone(self, telephone):
        telephone_input = WebDriverWait(self.driver, 3).until(
            EC.presence_of_element_located(self.telephone_input)
        )
        telephone_input.send_keys(telephone)

    def click_submit_button(self):
        submit_button = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.submit_button)
        )
        submit_button.click()

    def click_privacy_policy_link(self):
        privacy_policy_link = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.privacy_policy_link)
        )
        privacy_policy_link.click()

    def click_politika_konfidencialnosti_link(self):
        politika_konfidencialnosti_link = WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(self.politika_konfidencialnosti_link)
        )
        politika_konfidencialnosti_link.click()
