from typing import List, Tuple
from prettytable import PrettyTable

from f_table import get_f


ACCURACY: int = 4


def calculate_cap(xs: List[float], ys: List[float]) -> Tuple[float, float, List[float]]:
    n: float = len(xs) * 1.0
    a1 = (n * sum([x * y for x, y in zip(xs, ys)]) - sum(xs) * sum(ys)) / (n * sum([x ** 2 for x in xs]) - sum(xs) ** 2)
    a0 = (sum(ys) - a1 * sum(xs)) / n
    return a0, a1, [round(a1 * x + a0, ACCURACY) for x in xs]


if __name__ == "__main__":
    # Variant 6
    DEBUG: bool = False
    xs: List[float]
    ys: List[float]
    if DEBUG:
        xs = [1.0, -1.0, 1.0, 1.0, -1.0, 0.0]
        ys = [0.0, -2.0, 1.0, 0.0, -2.0, -1.0]
    else:        
        xs = [2.40, 2.20, 2.60, 2.60, 2.30, 2.20, 2.80, 2.80, 2.80]
        ys = [40.2, 39.4, 43.7, 38.4, 38.8, 39.9, 30.1, 31.7, 37.2]

    K: int = 1
    xys: List[float] = [round(x * y, ACCURACY) for x, y in zip(xs, ys)]
    xs2: List[float] = [round(x * x, ACCURACY) for x in xs]
    ys2: List[float] = [round(y * y, ACCURACY) for y in ys]

    a0, a1, y_cap = calculate_cap(xs, ys)
    y_av: float = sum(ys) / len(ys)

    y_diff_av: List[float] = [round(y - y_av, ACCURACY) for y in y_cap]
    y_diff_av2: List[float] = [round(y * y, ACCURACY) for y in y_diff_av]
    y_diff: List[float] = [round(y_c - y, ACCURACY) for y_c, y in zip(y_cap, ys)]
    y_diff2: List[float] = [round(y * y, ACCURACY) for y in y_diff]

    table = PrettyTable()
    table.add_column("n", [str(i) for i in range (1, len(xs) + 1)] + ["Sum"])
    table.add_column("X_i", xs + [round(sum(xs), ACCURACY)])
    table.add_column("Y_i", ys + [round(sum(ys), ACCURACY)])
    table.add_column("X_i*Y_i", xys + [round(sum(xys), ACCURACY)])
    table.add_column("X_i^2", xs2 + [round(sum(xs2), ACCURACY)])
    table.add_column("Y_i^2", ys2 + [round(sum(ys2), ACCURACY)])
    table.add_column("Y^_i", y_cap + [round(sum(y_cap), ACCURACY)])
    table.add_column("Y^_i - Y_av", y_diff_av + [round(sum(y_diff_av), ACCURACY)])
    table.add_column("(Y^_i - Y_av)^2", y_diff_av2 + [round(sum(y_diff_av2), ACCURACY)])
    table.add_column("Y^_i - Y_i", y_diff + [round(sum(y_diff), ACCURACY)])
    table.add_column("(Y^_i - Y_i)^2", y_diff2 + [round(sum(y_diff2), ACCURACY)])
    
    print(table)

    F: float = (sum(y_diff_av2) / K) / (sum(y_diff2) / (len(xs) - 2))
    table_F: float = get_f(K, len(xs) - 2)
    print(f"F = {F}")
    print(f"Значення за таблицею Фішера: {table_F}")
    if F > table_F:
        print(f"Модель y^_i = {round(a1, ACCURACY)}*x_i + {round(a0, ACCURACY)} адекватна з рівнем значущості 5%.")
    else:
        print(f"Модель y^_i = {round(a1, ACCURACY)}*x_i + {round(a0, ACCURACY)} неадекватна з рівнем значущості 5%.")
