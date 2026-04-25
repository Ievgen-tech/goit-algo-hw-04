# Домашнє завдання 4 | Завдання 1
# Рекурсивне копіювання та сортування файлів за розширенням
#
# Запуск:
#   python modul1.py <вихідна_директорія> [директорія_призначення]
#
# Приклади:
#   python modul1.py ./my_folder            # збереже у ./dist
#   python modul1.py ./my_folder ./sorted   # збереже у ./sorted

import argparse
import shutil
from pathlib import Path


def parse_args() -> argparse.Namespace:
    """Парсить аргументи командного рядка."""
    parser = argparse.ArgumentParser(
        description="Рекурсивно копіює файли з вихідної директорії "
                    "до директорії призначення, сортуючи їх за розширенням."
    )
    # Обов'язковий аргумент — шлях до вихідної директорії
    parser.add_argument("source", type=Path, help="Шлях до вихідної директорії")
    # Необов'язковий аргумент — шлях до директорії призначення (за замовчуванням dist)
    parser.add_argument(
        "destination",
        type=Path,
        nargs="?",
        default=Path("dist"),
        help="Шлях до директорії призначення (за замовчуванням: dist)",
    )
    return parser.parse_args()


def copy_files(source: Path, destination: Path) -> None:
    """Рекурсивно обходить source та копіює файли до destination/розширення/.

    Args:
        source: Директорія, яку потрібно обійти.
        destination: Коренева директорія призначення.
    """
    try:
        for item in source.iterdir():
            if item.is_dir():
                # Рекурсивний виклик для кожної піддиректорії
                copy_files(item, destination)
            elif item.is_file():
                # Визначаємо розширення; файли без розширення → папка "no_extension"
                ext: str = item.suffix.lstrip(".").lower() or "no_extension"
                target_dir: Path = destination / ext
                try:
                    target_dir.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(item, target_dir / item.name)
                except PermissionError as e:
                    print(f"Немає доступу до файлу '{item}': {e}")
                except OSError as e:
                    print(f"Помилка копіювання '{item}': {e}")
    except PermissionError as e:
        print(f"Немає доступу до директорії '{source}': {e}")
    except OSError as e:
        print(f"Помилка читання директорії '{source}': {e}")


def main() -> None:
    """Точка входу: перевіряє аргументи та запускає копіювання."""
    args = parse_args()
    source: Path = args.source
    destination: Path = args.destination

    # Перевірка існування вихідної директорії
    if not source.exists():
        print(f"Помилка: директорія '{source}' не існує.")
        return

    if not source.is_dir():
        print(f"Помилка: '{source}' не є директорією.")
        return

    # Створюємо директорію призначення, якщо вона ще не існує
    destination.mkdir(parents=True, exist_ok=True)

    copy_files(source, destination)
    print(f"Готово. Файли скопійовано з '{source}' до '{destination}' та відсортовано за розширенням.")


if __name__ == "__main__":
    main()

