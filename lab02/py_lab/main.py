from typing import List, Tuple
from math import sqrt, fsum
from prettytable import PrettyTable
from table import get_student

# Variant 6
if __name__ == "__main__":
    #xs: List[float] = [2.7, 3.0, 2.8, 2.9, 2.6, 2.5, 2.8, 2.6, 2.5]
    xs: List[float] = [2.40, 2.20, 2.60, 2.60, 2.30, 2.20, 2.80, 2.80, 2.80]
    #ys: List[float] = [15.6, 15.3, 15.6, 15.2, 15.9, 16.1, 15.5, 16.0, 16.2]
    ys: List[float] = [40.2, 39.4, 43.7, 38.4, 38.8, 39.9, 30.1, 31.7, 37.2]
    xys: List[float] = [x * y for (x, y) in zip(xs, ys)]
    xs2: List[float] = [x * x for x in xs]
    ys2: List[float] = [y * y for y in ys]

    lists: List[Tuple[str, List[float]]] = [
        ("X_i", xs),
        ("Y_i", ys),
        ("X_i*Y_i", [round(t, 5) for t in xys]),
        ("X_i^2", [round(t, 5) for t in xs2]),
        ("Y_i^2", [round(t, 5) for t in ys2]),
    ]

    N: int = len(xs)

    do_first: bool = True
    do_second: bool = True
    do_third: bool = True
    do_forth: bool = True

    if do_first:
        print()
        print("1. Кореляційна таблиця.")
        table = PrettyTable()
        table.add_column("n", [f"{i}" for i in range(1, N + 1)] + ["sum"])
        for name, ls in lists:
            table.add_column(name, ls + [round(sum(ls), 5)])
        print(table)

    
    r: float = (N * fsum(xys) - fsum(xs) * fsum(ys)) / sqrt((N * fsum(xs2) - fsum(xs) ** 2) * (N * fsum(ys2) - fsum(ys) ** 2))
    if do_second:
        print()
        print(f"2. Оцінка коефієнту кореляції r = {r}")

    if do_third:
        print()
        if r < -1 or r > 1:
            print("ERROR! r is wrong!")
            exit(-1)
        
        if r >= 0:
            if 1 - r > r:
                print("3. Ближче до 1, скоріше за все - прямий лінійний стохастичний зв'язок.")
            else:
                print("3. Ближче до 0, зв'язок скоріш за все відсутній.")
        else:
            if r < 1 + r:
                print("3. Ближче до -1, скоріше за все - зворотній лінійний стохастичний зв'язок.")
            else:
                print("3. Бличже до 0, зв'язок скоріш за все відсутній.")

    t: float = r * sqrt(N - 2) / sqrt(1 - r ** 2)
    if do_forth:
        print()
        print(f"4. Статична значущість коефіцієнта кореляції t = {t}")

        t_from_table: float = get_student(k = N - 2, q = 0.05)
        abs_t = abs(t)
        if abs_t > t_from_table:
            print(f"|{round(t, 3)}| > {t_from_table}")
            print("Коефіцієнт кореляції значно відрізняється від нуля і між факторами існує лінійний зв'язок.")
        else:
            print(f"|{round(t, 3)}| < {t_from_table}")
            print("Коефіцієнт кореляції незначно відрізняється від нуля, тому лінійного зв'язку між параметрами моделі не існує.")