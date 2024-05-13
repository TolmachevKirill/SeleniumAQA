# base_page.py

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
import logging
import time


class BasePage:
    def __init__(self, driver: WebDriver, timeout: int = 30):
        """
        Инициализирует базовую страницу, которая будет использоваться как родительский класс для всех других страниц.

        :param driver: Экземпляр драйвера WebDriver.
        :param timeout: Время ожидания для операций, связанных с поиском элементов.
        """
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        """
        Поиск элемента с применением явного ожидания.

        :param locator: Локатор элемента для поиска.
        :return: Найденный элемент.
        """
        try:
            return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            logging.error(f"Timeout while finding element with locator: {locator}")
            raise


    def click_element(self, locator):
        """
        Кликает на элемент с задержкой перед взаимодействием.
        """
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable(locator)
        )
        time.sleep(0.5)  # Задержка для устойчивости состояния элемента
        self.find_element(locator).click()

    def enter_text(self, locator, text):
        """
        Вводит текст в элемент, когда он становится доступен для ввода.

        :param locator: Локатор элемента для ввода текста.
        :param text: Текст для ввода.
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            element.clear()  # Очищаем поле перед вводом текста
            element.send_keys(text)
        except TimeoutException:
            logging.error(f"Timeout while entering text into element with locator: {locator}")
            raise

    def is_element_visible(self, locator):
        """
        Проверяет видимость элемента.

        :param locator: Локатор элемента для проверки.
        :return: True, если элемент видим, иначе False.
        """
        try:
            WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            logging.error(f"Element with locator {locator} is not visible")
            return False

    def get_element_text(self, locator):
        """
        Получает текст элемента.

        :param locator: Локатор элемента.
        :return: Текст элемента.
        """
        try:
            element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))
            return element.text
        except TimeoutException:
            logging.error(f"Timeout while getting text from element with locator: {locator}")
            raise
