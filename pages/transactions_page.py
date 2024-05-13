# transactions_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage

class TransactionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.transactions_table = (By.CSS_SELECTOR, ".table")
        self.transaction_rows = (By.CSS_SELECTOR, "tbody tr")
        self.reset_button = (By.CSS_SELECTOR, "button[ng-click='reset()']")
        self.transactions_button = (By.CSS_SELECTOR, "button[ng-click='transactions()']")

    def get_transactions(self):
        """
        Получает список всех транзакций со страницы транзакций.

        :return: Список кортежей, каждый из которых представляет транзакцию (дата, сумма, тип).
        """
        self.wait_for_element(self.transactions_table)  # Убедитесь, что таблица загрузилась
        rows = self.driver.find_elements(*self.transaction_rows)
        transactions = []
        for row in rows:
            data = row.find_elements(By.TAG_NAME, "td")
            if len(data) == 3:  # Убедитесь, что в строке именно три столбца
                date_time = data[0].text
                amount = data[1].text
                transaction_type = data[2].text
                transactions.append((date_time, amount, transaction_type))
        return transactions

    def reset_transactions(self):
        """
        Сбрасывает фильтр транзакций, чтобы можно было увидеть все транзакции снова.
        """
        self.click_element(self.reset_button)

    def open_transactions_page(self):
        """
        Открывает страницу транзакций.
        """
        self.click_element(self.transactions_button)
