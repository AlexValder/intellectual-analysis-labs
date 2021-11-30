from typing import List, Tuple
from prettytable import PrettyTable
from numpy import average
from funcs import *
from scipy.stats import f

import numpy as np


DEBUG: bool = False
ACCURACY: int = 4


if __name__ == "__main__":
    xs: Tuple[List[float], List[float], List[float]]
    if DEBUG:
        print("Приклад")
        xs = (
            [
                10.37, 10.37, 10.28, 10.25, 11.72, 11.28, 11.45, 10.40, 11.60, 9.80, 9.81, 8.90, 9.84, 12.70, 12.27, 12.08, 14.90, 15.02,
            ], # x1
            [
                9.87, 11.08, 11.08, 9.08, 10.05, 20.18, 10.69, 13.90, 14.50, 14.70, 10.80, 15.06, 13.27, 16.20, 15.07, 15.20, 17.90, 20.37,
            ], # x2
            [
                8.20, 9.80, 10.10, 5.80, 9.50, 15.70, 11.50, 10.60, 11.40, 10.10, 9.40, 8.10, 10.80, 11.50, 10.20, 11.50, 12.90, 21.40,
            ], # x3
        )
    else:
        print("Варіант 6")
        xs = (
            [
                10.4, 10.1, 12.1, 16.1, 13.0, 7.9, 8.6, 11.1, 12.3, 10.5, 12.1, 11.4, 12.5, 13.4, 14.4, 15.0, 15.6, 15.4,
            ], # x1
            [
                16.7, 10.5, 11.9, 12.8, 12.4, 12.7, 14.4, 13.9, 14.5, 14.7, 14.8, 9.4, 15.9, 16.2, 16.8, 17.5, 17.9, 18.4,
            ], # x2
            [
                13.2, 10.9, 11.6, 10.4, 10.9, 14.2, 12.2, 13.1, 13.9, 12.6, 14.2, 11.9, 13.3, 14.0, 11.9, 14.9, 15.4, 18.2,
            ], # x3
        )

    assert(len(xs[0]) == len(xs[1]) == len(xs[2]))
    K: int = len(xs)
    N: int = len(xs[0])

    table1 = PrettyTable()
    table2 = PrettyTable()
    xst = list()
    for i, x in enumerate(xs):
        sig, av = sigma(x), average(x)
        table1.add_column(f"x*_{i}", x)
        table2.add_column(f"x*_{i}", [round((el - av) / sig, ACCURACY) for el in x])
        xst.append([(el - av) / sig for el in x])

    print()
    print("1. Вхідні дані")
    print(table1)

    print("Х*")
    print(table2)

    print()
    print("2. Кореляційна матриця R")
    R: np.array = calculate_R(xs)
    print(R)

    print()
    print("3. Розрахунки")
    detR = np.linalg.det(R)
    print(f"|R| = {detR}")
    hi_p = -(N - 1 - 1/(6*(3 + 5))) * np.log(detR)
    print(f"χ^2_p = {hi_p}")
    hi_t = get_pirson_quantile(p = 0.95, v = 3)
    print(f"χ^2_t = {hi_t}")

    if hi_p > hi_t:
        print("χ^2_p > χ^2_t, а отже в масиві незалежних змінних має місце загальна мультиколінеарність.")
    else:
        print("χ^2_p <= χ^2_t, а отже в масиві незалежних змінних не має місця загальна мультиколінеарність.")

    print()
    print("4. Обернена до R матриця C:")
    C = np.linalg.inv(R)
    print(C)

    print()
    print("Знайдемо F-критерій для кожної незалежної змінної:")

    F_k = [(C[i][i] - 1) * (N - K) / (K - 1) for i in range(K)]

    print(f"F_k1 = {F_k[0]}")
    print(f"F_k2 = {F_k[1]}")
    print(f"F_k3 = {F_k[2]}")

    print()
    F_t = f.ppf(1 - 0.05, 15, 2)
    print("Розрахункові значення порівнюємо з табличними " +
        "(обсяг вибірки дорівнює 18, кількість незалежних змінних – трьом) при 18-3=15 та " +
        f"3-1=2 ступенях свободи та рівні значущості q=5% F_t = {F_t}")

    for i, f_k in enumerate(F_k):
        if f_k < F_t:
            print(f"F_k{i + 1} < F_t: мультиколінеарність не спостерігається")
        else:
            print(f"F_k{i + 1} >= F_t: спостерігається мультиколінеарність")
