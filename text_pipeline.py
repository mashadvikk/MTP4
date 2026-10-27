"""Повышенная 9. Pipeline обработки текста.

Текст проходит цепочку шагов: разбиение на слова, приведение к нижнему
регистру, удаление знаков препинания, отбрасывание служебных слов и
подсчёт частот. Шаги — обычные функции, цепочку собирает make_pipeline().

>>> make_pipeline(str.split, words_lower, strip_punct)("Да, ДА! нет.")
['да', 'да', 'нет']
>>> top_words("кот и пёс, кот и мышь; КОТ!", 2)
[('кот', 3), ('мышь', 1)]
"""
from functools import reduce

STOP_WORDS = {"и", "в", "на", "с", "по", "а", "но", "не", "что", "как",
              "это", "для", "из", "к", "о", "у", "же", "то"}
PUNCT = ".,;:!?«»()—-\"'"

TEXT = """
Функциональное программирование — это стиль, в котором программа
строится из функций. Функции принимают данные и возвращают новые
данные, не меняя старые. Функции высшего порядка принимают другие
функции как аргументы: map применяет функцию к каждому элементу,
filter отбирает элементы, а reduce сворачивает данные в одно значение.
"""


def make_pipeline(*steps):
    """Композиция шагов слева направо через reduce."""
    return lambda data: reduce(lambda acc, step: step(acc), steps, data)


def words_lower(words):
    return list(map(str.lower, words))


def strip_punct(words):
    return [w for w in map(lambda w: w.strip(PUNCT), words) if w]


def drop_stop_words(words):
    return list(filter(lambda w: w not in STOP_WORDS, words))


def count_words(words):
    """Частоты слов свёрткой в словарь.

    >>> count_words(["а", "б", "а"])
    {'а': 2, 'б': 1}
    """
    return reduce(lambda acc, w: {**acc, w: acc.get(w, 0) + 1}, words, {})


def sort_by_count(freq):
    return sorted(freq.items(), key=lambda kv: (-kv[1], kv[0]))


def top_words(text, n=5):
    """Готовый конвейер: n самых частых значимых слов текста."""
    run = make_pipeline(str.split, words_lower, strip_punct,
                        drop_stop_words, count_words, sort_by_count)
    return run(text)[:n]


if __name__ == "__main__":
    print("Текст:", " ".join(TEXT.split())[:70] + "...")
    words = make_pipeline(str.split, words_lower, strip_punct)(TEXT)
    print("Всего слов:", len(words))
    print("Без служебных:", len(drop_stop_words(words)))
    print("Пять самых частых:")
    for word, count in top_words(TEXT, 5):
        print(f"  {word:<10} {count}")
    long_words = make_pipeline(
        str.split, strip_punct,
        lambda ws: filter(lambda w: len(w) > 10, ws), sorted)(TEXT)
    print("Длинные слова:", ", ".join(long_words))
