from typing import List, Tuple
from numpy.lib.function_base import average, sqrt
from prettytable import PrettyTable


# σ_x^2 with a line over it
def sigma_line_dispercy(ls: List[float]) -> float:
    av = average(ls)
    N = len(ls)
    # from formulas
    return sum((x - av) ** 2 for x in ls) / len(ls)
    # from example
    # return sum(x ** 2 for x in ls) / N - sum(ls) ** 2 / N ** 2

# σ_x^2 with ^ over it
def sigma_corner_dispercy(ls: List[float]) -> float:
    av = average(ls)
    N = len(ls)
    # from formulas
    return sum((x - av) ** 2 for x in ls) / (len(ls) - 1) # from formulas
    # from example
    # return sum(x ** 2 for x in ls) / (N - 1) - sum(ls) ** 2 / (N * (N - 1))


# σ_x with ^ over it
def sigma_corner(ls: List[float]) -> float:
    return sqrt(sigma_corner_dispercy(ls))

# σ_x with a line over it
def sigma_line(ls: List[float]) -> float:
    return sqrt(sigma_line_dispercy(ls))


def trust_interval_known(ls: List[float], sigma: float, eps: float) -> Tuple[float, float]:
    av: float = average(ls)
    N: int = len(ls)
    tmp: float = eps * sigma / sqrt(N)

    return (av - tmp, av + tmp)


def trust_interval_unknown(ls: List[float], eps: float) -> Tuple[float, float]:
    av: float = average(ls)
    N: int = len(ls)
    tmp: float = eps * sigma_line(ls) / sqrt(N - 1)

    return (av - tmp, av + tmp)


def dispercy_table(xs, ys) -> PrettyTable:
    xs2: List[float] = [x ** 2 for x in xs]
    ys2: List[float] = [y ** 2 for y in ys]

    lists: List[List[float]] = [xs, ys, xs2, ys2]

    N: int = len(xs)

    table: PrettyTable = PrettyTable()
    table.add_column("i", [str(i + 1) for i in range(N)])
    table.add_column("x_i", [str(x) for x in xs])
    table.add_column("y_i", [str(y) for y in ys])
    table.add_column("x_i^2", [str(round(x ** 2, 5)) for x in xs])
    table.add_column("y_i^2", [str(round(y ** 2, 5)) for y in ys])
    
    table.add_row(["Sum"] + [str(round(sum(ls), 5)) for ls in lists])
    table.add_row(["Average"] + [str(round(average(ls), 5)) for ls in lists])

    return table
