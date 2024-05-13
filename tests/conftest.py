# conftest.py

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.transactions_page import TransactionsPage

@pytest.fixture(scope="session")
def driver():
    """Фикстура для инициализации сессии WebDriver."""
    grid_url = "http://localhost:4444/wd/hub"
    options = Options()
    options.headless = False  # Вы можете установить значение True, если хотите запускать Chrome в фоновом режиме
    options.add_argument("--window-size=1920,1080")  # Настройка размера окна браузера
    driver = webdriver.Remote(command_executor=grid_url, options=options)
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def setup_pages(driver):
    """Фикстура для инициализации страниц, используемых в тестах."""
    login_page = LoginPage(driver)
    account_page = AccountPage(driver)
    transactions_page = TransactionsPage(driver)
    return login_page, account_page, transactions_page

