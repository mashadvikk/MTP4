"""Средняя 6. Генератор простых чисел.

>>> list(primes_up_to(30))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
>>> list(primes_up_to(1))
[]
>>> twin_primes(50)
[(3, 5), (5, 7), (11, 13), (17, 19), (29, 31), (41, 43)]
"""


def is_prime(n):
    """Проверка делением на нечётные числа до корня.

    >>> [n for n in range(15) if is_prime(n)]
    [2, 3, 5, 7, 11, 13]
    """
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % d for d in range(3, int(n ** 0.5) + 1, 2))


def primes_up_to(limit):
    """Генератор: выдаёт простые числа от 2 до limit по одному."""
    for n in range(2, limit + 1):
        if is_prime(n):
            yield n


def twin_primes(limit):
    """Пары простых-«близнецов» p и p + 2, где p <= limit."""
    return [(p, p + 2) for p in primes_up_to(limit) if is_prime(p + 2)]


if __name__ == "__main__":
    gen = primes_up_to(100)
    print("Генератор:", gen)
    print("Первые три через next:", next(gen), next(gen), next(gen))
    print("Остальные до 100:", list(gen))
    print("Простых до 1000:", sum(1 for _ in primes_up_to(1000)))
    print("Близнецы до 50:", twin_primes(50))
