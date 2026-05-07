import allure
import pytest

from helps.data import Users
from pages.home_page import HomePage, HomePageHeader
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Позитивный тест оформления заказа по кнопке "Заказать" в хедере')
    @allure.description('''1) Клик на кнопку "Заказать" в хедере;
        2) Заполнение данных "Для кого самокат" → "Далее";
        3) Заполнение данных "Про аренду" → "Заказать";
        4) Подтверждение заказа, проверка окна с текстом оформления''')
    def test_order_scooter_by_header_button(self, driver):
        header_page = HomePageHeader(driver)
        header_page.order_button_click()
        order_page = OrderPage(driver)
        order_page.order_scooter_full_path(Users.user)
        assert order_page.check_order_title()

    @allure.title('Позитивный тест оформления заказа по кнопке "Заказать" на главной странице')
    @allure.description('''1) Скролл до кнопки "Заказать" на главной странице и клик;
        2) Заполнение данных "Для кого самокат" → "Далее";
        3) Заполнение данных "Про аренду" → "Заказать";
        4) Подтверждение заказа, проверка окна с текстом оформления''')
    def test_order_scooter_by_home_page_button(self, driver):
        home_page = HomePage(driver)
        home_page.scroll_and_click_on_the_order_button()
        order_page = OrderPage(driver)
        order_page.order_scooter_full_path(Users.user_2)
        assert order_page.check_order_title()
