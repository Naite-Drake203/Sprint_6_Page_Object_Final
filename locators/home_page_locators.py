from selenium.webdriver.common.by import By


class HomePageHeaderLocators:
    """Локаторы элементов хедера (верхняя панель)"""

    # Логотип Яндекса – используем contains, так как класс может меняться
    logo_yandex = (By.XPATH, "//a[contains(@class, 'Header_LogoYandex')]")

    # Логотип Самоката
    logo_scooter = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]")

    # Кнопка «Заказать» в хедере – ищем внутри контейнера с классом Header
    order_button = (By.XPATH, "//div[contains(@class, 'Header')]//button[text()='Заказать']")

    # Кнопка «Статус заказа»
    order_status_button = (By.XPATH, "//button[text()='Статус заказа']")

    # Поле ввода номера заказа (рядом с кнопкой Go!)
    number_order_field = (By.XPATH, "//input[contains(@class, 'Header_Input')]")

    # Кнопка «Go!»
    go_button = (By.XPATH, "//button[text()='Go!']")

    # Поле «Введите номер заказа» (на странице «Статус заказа»)
    track_field = (By.XPATH, "//input[@placeholder='Введите номер заказа']")

    # Кнопка «Посмотреть»
    view_button = (By.XPATH, "//button[text()='Посмотреть']")

    # Заголовок «Учебный тренажёр» (в хедере)
    header_page_title = (By.XPATH, "//div[text()='Учебный тренажер']")


class HomePageLocators:
    """Локаторы элементов главной страницы (контент)"""

    # Заголовок главной страницы
    home_page_title = (By.XPATH, "//div[contains(@class, 'Home_Header')]")

    # Кнопка «Заказать» в центре страницы – ищем внутри блока с контентом
    order_button = (By.XPATH, "//div[contains(@class, 'Home_Content')]//button[text()='Заказать']")

    # Кнопка принятия куки
    accept_cookies_button = (By.ID, "rcc-confirm-button")

    # Заголовок блока с вопросами
    questions_title = (By.XPATH, "//div[text()='Вопросы о важном']")

    # Локаторы кнопок вопросов (аккордеон). ID уникальны и стабильны – можно использовать напрямую.
    questions = [
        (By.ID, "accordion__heading-0"),
        (By.ID, "accordion__heading-1"),
        (By.ID, "accordion__heading-2"),
        (By.ID, "accordion__heading-3"),
        (By.ID, "accordion__heading-4"),
        (By.ID, "accordion__heading-5"),
        (By.ID, "accordion__heading-6"),
        (By.ID, "accordion__heading-7")
    ]

    # Локаторы текстов ответов
    questions_text = [
        (By.ID, "accordion__panel-0"),
        (By.ID, "accordion__panel-1"),
        (By.ID, "accordion__panel-2"),
        (By.ID, "accordion__panel-3"),
        (By.ID, "accordion__panel-4"),
        (By.ID, "accordion__panel-5"),
        (By.ID, "accordion__panel-6"),
        (By.ID, "accordion__panel-7")
    ]
комент ревьюера
Необходимо исправить здесь и далее: не стоит использовать в локаторах путь от рута, абсолютный путь или индексы элемента. Это делает локатор очень хрупким
    """Хедер"""
    logo_yandex = (By.XPATH, ".//a[@class = 'Header_LogoYandex__3TSOI']")
    logo_scooter = (By.XPATH, ".//a[@class = 'Header_LogoScooter__3lsAR']")
    order_button = (By.XPATH, "(.//button[text() = 'Заказать'])[1]")

class HomePageLocators:
    """Главная страница сервиса"""
    home_page_title = (By.XPATH, ".//div[@class = 'Home_Header__iJKdX']")
    order_button = (By.XPATH, "(//button[text() = 'Заказать'])[2]")
