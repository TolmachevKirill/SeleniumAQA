from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

# Адрес и порт Selenium Grid
grid_url = "http://localhost:4444/"

# Создаем экземпляр WebDriver, подключенный к Selenium Grid
driver = WebDriver(command_executor=grid_url, desired_capabilities={})

# Проверяем соединение
try:
    # Отправляем пустой запрос для проверки соединения
    driver.get("about:blank")
    print("Успешное подключение к Selenium Grid по адресу:", grid_url)
except Exception as e:
    print("Ошибка подключения к Selenium Grid:", e)
finally:
    # Закрываем драйвер после проверки
    driver.quit()