from typing import List, Tuple
import sys


def selective_increment(sides: List[int], k1: int, k2: int, length: int) -> Tuple[int, int]:
    a = b = 0
    if k1 + 1 == k2:
        b = 1
    elif k2 == length - 1:
        a = 1
    else:
        sum_with_a = sides[k1 + 1] + sides[k2]
        sum_with_b = sides[k1] + sides[k2 + 1]
        if sum_with_a >= sum_with_b:
            a = 1
        else:
            b = 1
    return k1 + a, k2 + b


if __name__ == '__main__':
    n = input()
    sides = [int(x) for x in input().split()]
    sides.sort(reverse=True)
    length_sides = len(sides)
    for h in range(length_sides - 2):
        k1, k2 = h + 1, h + 2
        while True:
            if k2 == length_sides:
                break
            if sides[h] < sides[k1] + sides[k2]:
                print(sides[h] + sides[k1] + sides[k2])
                sys.exit()
            else:
                k1, k2 = selective_increment(sides, k1, k2, length_sides)