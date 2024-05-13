# helpers.py

def calculate_fibonacci(n):
    """
    Вычисляет n-е число Фибоначчи.
    Пример использования: calculate_fibonacci(9) -> 21

    :param n: Позиция числа в последовательности Фибоначчи.
    :return: n-е число Фибоначчи.
    """
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
