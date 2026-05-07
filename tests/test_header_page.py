import allure
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from helps.data import Questions, Urls
from locators.home_page_locators import HomePageLocators
from pages.home_page import HomePage, HomePageHeader
from pages.dzen_page import DzenPage


class TestMainPage:

    @allure.title('Тест проверки перехода на главную страницу DZEN по клику на логотип "Яндекс"')
    @allure.description('''1) Кликаем на логотип "Яндекс"
                        2) Переключаемся на новую вкладку
                        3) Ожидаем загрузки нужного URL
                        4) Сравниваем текущий URL с ожидаемым и проверяем наличие элемента на странице''')
    def test_yandex_logo_click(self, driver):
        header_page = HomePageHeader(driver)
        dzen_page = DzenPage(driver)
        
        header_page.yandex_logo_click()      # клик по логотипу Яндекса (открывает новую вкладку)
        header_page.go_to_new_tab()          # переключаемся на новую вкладку
        
        # Явное ожидание: URL станет равен ожидаемому адресу Дзена
        WebDriverWait(driver, 10).until(EC.url_to_be(Urls.DZEN_URL))
        
        current_url = header_page.get_current_url()
        assert current_url == Urls.DZEN_URL and dzen_page.check_element_main_button()
