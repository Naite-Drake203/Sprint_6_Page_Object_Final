import allure
import pytest

from helps.data import Users
from pages.home_page import HomePage, HomePageHeader
from pages.order_page import OrderPage


class TestOrderPage:

    @allure.title('Позитивный тест оформления заказа')
    @allure.description('''Параметризованный тест: 
        1) Клик на кнопку "Заказать" (через хедер или через скролл на главной странице);
        2) Заполнение данных "Для кого самокат" → "Далее";
        3) Заполнение данных "Про аренду" → "Заказать";
        4) Подтверждение заказа, проверка окна с текстом оформления''')
    @pytest.mark.parametrize('click_method, user', [
        ('header', Users.user),
        ('home_page', Users.user_2)
    ])
    def test_order_scooter(self, driver, click_method, user):
        if click_method == 'header':
            header_page = HomePageHeader(driver)
            header_page.order_button_click()
        elif click_method == 'home_page':
            home_page = HomePage(driver)
            home_page.scroll_and_click_on_the_order_button()

        order_page = OrderPage(driver)
        order_page.order_scooter_full_path(user)
        assert order_page.check_order_title()
