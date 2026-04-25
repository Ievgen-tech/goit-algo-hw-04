# Домашнє завдання 4 | Завдання 3
# Порівняльний аналіз алгоритмів сортування: злиттям, вставками та Timsort
#
# Запуск:
#   python modul3.py

import timeit
import random


#  Сортування вставками

def insertion_sort(arr: list) -> list:
    """Сортування вставками. Складність: O(n²) в середньому та в найгіршому випадку.

    Args:
        arr: Список для сортування.

    Returns:
        Відсортований список (новий об'єкт).
    """
    arr = arr[:]  # Не змінюємо оригінал
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Зсуваємо елементи, більші за key, на одну позицію вправо
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


#  Сортування злиттям

def merge_sort(arr: list) -> list:
    """Сортування злиттям. Складність: O(n log n) у всіх випадках.

    Args:
        arr: Список для сортування.

    Returns:
        Відсортований список (новий об'єкт).
    """
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)


def _merge(left: list, right: list) -> list:
    """Злиття двох відсортованих списків в один.

    Args:
        left: Лівий відсортований список.
        right: Правий відсортований список.

    Returns:
        Злитий відсортований список.
    """
    result: list = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


#  Timsort (вбудований Python)

def timsort(arr: list) -> list:
    """Timsort — вбудований алгоритм Python. Складність: O(n log n).

    Args:
        arr: Список для сортування.

    Returns:
        Відсортований список (новий об'єкт).
    """
    return sorted(arr)


#  Вимірювання часу

def measure_time(func, data: list, repeats: int = 5) -> float:
    """Вимірює середній час виконання функції сортування.

    Args:
        func: Функція сортування.
        data: Вхідний список.
        repeats: Кількість повторень для усереднення.

    Returns:
        Середній час виконання у секундах.
    """
    timer = timeit.Timer(lambda: func(data))
    total = timer.timeit(number=repeats)
    return total / repeats


#  Головна програма

def main() -> None:
    """Запускає порівняльний аналіз алгоритмів на різних наборах даних."""

    # Розміри наборів даних для тестування
    sizes = [100, 1_000, 5_000, 10_000]

    # Типи вхідних даних
    datasets: dict[str, list] = {}

    algorithms = {
        "Insertion Sort": insertion_sort,
        "Merge Sort    ": merge_sort,
        "Timsort       ": timsort,
    }

    print("=" * 65)
    print("  Порівняльний аналіз алгоритмів сортування")
    print("=" * 65)

    for size in sizes:
        # Генеруємо три типи даних для кожного розміру
        datasets = {
            "Випадковий   ": random.sample(range(size * 10), size),
            "Майже впорядк": list(range(size - size // 10)) + random.sample(range(size), size // 10),
            "Зворотній    ": list(range(size, 0, -1)),
        }

        print(f"\n  Розмір масиву: {size:,} елементів")
        print(f"  {'Алгоритм':<20} {'Випадковий':>14} {'Майже впорядк':>15} {'Зворотній':>12}")
        print("  " + "-" * 63)

        for algo_name, algo_func in algorithms.items():
            # Пропускаємо сортування вставками для великих масивів (занадто повільно)
            if algo_name.strip() == "Insertion Sort" and size > 5_000:
                row = f"  {algo_name:<20}"
                for _ in datasets:
                    row += f"  {'(пропущено)':>12}"
                print(row)
                continue

            row = f"  {algo_name:<20}"
            for data in datasets.values():
                t = measure_time(algo_func, data)
                row += f"  {t:>12.6f}s"
            print(row)

    print("\n" + "=" * 65)
    print("  Висновки:")
    print("  - Timsort стабільно найшвидший на всіх типах даних.")
    print("  - Merge Sort стабільний O(n log n), але повільніший за Timsort")
    print("    через накладні витрати на рекурсію та виділення пам'яті.")
    print("  - Insertion Sort ефективний лише на малих (<100) або")
    print("    майже впорядкованих масивах. На великих масивах — O(n²).")
    print("=" * 65)


if __name__ == "__main__":
    main()
