from typing import List, Union


def int_or_float(num: float) -> Union[int, float]:
    if int(num) == num:
        return int(num)
    return num


def find_mediana(islands1: List[int], islands2: List[int], len1: int, len2: int) -> Union[int, float]:
    is_even = (len1 + len2) % 2 == 0
    k = len1 // 2
    mid = search(islands1, islands2, ks)




if __name__ == '__main__':
    n_north = int(input())
    n_south = int(input())
    islands1 = [int(x) for x in input().split()]
    islands2 = [int(x) for x in input().split()]
    print(find_mediana(islands1, islands2, n_north, n_south))