# Exemplary calculator functions
"""Simple python calculator"""


def add(a: int, b: int) -> int:
    """Add two numbers a + b"""
    return a + b


def subtract(a: int, b: int) -> int:
    """Substract two numbers a - b"""
    return a - b


def multiply(a: int, b: int) -> int:
    """Multiply two numbers a * b"""
    return a * b


def divide(a: int, b: int) -> float:
    """Divide two numbers a / b"""
    return a / b


def dec_to_bin(n: int) -> str:
    """Convert a decimal number to binary."""
    res = ""
    if n == 0:
        return "0"

    while n > 0:
        res = str(n % 2) + res
        n //= 2
    return res
