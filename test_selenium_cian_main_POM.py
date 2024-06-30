from conftest import driver
from pages.main_page import MainPage


def test_selenium_cian_main_POM(driver):
    driver.get('https://www.cian.ru/')
    main_page = MainPage(driver)
    main_page.click_daily_rent_button()
    main_page.click_search_button()
    assert driver.current_url == 'https://www.cian.ru/snyat-kvartiru-posutochno/'
