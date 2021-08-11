from typing import List, Union


def int_or_float(num: float) -> Union[int, float]:
    if int(num) == num:
        return int(num)
    return num


def find_mediana(islands1: List[int], islands2: List[int], len1: int, len2: int) -> Union[int, float]:
    i, j = 0, 0
    islands = [0] * (len1 + len2)
    for k in range(len1 + len2):
        if len1 == i:
            islands[k] = islands2[j]
            j += 1
        elif len2 == j:
            islands[k] = islands1[i]
            i += 1
        elif islands1[i] <= islands2[j]:
            islands[k] = islands1[i]
            i += 1
        else:
            islands[k] = islands2[j]
            j += 1
    mid = (len1 + len2) // 2
    if (len1 + len2) % 2 == 1:
        return islands[mid]
    else:
        return int_or_float((islands[mid - 1] + islands[mid]) / 2)



def separate_seq(islands1: List[int], islands2: List[int], len1: int, len2: int) -> Union[int, float]:
    if len1 + len2 <= 3:
        return find_mediana(islands1, islands2, len1, len2)
    mid1, mid2 = len1 // 2, len2 // 2
    if islands1[mid1] <= islands2[mid2]:
        return separate_seq(islands1[:mid1], islands2[mid2:], mid1, len2 - mid2)
    else:
        return separate_seq(islands1[mid1:], islands2[:mid2], len1 - mid1, len2)


if __name__ == '__main__':
    n_north = int(input())
    n_south = int(input())
    islands1 = [int(x) for x in input().split()]
    islands2 = [int(x) for x in input().split()]
    print(find_mediana(islands1, islands2, n_north, n_south))