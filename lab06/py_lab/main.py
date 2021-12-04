import numpy as np

from typing import List
from prettytable import PrettyTable
from d_table import d_1, d_2
from e_table import e


DEBUG: bool = False
ACCURACY: int = 2


def count_series(_input: List) -> int:
    if len(_input) < 2:
        return 1

    count = 1
    for i in range(len(_input) - 1):
        if _input[i] != _input[i + 1]:
            count += 1
    return count


if __name__ == "__main__":
    years: List[int]
    xs: List[float]
    ys: List[float]

    if DEBUG:
        years = list(np.array([[x]*4 for x in range(1990, 1996)]).flat)
        xs = [i for i in range(1, 25)]
        ys = [
            40.69, 68.76, 91.76, 45.03, 67.69, 115.9, 152.7, 73.84,
            110.4, 184.2, 240.1, 114.2, 168.8, 279.8, 359.6, 171.0,
            248.7, 405.3, 514.9, 240.6, 347.9, 562.0, 708.2, 327.3,
        ]
    else:
        print("VARIANT 6")
        years = [i for i in range(1993, 2017)]
        xs = [i for i in range (1, 25)]
        ys = [
            255.0, 162.0, 271.0, 283.0, 294.0, 310.0, 367.0, 380.0,
            259.0, 235.0, 240.0, 235.0, 215.0, 220.0, 236.0, 293.0,
            306.0, 317.0, 293.0, 298.0, 293.0, 273.0, 278.0, 185.0,
        ]
    
    assert(len(years) == len(xs) == len(ys))
    
    a1, a0 = np.polyfit(xs, ys, 1)
    ys_cap: List[float] = [a1 * x + a0 for x in xs]
    es: List[float] = [y_cap - y for y_cap, y in zip(ys_cap, ys)]
    signs: List[str] = ['-' if e < 0 else '+' for e in es]
    
    print("Вихідні дані:")

    print(f"Роки: {set(years)}")
    print(f"X: {xs}")
    print(f"Y: {ys}")
    print(f"Залишки регресійної моделі: y = {round(a0, ACCURACY)} {'+' if a1 >= 0 else '-'} {round(abs(a1), ACCURACY)} * x_i")

    table1 = PrettyTable()
    table1.add_column('Рік', years)
    table1.add_column('X', [round(x, ACCURACY) for x in xs])
    table1.add_column('Y', [round(y, ACCURACY) for y in ys])
    table1.add_column('Y^', [round(y, ACCURACY) for y in ys_cap])
    table1.add_column('Залишки e_i', [round(e, ACCURACY) for e in es])
    table1.add_column('Знаки залишків', signs)
    print(table1)

    print("\n=== Перевірка на автокореляцію за критерієм знаків ===\n")

    print("Підрахуеємо кількість додатніх знаків, кількість від'ємних знаків та кількість серій знаків.")
    pos_num: int = sum(1 if s == '+' else 0 for s in signs)
    neg_num: int = sum(1 if s == '-' else 0 for s in signs)
    ser_num: int = count_series(signs)
    print(f"Кількість додатніх знаків: n1 = {pos_num}")
    print(f"Кількість від'єсних знаків: n2 = {neg_num}")
    print(f"Кількість \"серій\": nu = {ser_num}")

    upper_n: int = d_1(n1=pos_num, n2=neg_num)
    lower_n: int = d_2(n1=pos_num, n2=neg_num)
    print(f"Верхня границя nu = {upper_n}, а нижня - {lower_n}")
    if lower_n <= ser_num <= upper_n:
        print("За критерієм знаків, автокореляція ВІДСУТНЯ.")
    else:
        print("За критерієм знаків, автокореляція НАЯВНА.")
    
    print("\n=== Перевірка на автокореляцію за критерієм Дарбіна-Уотсона ===\n")

    table2 = PrettyTable()
    table2.add_column('Рік', years + ['сума'])
    table2.add_column('X_i', xs + [''])
    table2.add_column('Y_i', [round(y, ACCURACY) for y in ys] + [round(sum(ys), ACCURACY)])
    table2.add_column('Y^_i', [round(y, ACCURACY) for y in ys_cap] + [round(sum(ys_cap), ACCURACY)])
    table2.add_column('e_i', [round(e, ACCURACY) for e in es] + [round(sum(es), ACCURACY)])
    table2.add_column('e^2_i', [round(e ** 2, ACCURACY) for e in es] + [round(sum(e ** 2 for e in es), ACCURACY)])
    table2.add_column('e_{i-1}', [''] + [round(e, ACCURACY) for e in es[:-1]] + [round(sum(es[:-1]), ACCURACY)])
    table2.add_column('e_{i-1} - e_i', [''] + [round(es[i] - es[i - 1], ACCURACY) for i in range(1, len(es))] + [round(sum(es[i] - es[i - 1] for i in range(1, len(es))), ACCURACY)])
    table2.add_column('(e_{i-1} - e_i)^2', [''] + [round((es[i] - es[i - 1])**2, ACCURACY) for i in range(1, len(es))] + [round(sum((es[i] - es[i - 1])**2 for i in range(1, len(es))), ACCURACY)])
    print(table2)

    print("Розрахуємо d-статистику на основі табличних даних:")
    d: float = sum((es[i] - es[i - 1]) ** 2 for i in range(1, len(es))) / sum(e ** 2 for e in es)
    print(f'd = {d}')

    print(f"Користуючись статистичними таблицями Дарбіна–Уотсона для n={len(xs)} (обсяг вибірки), " +
        "k=1 (кількість незалежних змінних) та заданим рівнем значущості –5%, знаходимо значення ")

    dl, du = e(k=1, n=24)
    
    if d < dl:
        print(f"d < {dl}, а значить автокореляція НАЯВНА з неймовірністю 5%.")
    elif dl < d < du:
        print(f"{dl} < d < {du}, а значить НЕВІДОМО.")
    elif du < d < 4 - du:
        print(f"{du} < d < {4 - du}, а значить автокореляція ВІДСУТНЯ.")
    elif 4 - du < d < 4 - dl:
        print(f"{4 - du} < d < {4 - dl}, а значить НЕВІДОМО.")
    else:
        print(f"{4 - dl} < d < 4, а значить автокореляція НАЯВНА з неймовірністю 5%.")
