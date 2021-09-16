from typing import List
from numpy import linalg
from numpy.lib.function_base import average
from prettytable import PrettyTable


# Variant 6

if __name__ == "__main__":
    xs: List[float] = [15.4, 17.6, 12.3, 15.9, 11.0, 12.6, 10.4, 4.9, 2.4, 1.6]
    ys: List[float] = [13.7, 18.0, 16.2, 19.5, 14.1, 14.8, 15.0, 9.0, 5.1, 3.7]

    xs2: List[float] = [x ** 2 for x in xs]
    ys2: List[float] = [y ** 2 for y in ys]

    lists: List[List[float]] = [xs, ys, xs2, ys2]

    assert(len(xs) == len(ys) == len(xs2) == len(ys2))
    N: int = len(xs)

    table: PrettyTable = PrettyTable()
    table.add_column("i", [str(i + 1) for i in range(N)])
    table.add_column("x_i", [str(x) for x in xs])
    table.add_column("y_i", [str(y) for y in ys])
    table.add_column("x_i^2", [str(round(x ** 2, 5)) for x in xs])
    table.add_column("y_i^2", [str(round(y ** 2, 5)) for y in ys])
    
    table.add_row(["Sum"] + [str(round(sum(ls), 5)) for ls in lists])
    table.add_row(["Average"] + [str(round(average(ls), 5)) for ls in lists])

    print(table)