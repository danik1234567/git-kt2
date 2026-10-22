"""Простой калькулятор с базовыми арифметическими операциями."""


def add(a, b):
    """Сложение."""
    return a + b


def subtract(a, b):
    """Вычитание."""
    return a - b


def multiply(a, b):
    """Умножение."""
    return a * b


def divide(a, b):
    """Деление с проверкой деления на ноль."""
    if b == 0:
        raise ValueError("Деление на ноль невозможно")
    return a / b


if __name__ == "__main__":
    print("2 + 3 =", add(2, 3))
    print("7 - 4 =", subtract(7, 4))
    print("5 * 6 =", multiply(5, 6))
    print("8 / 2 =", divide(8, 2))
