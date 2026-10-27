"""Средняя 10. Применить несколько функций к списку через map.

>>> apply_all([abs, str], [-2, 3])
{'abs': [2, 3], 'str': ['-2', '3']}
>>> apply_chain([lambda x: x + 1, lambda x: x * 10], [1, 2, 3])
[20, 30, 40]
>>> describe([4, 1, 7])
{'min': 1, 'max': 7, 'sum': 12, 'len': 3}
"""
from functools import reduce


def apply_all(funcs, items):
    """Каждую функцию из funcs применяет ко всем элементам items.

    Внешний map проходит по функциям, внутренний — по элементам.
    """
    return dict(map(lambda f: (f.__name__, list(map(f, items))), funcs))


def apply_chain(funcs, items):
    """Функции применяются к каждому элементу по очереди (композиция)."""
    return list(map(lambda x: reduce(lambda acc, f: f(acc), funcs, x),
                    items))


def describe(numbers):
    """Несколько агрегирующих функций одним map по списку функций."""
    funcs = [min, max, sum, len]
    return dict(zip(map(lambda f: f.__name__, funcs),
                    map(lambda f: f(numbers), funcs)))


def celsius_to_f(c):
    """Перевод градусов Цельсия в Фаренгейты.

    >>> celsius_to_f(100)
    212.0
    """
    return c * 9 / 5 + 32


if __name__ == "__main__":
    words = ["Тула", "python", "Map", "ФУНКЦИЯ"]
    print("Слова:", words)
    for name, values in apply_all([str.upper, str.lower, len], words).items():
        print(f"  {name:<6} {values}")
    temps = [-10, 0, 18.5, 36.6]
    print("Температуры:", temps)
    print("  в Фаренгейтах:", apply_chain([celsius_to_f, round], temps))
    print("Статистика [3, 8, 1, 9, 4]:", describe([3, 8, 1, 9, 4]))
