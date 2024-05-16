# Тестовое задание: Автоматизация банковских операций с использованием Selenium Grid и Allure

## Описание

Данный проект представляет собой автоматизацию тестирования банковских операций на веб-сайте [GlobalSQA Banking Project](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login) с использованием следующих технологий:
- Selenium Grid для запуска тестов
- Паттерн проектирования Page Object
- Формирование отчетов с использованием Allure

## Технологии

- Python
- Selenium WebDriver
- Selenium Grid
- Allure

## Задание

В рамках данного задания выполнены следующие шаги:
1. Установка и настройка Selenium Grid.
2. Реализация тестов с использованием паттерна Page Object.
3. Открытие браузера с помощью Selenium и переход на страницу [GlobalSQA Banking Project](https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login).
4. Авторизация под пользователем "Harry Potter".
5. Вычисление N-го числа Фибоначчи, где N - это текущий день месяца + 1.
6. Пополнение счета на сумму, равную вычисленному числу Фибоначчи.
7. Списание со счета на сумму, равную вычисленному числу Фибоначчи.
8. Проверка баланса - он должен быть равен нулю.
9. Проверка наличия транзакций на странице транзакций.
10. Формирование CSV-файла с данными о проведенных транзакциях.
11. Прикрепление сформированного CSV-файла к отчету Allure.

## Установка

### 1. Клонирование репозитория

```bash
git clone https://github.com/TolmachevKirill/SeleniumAQA.git
cd SeleniumAQA
```

### 2. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 3. Установка и настройка Selenium Grid

Следуйте [официальной документации Selenium Grid](https://www.selenium.dev/documentation/grid/) для установки и настройки Grid.

### 4. Настройка Allure

Следуйте [официальной документации Allure](https://docs.qameta.io/allure/) для установки и настройки Allure.

## Запуск тестов

### 1. Запуск Selenium Grid

Запустите хаб и ноды Selenium Grid.

### 2. Запуск тестов

```bash
pytest --alluredir=allure-results
```

### 3. Формирование отчета Allure

```bash
allure serve allure-results
```

## Структура проекта

- `pages/` - директория с реализацией паттерна Page Object.
- `tests/` - директория с тестовыми сценариями.
- `utils/` - утилиты и вспомогательные функции (например, для вычисления числа Фибоначчи и формирования CSV-файлов).
- `allure-results/` - директория для хранения результатов тестов Allure.

## Отчет Allure

После выполнения тестов отчет Allure можно открыть с помощью команды:

```bash
allure serve allure-results
```

## Пример CSV-файла

CSV-файл с данными о проведенных транзакциях будет иметь следующий формат:

```csv
Дата-времяТранзакции,Сумма,ТипТранзакции
"15 Май 2024 14:23:45",21,Credit
"15 Май 2024 14:24:10",21,Debit
```

## Контакты

Если у вас возникли вопросы или предложения, пожалуйста, свяжитесь с нами по электронной почте [tolmachev.kirill@yahoo.com].
