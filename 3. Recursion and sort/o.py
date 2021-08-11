import itertools
from math import fabs
import cProfile
from typing import List


def solution_old(areas: List[int], n: int, k: int):
    result = []
    for i, j in itertools.combinations(range(n), 2):
        result.append(int(fabs(areas[i] - areas[j])))
    result.sort()
    print(result[k-1])



def solution_new(areas: List[int], n: int, k: int):
    result = []
    v = 0
    for i, j in itertools.combinations(range(n), 2):
        if v < k:
            result.append(int(fabs(areas[i] - areas[j])))
            result.sort()
        else:
            difference = int(fabs(areas[i] - areas[j]))
            if difference < result[k-1]:
                result[k-1] = difference
                result.sort()
        v += 1
    print(result[k-1])


def insert_elem(lst: List[int], elem: int) -> None:
    lst.pop()
    if len(lst) == 0:
        lst.append(elem)
    else:
        for i, num in enumerate(lst):
            if elem <= num:
                lst.insert(i, elem)
                return
        lst.append(elem)


def solution_new_new(areas: List[int], n: int, k: int):
    result = []
    v = 0
    for i, j in itertools.combinations(range(n), 2):
        if v < k - 1:
            result.append(int(fabs(areas[i] - areas[j])))
        elif v == k - 1:
            result.append(int(fabs(areas[i] - areas[j])))
            result.sort()
        else:
            difference = int(fabs(areas[i] - areas[j]))
            if difference < result[k-1]:
                insert_elem(result, difference)
        v += 1
    print(result[k-1])



def solution():
    n = int(input())
    areas = [int(x.replace(',', '')) for x in input().split()]
    k = int(input())
    solution_old(areas, n, k)
    solution_new(areas, n, k)
    solution_new_new(areas, n, k)


if __name__ == '__main__':
    cProfile.run('solution()')
