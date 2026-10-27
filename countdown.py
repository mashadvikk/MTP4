"""Повышенная 5. Собственный класс-итератор.

>>> list(Countdown(5))
[5, 4, 3, 2, 1]
>>> list(Countdown(10, stop=0, step=3))
[10, 7, 4, 1]
>>> it = Countdown(2)
>>> next(it), next(it)
(2, 1)
>>> next(it)
Traceback (most recent call last):
...
StopIteration
>>> list(Cycle("абв", times=2))
['а', 'б', 'в', 'а', 'б', 'в']
"""


class Countdown:
    """Обратный отсчёт от start до stop (не включая) с шагом step.

    Класс реализует протокол итератора: __iter__ возвращает сам объект,
    __next__ выдаёт очередное значение или бросает StopIteration.
    """

    def __init__(self, start, stop=0, step=1):
        if step <= 0:
            raise ValueError("шаг должен быть положительным")
        self.current = start
        self.stop = stop
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.stop:
            raise StopIteration
        value = self.current
        self.current -= self.step
        return value


class Cycle:
    """Повторяет элементы последовательности times раз по кругу.

    В отличие от Countdown, __iter__ создаёт новый объект-генератор,
    поэтому один Cycle можно обходить несколько раз.

    >>> c = Cycle([1, 2], times=1)
    >>> list(c), list(c)
    ([1, 2], [1, 2])
    """

    def __init__(self, items, times=1):
        self.items = list(items)
        self.times = times

    def __iter__(self):
        for _ in range(self.times):
            yield from self.items

    def __len__(self):
        return len(self.items) * self.times


if __name__ == "__main__":
    print("Старт через:", end=" ")
    for sec in Countdown(10):
        print(sec, end=" ")
    print("Пуск!")
    print("Чётные вниз от 20:", list(Countdown(20, stop=0, step=2)))
    days = Cycle(["пн", "вт", "ср", "чт", "пт"], times=2)
    print(f"Две рабочие недели ({len(days)} дней):", " ".join(days))
