# transactions_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage

class TransactionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.transactions_table = (By.CSS_SELECTOR, ".table")
        self.transaction_rows = (By.CSS_SELECTOR, "tbody>tr")
        self.reset_button = (By.CSS_SELECTOR, "button[ng-click='reset()']")

    def get_transactions(self):
        """
        Получает список всех транзакций со страницы транзакций.

        :return: Список кортежей, каждый из которых представляет транзакцию (дата, сумма, тип).
        """
        transactions = []
        # Ожидаем загрузку таблицы транзакций
        self.wait_for_element(self.transactions_table)
        rows = self.driver.find_elements(*self.transaction_rows)
        for row in rows:
            # Получаем данные из каждой строки таблицы
            cells = row.find_elements(By.TAG_NAME, "td")
            if len(cells) == 4:  # Убедимся, что строка содержит все необходимые данные
                date_time = cells[0].text
                transaction_type = cells[1].text
                amount = cells[2].text
                transactions.append((date_time, amount, transaction_type))
        return transactions

    def reset_transactions(self):
        """
        Сбрасывает фильтр транзакций, чтобы можно было увидеть все транзакции снова.
        """
        self.click_element(self.reset_button)
