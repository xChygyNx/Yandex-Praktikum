from typing import List, Tuple, Set
from copy import copy


def define_luggage(items: List[Tuple[int, int]], bag_v: int) -> List[List[int]]:
    tab = [[0 for _ in range(bag_v + 1)] for _ in range(len(items) + 1)]
    tab[1] = [0 if x < items[0][0] else items[0][1] for x in range(bag_v + 1)]
    for i in range(2, len(items) + 1):
        for j in range(1, bag_v + 1):
            if j < items[i-1][0]:
                tab[i][j] = tab[i - 1][j]
            elif tab[i-1][j] >= tab[i-1][j-items[i-1][0]] + items[i - 1][1]:
                tab[i][j] = tab[i-1][j]
            else:
                tab[i][j] = tab[i-1][j-items[i-1][0]] + items[i-1][1]
    return tab


def define_items_list(items: List[Tuple[int, int]], luggage: List[List[int]]) -> List[int]:
    i, j = len(luggage) - 1, len(luggage[0]) - 1
    lst = []
    while luggage[i][j] > 0:
        if luggage[i][j] != luggage[i][j-1]:
            if luggage[i][j] != luggage[i-1][j]:
                lst.append(i)
                j -= items[i-1][0]
            i -= 1
        else:
            j -= 1
    return lst


def read_items(n_items: int) -> List[Tuple[int, int]]:
    items = []
    for _ in range(n_items):
        weight, cost = [int(x) for x in input().split()]
        items.append((weight, cost))
    return items


if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    items = read_items(n)
    luggage = define_luggage(items, m)
    items_list = define_items_list(items, luggage)
    print(len(items_list))
    print(' '.join([str(x) for x in items_list]))
