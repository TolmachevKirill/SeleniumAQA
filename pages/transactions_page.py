# transactions_page.py

from datetime import datetime
from selenium.webdriver.common.by import By
from .base_page import BasePage
import csv
import os

class TransactionsPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.transactions_table = (By.CSS_SELECTOR, ".table")
        self.transaction_rows = (By.CSS_SELECTOR, "tbody tr")
        self.reset_button = (By.CSS_SELECTOR, "button[ng-click='reset()']")
        self.transactions_button = (By.CSS_SELECTOR, "button[ng-click='transactions()']")

    def parse_date(self, date_str):
        # Преобразование из 'May 13, 2024 9:07:49 PM' в '13 May 2024 21:07:49'
        return datetime.strptime(date_str, '%b %d, %Y %I:%M:%S %p').strftime('%d %b %Y %H:%M:%S')

    def get_transactions(self):
        """
        Получает список всех транзакций со страницы транзакций.
        """
        self.wait_for_element(self.transactions_table)
        rows = self.driver.find_elements(*self.transaction_rows)
        transactions = []
        for row in rows:
            data = row.find_elements(By.TAG_NAME, "td")
            if len(data) == 3:
                date_time = self.parse_date(data[0].text)
                amount = data[1].text
                transaction_type = data[2].text
                transactions.append((date_time, amount, transaction_type))
        return transactions

    def save_transactions_to_csv(self, transactions, filename="transactions.csv"):
        file_path = os.path.join("C:/Users/V/PycharmProjects/SimbirSoft/reports", filename)
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Дата-времяТранзакции', 'Сумма', 'ТипТранзакции'])
            for transaction in transactions:
                writer.writerow(transaction)
        return file_path

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
