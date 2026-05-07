import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        with allure.step("Получить текущий URL страницы"):
            return self.driver.current_url

    def wait_for_url(self, expected_url, timeout=10):
        with allure.step(f"Ожидание URL: {expected_url}"):
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(expected_url))

    def wait_for_url_contains(self, partial_url, timeout=10):
        with allure.step(f"Ожидание URL, содержащего: {partial_url}"):
            WebDriverWait(self.driver, timeout).until(EC.url_contains(partial_url))

    def find_and_wait_locator(self, locator):
        with allure.step(f"Ожидание появления элемента: {locator}"):
            return WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(locator)
            )

    def click_button(self, locator):
        with allure.step(f"Клик по кнопке: {locator}"):
            self.find_and_wait_locator(locator).click()

    def send_keys_to_field(self, locator, text):
        with allure.step(f"Ввод текста '{text}' в поле: {locator}"):
            self.find_and_wait_locator(locator).send_keys(text)

    def get_text_locator(self, locator):
        with allure.step(f"Получение текста элемента: {locator}"):
            return self.find_and_wait_locator(locator).text

    def scroll_to_locator(self, locator):
        with allure.step(f"Скролл до элемента: {locator}"):
            element = self.find_and_wait_locator(locator)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def go_to_new_tab(self):
        with allure.step("Переключиться на новую вкладку браузера"):
            self.driver.switch_to.window(self.driver.window_handles[1])

    def check_element(self, locator):
        with allure.step(f"Проверка отображения элемента: {locator}"):
            return self.find_and_wait_locator(locator).is_displayed()
