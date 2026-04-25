# goit-algo-hw-04

## Завдання 1 — Рекурсивне копіювання та сортування файлів за розширенням

Скрипт `modul1.py` рекурсивно обходить вихідну директорію, копіює всі файли до директорії призначення та розподіляє їх по піддиректоріях за розширенням (`.txt`, `.jpg`, `.py` тощо).

---

## Вимоги

- Python 3.6 або новіший

---

## Швидкий старт (для перевірки)

Скопіюйте і вставте один рядок у термінал — він створить тестові файли, запустить скрипт і покаже результат:

```bash
mkdir test_folder\subdir; echo text > test_folder\a.txt; echo x > test_folder\b.jpg; echo x > test_folder\subdir\c.csv; python modul1.py test_folder; tree dist /F
```

---

## Запуск

### Синтаксис

```bash
python modul1.py <вихідна_директорія> [директорія_призначення]
```

- `<вихідна_директорія>` — обов'язковий аргумент, шлях до папки з файлами
- `[директорія_призначення]` — необов'язковий, за замовчуванням створюється папка `dist`

---

## Покрокова інструкція для перевірки

### Крок 1 — Клонувати або завантажити репозиторій

```bash
git clone https://github.com/Ievgen-tech/goit-algo-hw-04.git
cd goit-algo-hw-04
```

### Крок 2 — Створити тестову папку з файлами

```bash
mkdir test_folder
mkdir test_folder\subdir
echo "hello world" > test_folder\file1.txt
echo "some text" > test_folder\notes.txt
echo "print('hi')" > test_folder\script.py
echo "" > test_folder\image.jpg
echo "data" > test_folder\subdir\nested.csv
```

### Крок 3 — Запустити скрипт

> Переконайтесь, що Крок 2 виконано — папка `test_folder` має існувати до запуску.

**Варіант А** — destination за замовчуванням (`dist`):

```bash
python modul1.py test_folder
```

**Варіант Б** — вказати власну папку призначення:

```bash
python modul1.py test_folder my_output
```

### Крок 4 — Перевірити результат

```bash
tree dist /F
```

Очікувана структура:

```text
dist/
├── txt/
│   ├── file1.txt
│   └── notes.txt
├── py/
│   └── script.py
├── jpg/
│   └── image.jpg
└── csv/
    └── nested.csv
```

---

## Обробка помилок

- Якщо вихідна директорія не існує — скрипт виведе повідомлення про помилку і завершить роботу
- Якщо немає доступу до файлу або директорії — скрипт виведе попередження і продовжить роботу з іншими файлами
