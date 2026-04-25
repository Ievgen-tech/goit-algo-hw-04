# Домашнє завдання 4 | Завдання 2
# Фрактал «Сніжинка Коха» з використанням рекурсії
#
# Запуск:
#   python modul2.py
# Після запуску програма запитає рівень рекурсії (рекомендовано: 1–6)

import turtle


def koch_curve(t: turtle.Turtle, order: int, size: float) -> None:
    """Рекурсивно малює криву Коха.

    Args:
        t: Об'єкт черепашки для малювання.
        order: Рівень рекурсії (0 — пряма лінія).
        size: Довжина сторони поточного відрізка.
    """
    if order == 0:
        # Базовий випадок: малюємо пряму лінію
        t.forward(size)
    else:
        # Рекурсивно малюємо 4 сегменти кривої Коха
        step = size / 3
        koch_curve(t, order - 1, step)
        t.left(60)
        koch_curve(t, order - 1, step)
        t.right(120)
        koch_curve(t, order - 1, step)
        t.left(60)
        koch_curve(t, order - 1, step)


def draw_snowflake(order: int, size: float = 300) -> None:
    """Малює сніжинку Коха — три криві Коха, з'єднані у трикутник.

    Args:
        order: Рівень рекурсії.
        size: Довжина сторони трикутника.
    """
    screen = turtle.Screen()
    screen.title(f"Сніжинка Коха — рівень рекурсії: {order}")
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)          # Максимальна швидкість малювання
    t.color("steelblue")
    t.pensize(1)

    # Початкова позиція — центрування сніжинки на екрані
    t.penup()
    t.goto(-size / 2, size / 3)
    t.pendown()

    # Сніжинка = 3 криві Коха під кутом 120° одна до одної
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    t.hideturtle()
    screen.mainloop()


def main() -> None:
    """Точка входу: зчитує рівень рекурсії від користувача."""
    print("=== Сніжинка Коха ===")
    while True:
        try:
            order = int(input("Введіть рівень рекурсії (рекомендовано 1–6): "))
            if order < 0:
                print("Рівень не може бути від'ємним. Спробуйте ще раз.")
                continue
            break
        except ValueError:
            print("Будь ласка, введіть ціле число.")

    draw_snowflake(order)


if __name__ == "__main__":
    main()
