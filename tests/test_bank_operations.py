# test_bank_operations.py

import allure
import pytest
from utils.helpers import calculate_fibonacci
from datetime import date

@pytest.mark.usefixtures("setup_pages")
class TestBankOperations:
    @allure.feature('Bank Operations')
    @allure.story('Complete Bank Transaction Cycle')
    def test_bank_operations(self, setup_pages):
        login_page, account_page, transactions_page = setup_pages

        with allure.step('Login as Harry Potter'):
            login_page.login_as_user("Harry Potter")

        with allure.step('Calculate Fibonacci Number'):
            fib_number = calculate_fibonacci(date.today().day + 1)

        with allure.step('Deposit Amount Equal to Fibonacci Number'):
            account_page.deposit(fib_number)

        with allure.step('Withdraw the Same Amount'):
            account_page.withdraw(fib_number)

        with allure.step('Check Balance is Zero'):
            balance = account_page.get_balance()
            assert balance == "0", f"Expected balance to be 0, but it was {balance}"

        with allure.step('Navigate to Transactions Page'):
            transactions_page.open_transactions_page()

        with allure.step('Get and Validate Transactions'):
            transactions = transactions_page.get_transactions()
            assert len(transactions) >= 2, "Transactions not recorded correctly"

        with allure.step('Save Transactions to CSV'):
            csv_file_path = transactions_page.save_transactions_to_csv(transactions)

        with allure.step('Attach Transactions CSV to Allure Report'):
            with open(csv_file_path, 'rb') as f:
                allure.attach(f.read(), name="transactions.csv", attachment_type=allure.attachment_type.CSV)
