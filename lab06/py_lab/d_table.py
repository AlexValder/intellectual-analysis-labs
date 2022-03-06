from typing import List

def d_1(n1: int, n2: int) -> int:
    if n1 < 2 or n1 > 20:
        raise RuntimeError("n1 should be [2, 20]")
    if n2 < 2 or n2 > 20:
        raise RuntimeError("n2 should be [2, 20]")
    
    return __table1[n1 - 2][n2 - 2]


def d_2(n1: int, n2: int) -> int:
    if n1 < 2 or n1 > 20:
        raise RuntimeError("n1 should be [2, 20]")
    if n2 < 2 or n2 > 20:
        raise RuntimeError("n2 should be [2, 20]")
    
    return __table2[n1 - 2][n2 - 2]


__table1: List[List[int]] = [
    # 2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  2,  2,  2,  2,  2,  2,  2,  2,  2,], # 2
    [ 0,  0,  0,  0,  2,  2,  2,  2,  2,  2,  2,  2,  2,  3,  3,  3,  3,  3,  3,], # 3
    [ 0,  0,  0,  2,  2,  2,  3,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,], # 4
    [ 0,  0,  2,  2,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  4,  4,  5,  5,  5,], # 5
    [ 0,  2,  2,  3,  3,  3,  3,  4,  4,  4,  4,  5,  5,  5,  5,  5,  6,  6,  6,], # 6
    [ 0,  2,  2,  3,  3,  3,  4,  4,  5,  5,  5,  5,  5,  6,  6,  6,  6,  6,  6,], # 7
    [ 0,  2,  3,  3,  3,  4,  4,  5,  5,  5,  6,  6,  6,  6,  6,  7,  7,  7,  7,], # 8
    [ 0,  2,  3,  3,  4,  4,  5,  5,  5,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,], # 9
    [ 0,  2,  3,  3,  4,  5,  5,  5,  6,  6,  7,  7,  7,  7,  8,  8,  8,  8,  9,], # 10
    [ 0,  2,  3,  4,  4,  5,  5,  6,  6,  7,  7,  7,  8,  8,  8,  9,  9,  9,  9,], # 11
    [ 2,  2,  3,  4,  4,  5,  6,  6,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10, 10,], # 12
    [ 2,  2,  3,  4,  5,  5,  6,  6,  7,  7,  8,  8,  9,  9,  9, 10, 10, 10, 10,], # 13
    [ 2,  2,  3,  4,  5,  5,  6,  7,  7,  8,  8,  9,  9,  9, 10, 10, 10, 11, 11,], # 14
    [ 2,  2,  3,  4,  5,  6,  6,  7,  7,  8,  8,  9,  9, 10, 10, 11, 11, 11, 12,], # 15
    [ 2,  2,  4,  4,  5,  6,  6,  7,  8,  8,  9,  9, 10, 10, 11, 11, 11, 12, 12,], # 16
    [ 2,  2,  4,  4,  5,  6,  7,  7,  8,  9,  9, 10, 10, 11, 11, 11, 12, 12, 13,], # 17
    [ 2,  2,  4,  5,  5,  6,  7,  8,  8,  9,  9, 10, 10, 11, 11, 12, 12, 13, 13,], # 18
    [ 2,  2,  4,  5,  6,  6,  7,  8,  8,  9, 10, 10, 11, 11, 12, 12, 13, 13, 13,], # 19
    [ 2,  2,  4,  5,  6,  6,  7,  8,  9,  9, 10, 10, 11, 12, 12, 13, 13, 13, 14,], # 20
]

__table2: List[List[int]] = [
    # 2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,], # 2
    [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,], # 3
    [ 0,  0,  0,  9,  9,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,], # 4
    [ 0,  0,  9, 10, 10, 11, 11,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,], # 5
    [ 0,  0,  9, 10, 11, 12, 12, 13, 13, 13, 13,  0,  0,  0,  0,  0,  0,  0,  0,], # 6
    [ 0,  0,  0, 11, 12, 13, 13, 14, 14, 14, 14, 15, 15, 15,  0,  0,  0,  0,  0,], # 7
    [ 0,  0,  0, 11, 12, 13, 14, 14, 15, 15, 16, 16, 16, 16, 17, 17, 17, 17, 17,], # 8
    [ 0,  0,  0,  0, 13, 14, 14, 15, 16, 16, 16, 17, 17, 18, 18, 18, 18, 18, 18,], # 9
    [ 0,  0,  0,  0, 13, 14, 15, 16, 16, 17, 17, 18, 18, 18, 19, 19, 19, 20, 20,], # 10
    [ 0,  0,  0,  0, 13, 14, 15, 16, 17, 17, 18, 19, 19, 19, 20, 20, 20, 21, 21,], # 11
    [ 0,  0,  0,  0, 13, 14, 16, 16, 17, 18, 19, 19, 20, 20, 21, 21, 21, 22, 22,], # 12
    [ 0,  0,  0,  0,  0, 15, 16, 17, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 23,], # 13
    [ 0,  0,  0,  0,  0, 15, 16, 17, 18, 19, 20, 20, 21, 22, 22, 23, 23, 23, 24,], # 14
    [ 0,  0,  0,  0,  0, 15, 16, 18, 18, 19, 20, 21, 22, 22, 23, 23, 24, 24, 25,], # 15
    [ 0,  0,  0,  0,  0,  0, 17, 18, 19, 20, 21, 21, 22, 23, 23, 24, 25, 25, 25,], # 16
    [ 0,  0,  0,  0,  0,  0, 17, 18, 19, 20, 21, 22, 23, 23, 24, 25, 25, 26, 26,], # 17
    [ 0,  0,  0,  0,  0,  0, 17, 18, 19, 20, 21, 22, 23, 24, 25, 25, 26, 26, 27,], # 18
    [ 0,  0,  0,  0,  0,  0, 17, 18, 20, 21, 22, 23, 23, 24, 25, 26, 26, 27, 27,], # 19
    [ 0,  0,  0,  0,  0,  0, 17, 18, 20, 21, 22, 23, 24, 25, 25, 26, 27, 27, 28,], # 20
]