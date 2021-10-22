from typing import Set


def define_count_banknotes(cost: int, nominals: Set[int]) -> int:
    tab = [None for _ in range(cost+1)]
    for i in range(1, cost+1):
        if i in nominals:
            tab[i] = 1
        else:
            min_count = float('inf')
            for nominal in nominals:
                ind = i - nominal
                if ind > 0:
                    try:
                        min_count = min(tab[ind] + 1, min_count)
                    except TypeError:
                        pass
            tab[i] = min_count
    return tab[-1]


if __name__ == '__main__':
    cost = int(input())
    _ = input()
    nominals = set([int(x) for x in input().split()])
    print(define_count_banknotes(cost, nominals))