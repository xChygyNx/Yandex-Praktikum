import cProfile
from typing import List




def solution_new_new_new(areas: List[int], n: int, k: int):
    areas.sort()
    left, right = 0, n
    count = 0
    mid = (areas[right] - areas[0]) // 2
    while left < right:
        for i in range(n):
            while areas[right] - areas[i] > mid:
                count += 1



def solution():
    n = int(input())
    areas = [int(x.replace(',', '')) for x in input().split()]
    k = int(input())
    solution_new_new_new(areas, n, k)


if __name__ == '__main__':
    cProfile.run('solution()')
