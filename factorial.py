"""Средняя 4. Факториал через reduce.

>>> factorial(0)
1
>>> factorial(5)
120
>>> [factorial(n) for n in range(1, 8)]
[1, 2, 6, 24, 120, 720, 5040]
>>> double_factorial(7)
105
>>> factorial(-3)
Traceback (most recent call last):
...
ValueError: факториал определён только для n >= 0
"""
from functools import reduce
from operator import mul


def factorial(n):
    """n! как свёртка произведения чисел 1..n (для 0 — начальное 1)."""
    if n < 0:
        raise ValueError("факториал определён только для n >= 0")
    return reduce(lambda acc, x: acc * x, range(1, n + 1), 1)


def double_factorial(n):
    """n!! — произведение чисел той же чётности, что и n.

    >>> double_factorial(8)
    384
    """
    return reduce(mul, range(n, 0, -2), 1)


def factorial_steps(n):
    """Промежуточные значения свёртки — видно, как reduce копит результат.

    >>> factorial_steps(4)
    [1, 2, 6, 24]
    """
    steps = []
    reduce(lambda acc, x: steps.append(acc * x) or acc * x,
           range(1, n + 1), 1)
    return steps


if __name__ == "__main__":
    for n in (0, 1, 5, 10, 20):
        print(f"{n}! = {factorial(n)}")
    print("Шаги для 6!:", " -> ".join(map(str, factorial_steps(6))))
    print("7!! =", double_factorial(7), " 8!! =", double_factorial(8))
    n = int(input("Введите n: ") or 12)
    print(f"{n}! = {factorial(n)}")
