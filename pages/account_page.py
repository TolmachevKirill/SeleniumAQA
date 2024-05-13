# account_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.deposit_button = (By.CSS_SELECTOR, "button[ng-click='deposit()']")
        self.withdrawl_button = (By.CSS_SELECTOR, "button[ng-click='withdrawl()']")
        self.amount_input = (By.CSS_SELECTOR, "input[type='number'][ng-model='amount']")
        self.submit_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.balance_label = (By.CSS_SELECTOR, ".balance")
        self.transactions_button = (By.CSS_SELECTOR, "button[ng-click='transactions()']")

    def perform_transaction(self, button_locator, amount):
        """
        Общий метод для выполнения транзакций (пополнение или вывод средств).

        :param button_locator: Локатор кнопки для начала транзакции.
        :param amount: Сумма для операции.
        """
        self.click_element(button_locator)
        self.enter_text(self.amount_input, str(amount))
        # Ждем пока введенное значение появится в поле ввода
        WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element_value(self.amount_input, str(amount))
        )
        time.sleep(1)  # Дополнительное ожидание перед нажатием на кнопку подтверждения
        self.click_element(self.submit_button)

    def deposit(self, amount):
        """
        Выполняет пополнение счета на указанную сумму.
        """
        self.perform_transaction(self.deposit_button, amount)

    def withdraw(self, amount):
        """
        Выполняет списание с указанного счета на заданную сумму.

        :param amount: Сумма для списания.
        """
        self.click_element(self.withdrawl_button)  # Нажать на кнопку для вывода средств
        time.sleep(2)  # Ожидание загрузки формы вывода

        # Ввод суммы для вывода
        self.enter_text(self.amount_input, str(amount))

        # Явное ожидание, чтобы убедиться, что текст в поле ввода корректен
        WebDriverWait(self.driver, self.timeout).until(
            EC.text_to_be_present_in_element_value(self.amount_input, str(amount))
        )

        time.sleep(1)  # Дополнительное ожидание перед кликом на кнопку подтверждения вывода средств
        self.click_element(self.submit_button)

    def get_balance(self):
        """
        Получает текущий баланс счета пользователя.
        """
        return self.get_element_text(self.balance_label)

    def open_transactions_page(self):
        """
        Переходит на страницу транзакций счета.
        """
        self.click_element(self.transactions_button)
