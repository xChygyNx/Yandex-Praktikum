from typing import List


def construct_table(sum: int, nominals: List[int]) -> List[List[int]]:
    tab = [[0 for _ in range(sum + 1)] for _ in range(len(nominals) + 1)]
    for i in range(1, sum + 1):
        if i % nominals[0] == 0:
            tab[1][i] = 1
    for i in range(2, len(nominals) + 1):
        for j in range(1, sum + 1):
            if j <= nominals[i-1]:
                tab[i][j] = tab[i-1][j] + j // nominals[i-1]
            else:
                tab[i][j] = tab[i-1][j] + tab[i][j-nominals[i-1]]
    return tab


if __name__ == '__main__':
    sum = int(input())
    _ = input()
    nominals = [int(x) for x in input().split()]
    table = construct_table(sum, nominals)
    print(table[-1][-1])