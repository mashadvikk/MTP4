"""Главное меню: запуск любого задания лабораторной №4 (вариант 4)."""
import subprocess
import sys

TASKS = {
    "1": ("Средняя 4. Факториал через reduce", "factorial.py"),
    "2": ("Средняя 6. Генератор простых чисел", "primes.py"),
    "3": ("Средняя 10. Несколько функций к списку через map", "apply_all.py"),
    "4": ("Повышенная 5. Собственный класс-итератор", "countdown.py"),
    "5": ("Повышенная 9. Pipeline обработки текста", "text_pipeline.py"),
}


def main():
    while True:
        print("\nЛабораторная №4, вариант 4. Задания:")
        for key, (title, _) in TASKS.items():
            print(f"  {key}. {title}")
        print("  0. Выход")
        choice = input("Номер задания: ").strip()
        if choice == "0":
            print("Пока!")
            return
        task = TASKS.get(choice)
        if task is None:
            print("Нет такого пункта, попробуйте ещё раз.")
            continue
        title, script = task
        print(f"--- {title} ---")
        subprocess.run([sys.executable, script], check=False)


if __name__ == "__main__":
    main()
