# login_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.customer_login_button = (By.CSS_SELECTOR, "button[ng-click^='customer']")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.username_dropdown = (By.CSS_SELECTOR, "#userSelect")

    def navigate_to_login_page(self):
        self.driver.get("https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login")

    def select_user(self, username):
        self.click_element(self.customer_login_button)
        self.click_element(self.username_dropdown)
        # Пауза для визуальной проверки
        WebDriverWait(self.driver, self.timeout).until(
            EC.element_to_be_clickable((By.XPATH, f"//option[normalize-space()='{username}']"))
        ).click()

    def login(self):
        self.click_element(self.login_button)

    def login_as_user(self, username):
        self.navigate_to_login_page()
        self.select_user(username)
        self.login()

