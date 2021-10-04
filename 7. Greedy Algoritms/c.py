from typing import List, Tuple


def read_heaps(n: int) -> List[Tuple[int, int]]:
    heaps = []
    for _ in range(n):
        heaps.append(tuple([int(x) for x in input().split()]))
    heaps.sort(reverse=True)
    return heaps


def maximize_profit(v: int, heaps: List[Tuple[int, int]]) -> int:
    profit = 0
    for cost, count in heaps:
        weight = min(count, v)
        profit += cost * weight
        v -= weight
        if v == 0:
            break
    return profit



if __name__ == '__main__':
    v = int(input())
    n = int(input())
    heaps = read_heaps(n)
    max_cost = maximize_profit(v, heaps)
    print(max_cost)