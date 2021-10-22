from typing import List, NamedTuple, Tuple


class NOP(NamedTuple):
    length: int
    indexes1: List[int]
    indexes2: List[int]


def count_nop_tab(seq1: List[int], seq2: List[int]) -> List[List[int]]:
    tab = [[0 for _ in range(len(seq2) + 1)] for _ in range(len(seq1) + 1)]
    for i in range(len(seq1)):
        for j in range(len(seq2)):
            if seq1[i] == seq2[j]:
                tab[i+1][j+1] = tab[i][j] + 1
            else:
                tab[i+1][j+1] = max(tab[i][j+1], tab[i+1][j])
    return tab


def define_indexes(seq1: List[int], seq2: List[int], tab: List[List[int]]) -> Tuple[List[int], List[int]]:
    n = len(tab) - 1
    m = len(tab[n]) - 1
    indexes1, indexes2 = [], []
    while tab[n][m] != 0:
        if seq1[n-1] == seq2[m-1]:
            indexes1.append(n)
            indexes2.append(m)
            n -= 1
            m -= 1
        elif tab[n - 1][m] == tab[n][m]:
            n -= 1
        else:
            m -= 1
    return indexes1, indexes2



def find_nop(seq1: List[int], seq2: List[int]) -> NOP:
    tab = count_nop_tab(seq1, seq2)
    indexes1, indexes2 = define_indexes(seq1, seq2, tab)
    indexes1.reverse()
    indexes2.reverse()
    return NOP(length=tab[-1][-1], indexes1=indexes1, indexes2=indexes2)


if __name__ == '__main__':
    _ = input()
    seq1 = [int(x) for x in input().split()]
    _ = input()
    seq2 = [int(x) for x in input().split()]
    nop = find_nop(seq1, seq2)
    print(f'{nop.length}\n{" ".join([str(x) for x in nop.indexes1])}\n{" ".join([str(x) for x in nop.indexes2])}')