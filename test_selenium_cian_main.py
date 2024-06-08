from selenium.webdriver.common.by import By
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_selenium_cian_main(driver):
    driver.get('https://www.cian.ru/')
    elem = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//div//a[@href="/posutochno/"]')))
    elem.click()
    button = WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable((By.XPATH, '//span//a[@href="https://www.cian.ru/snyat-kvartiru-posutochno/"]')))
    button.click()
    assert driver.current_url == 'https://www.cian.ru/snyat-kvartiru-posutochno/'
