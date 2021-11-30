import statistics as stats
import numpy as np

from typing import List
from math import sqrt, log
from numpy import average


def sigma(xs: List[float]) -> float:
    av = average(xs)
    return sqrt(sum((x - av)** 2 for x in xs) / (len(xs) - 1))


def dispersion(arr: List[float], mean: float, n: int) -> float:
    return sum([(x - mean)**2 for x in arr]) / (n - 1)


def calculate_R(xs: List[List[float]]) -> np.array:
    def _normal(xx: np.array) -> np.array:
        n1: int = len(xx)
        n2: int = len(xx[0])
        means: List[float] = [stats.mean(x) for x in xs]
        disps: List[float] = [dispersion(x, m, n2) for x, m in zip(xx, means)]
        return np.array(
            [[(xx[i][j] - means[j]) / (sqrt(n1) * disps[j]) for j in range(n2)] for i in range(n1)]
        )


    X_tr = np.array(xs)
    X = X_tr.transpose()
    X_n = _normal(X)
    X_n_tr = X_n.transpose()
    raw_R = X_n_tr.dot(X_n)
    return np.array(
            [[1 if i == j else 1 - raw_R[i][j] for j in range(len(raw_R[i]))] for i in range(len(raw_R))]
        )


def fi(x: float) -> float:
    c0 = 2.515517
    c1 = 0.802853
    c2 = 0.010328
    d1 = 1.432788
    d2 = 0.1892659
    d3 = 0.001308

    t = sqrt(-2 * log(x))

    numerator = c0 + c1 * t + c2 * t * t
    denomerator = 1 + d1 * t + d2 * t * t + d3 * t * t * t

    return t - numerator / denomerator


def get_normal_quantile(p: float) -> float:
    return fi(1 - p) if p > 0.5 else -fi(p)


def get_pirson_quantile(p: float, v: float) -> float:
    normal_quantile = get_normal_quantile(p)

    t = 2 / (9 * v)
    return v * (1 - t + normal_quantile * sqrt(t))**3 + 0.03