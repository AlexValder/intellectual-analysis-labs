from typing import List
from numpy.lib.function_base import average
from numpy.linalg.linalg import inv
from prettytable import PrettyTable
from math import sqrt
from f_table import get_f
from table import get_student
import numpy as np


DEBUG: bool = False
ACCURACY: int = 2


if __name__ == "__main__":
    ys: List[float]
    xs1: List[float]
    xs2: List[float]
    if DEBUG:
        ys = [10.0, 12.0, 17.0, 13.0, 15.0, 10.0, 14.0, 12.0, 16.0, 18.0]
        xs1 = [2.0, 2.0, 8.0, 2.0, 6.0, 3.0, 5.0, 3.0, 9.0, 10.0]
        xs2 = [1.0, 2.0, 10.0, 4.0, 8.0, 4.0, 7.0, 3.0, 10.0, 11.0]
    else:
        print("Variant 6")
        ys = [17.30, 26.70, 31.50, 4.90, 42.00, 18.00, 38.00, 6.00, 53.00, 65.00]
        xs1 = [3.20, 5.30, 6.70, 2.20, 8.80, 4.30, 6.90, 2.10, 8.90, 10.10]
        xs2 = [5.80, 6.90, 8.10, 3.20, 9.60, 5.60, 9.30, 3.50, 12.00, 15.00]
    
    R = np.array([
        [1 for i in range(len(xs1))],
        xs1,
        xs2
    ])
    R1 = R.transpose()
    RR1 = R.dot(R1)
    invRR1 = np.linalg.inv(RR1)
    detRR1 = np.linalg.det(RR1)
    Y = np.array(ys)
    RY = R.dot(Y)
    a_up = invRR1.dot(RY)
    y_av = average(ys)
    y_cap = [round(a_up[0] + a_up[1] * x1 + a_up[2] * x2, ACCURACY) for x1, x2 in zip(xs1, xs2)]

    row5 = [round(y1 - y2, ACCURACY) for y1, y2 in zip(y_cap, ys)]
    row6 = [round(y * y, ACCURACY) for y in row5]
    row7 = [round(y_av - y, ACCURACY) for y in y_cap]
    row8 = [round(y * y, ACCURACY) for y in row7]
    row9 = [round(y - y_av, ACCURACY) for y in y_cap]
    row10 = [round(y * y, ACCURACY) for y in row9]

    # 1
    print("1. Вхідні дані:")

    table = PrettyTable()
    table.add_column("Y", ys)
    table.add_column("X1", xs1)
    table.add_column("X2", xs2)
    print(table)
    print()

    # 2
    print("2. Кореляційна таблиця")

    table = PrettyTable()
    table.add_column('n', [str(i) for i in range(1, 11)] + ['Sum', 'Average'])
    table.add_column('y_i', [str(y) for y in ys] + [sum(ys), average(ys)])
    table.add_column('x_1', [str(x) for x in xs1] + [sum(xs1), ''])
    table.add_column('x_2', [str(x) for x in xs2] + [sum(xs2), ''])
    table.add_column('y^_i', [str(y) for y in y_cap] + [sum(y_cap), ''])
    table.add_column('y^_i - y_i', [str(y) for y in row5] + [round(sum(row5), ACCURACY), ''])
    table.add_column('(y^_i - y_i)^2', [str(y) for y in row6] + [round(sum(row6), ACCURACY), ''])
    table.add_column('y_av_i - y^_i', [str(y) for y in row7] + [round(sum(row7), ACCURACY), ''])
    table.add_column('(y_av_i - y^_i)^2', [str(y) for y in row8] + [round(sum(row8), ACCURACY), ''])
    table.add_column('y^_i - y_av', [str(y) for y in row9] + [round(sum(row9), ACCURACY), ''])
    table.add_column('(y^_i - y_av)^2', [str(y) for y in row10] + [round(sum(row10), ACCURACY), ''])
    
    print(table)
    print()
    R2 = 1 - (sum(row6) / sum(row8))
    print(f"R^2 = {R2}")
    if 1 - R2 > R2:
        print("Коефіцієнт детермінації наближається до 1, тому робимо висновок, що варіація залежної " +
        "змінної значною мірою залежить від варіації незалежних змінних")
    else:
        print("Коефіцієнт детермінації наближається до 0, тому робимо висновок, що варіація залежної " +
        "змінної значною мірою не залежить від варіації незалежних змінних")

    print(f"Надкреслене R2 = 1 - (1 - {R2}^2) * ({len(ys)} - 1) / ({len(ys)} - 2 - 1) = {1 - (1-R2**2) * (len(ys) - 1)/(len(ys) - 3)}")

    print("Вибірковий коефіцієнт множинної кореляції:")
    R = sqrt(R2)
    print(f"R = sqrt({R2}) = {R}")

    if 1 - R > R:
        print("Значення коефіцієнта кореляції наближається до 1, тому можна припустити," +
        "що існує суттєвий зв'язок між всіма незалежними факторами і залежною змінною.")
    else:
        print("Значення коефіцієнта кореляції наближається до 0, тому можна припустити," +
        "що не існує суттєвого зв'язку між всіма незалежними факторами і залежною змінною.")

    # 3
    print()
    print("3. Перевіримо модель на адекватність за F–статистикою:")
    F_p = (sum(row8) / 2) / (sum(row6) / (len(ys) - 2))
    print(f"F_p = ({sum(row8)} / 2)/({sum(row6)}/({len(ys)} - 2)) = {F_p}")
    F_t = get_f(2, 7)
    print(f"Розрахункове значення порівняємо з табличним при 2–х і 7–миступенях свободи і рівнем значущості q = 5%; F_t = {F_t}")

    if F_p > F_t:
        print(f"F_p > F_t, тобто можна сказати, що дана модель з довірчою ймовірностю 95% є адекватною.")
    else:
        print(f"F_p <= F_t, тобто можна сказати, що дана модель з довірчою ймовірностю 95% не є адекватною.")

    # 4
    print()
    print("4. За критерієм Стьюдента визначимо значущість коефіцієнта кореляції:")
    t_p = R * sqrt(len(ys) - 2 - 1) / sqrt(1 - R2)
    t_t = get_student(7, 0.05)
    print(f"t_p = {t_p}")
    print(f"t_t(5%, 7) = {t_t}")

    if abs(t_p) > t_t:
        print("Т.я. |t_p| > t_t, робимо висновок щодо значущості коефіцієнта кореляції з ймовірністю 95%.")
    else:
        print("Т.я. |t_p| <= t_t, робимо висновок щодо не значущості коефіцієнта кореляції з ймовірністю 95%.")

    # 5
    print()
    print("5. Перевіримо значущість окремих коефіцієнтів регресії:")

    t_xp = [a_up[i] / sqrt(R * invRR1[i][i]) for i in range(3)]
    for i, t in enumerate(t_xp):
        print(f"t_{i}p = {t}")
    
    print("Розрахункові значення порівняємо з табличним з рівнем значущості 5% та 7-ма ступенями свободи")
    for i, t in enumerate(t_xp):
        if abs(t) > t_t:
            print(f"Оскільки |t_{i}p| > t_t, то оцінка a_{i} є значущою.")
        else:
            print(f"Оскільки |t_{i}p| <= t_t, то оцінка a_{i} не є значущою.")
    
    deltaR = [(1 - R2) * t*t / (len(ys) - 2 - 1) for t in t_xp]
    for i, r in enumerate(deltaR):
        print(f"ΔR^2_{i} = {r}")
    
    print("На залежну змінну найбільше впливає фактор, який має найбільше значення ΔR^2_j.")
    print(f"В данному випадку це ΔR^2_{deltaR.index(max(deltaR))} = {max(deltaR)}")
