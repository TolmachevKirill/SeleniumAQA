# test_bank_operations.py

import pytest
from utils.helpers import calculate_fibonacci
from datetime import date

@pytest.mark.usefixtures("setup_pages")
class TestBankOperations:
    def test_bank_operations(self, setup_pages):
        login_page, account_page, transactions_page = setup_pages

        # Авторизация пользователя "Harry Potter"
        login_page.login_as_user("Harry Potter")

        # Вычисление N-го числа Фибоначчи
        fib_number = calculate_fibonacci(date.today().day + 1)

        # Пополнение счета на сумму, равную N-му числу Фибоначчи
        account_page.deposit(fib_number)

        # Списание со счета на ту же сумму
        account_page.withdraw(fib_number)

        # Проверка баланса - должен быть равен 0
        balance = account_page.get_balance()
        assert balance == "0", f"Expected balance to be 0, but it was {balance}"

        # Переход на страницу транзакций и проверка наличия транзакций
        transactions_page.open_transactions_page()
        transactions = transactions_page.get_transactions()
        assert len(transactions) >= 2, "Transactions not recorded correctly"
