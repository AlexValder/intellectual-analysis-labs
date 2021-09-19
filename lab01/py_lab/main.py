from typing import List, Dict
from functions import *
from alphas import get_eps, get_normal


# Variant 6

if __name__ == "__main__":
    xs: List[float] = [15.4, 17.6, 12.3, 15.9, 11.0, 12.6, 10.4, 4.9, 2.4, 1.6]
    ys: List[float] = [13.7, 18.0, 16.2, 19.5, 14.1, 14.8, 15.0, 9.0, 5.1, 3.7]

    calculate_1: bool = True
    calculate_2: bool = True
    calculate_3: bool = True
    calculate_4: bool = True

    # 1
    if calculate_1:
        print("1. Дисперсійна таблиця")
        print(dispercy_table(xs, ys))

    for ls, name in [(xs, "X"), (ys, "Y")]:
        print(f"ДЛЯ {name}")
        # 2
        if calculate_2:
            print()
            print("Математичне очікування:")
            print(sum(ls) / len(ls))
            print("Зміщена та незміщена оцінки дисперсії:")
            print(sigma_line_dispercy(ls))
            print(sigma_corner_dispercy(ls))
            print("Зміщена на незміщена оцінки середньоквадратичного відхилення:")
            print(sigma_line(ls))
            print(sigma_corner(ls))

        # 3
        if calculate_3:
            print()
            sigma: float = 1.0
            alpha: float = 0.95
            print(f"3. Довірчий інтервал при σ={sigma} з довірчою ймовірністю {alpha * 100}%")
            first, second = get_normal((alpha + 1) / 2)
            eps3: float = first / 10 + second / 1000
            left3, right3 = trust_interval_known(ls, sigma, eps3)
            print(f"({round(left3, 5)}, {round(right3, 5)})")
        
        # 4
        if calculate_4:
            print()
            q: float = 0.05
            eps4: float = get_eps(k = 10, q = q)
            print(f"4. Довірчий інтервал з довірчою ймовірністю {(1 - q) * 100}%")
            left4, right4 = trust_interval_unknown(ls, eps4)
            print(f"({round(left4, 5)}, {round(right4, 5)})")
