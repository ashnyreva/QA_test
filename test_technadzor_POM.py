from conftest import driver
from pages.technadzor_page import TechnadzorPage


def test_technadzor_POM(driver):
    driver.get('https://promo.cian.site/technadzor')
    technadzor = TechnadzorPage(driver)
    technadzor.click_check_house_button()
    assert technadzor.applying_popup_show(), "Модальное окно не отображается на странице"
