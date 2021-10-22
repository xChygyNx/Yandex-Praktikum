from typing import List, Union, Optional
from copy import copy


def compare_two(line: List[Union[float, int]], num: int) -> Optional[int]:
    if line[1] < num:
        return None
    elif line[0] >= num:
        return line[0]
    else:
        return line[1]


def binary_search(line: List[Union[float, int]], num: int) -> Optional[int]:
    start = 0
    end = len(line) - 1
    while end - start > 1:
        k = (end - start) // 2 + start
        if line[k] <= num:
            end = k
        else:
            start = k
    return k


def find_NONM(seq: List[int]) -> List[int]:
    sort_seq = copy(seq)
    sort_seq.sort()
    n = len(sort_seq)
    line = [-1 * float('inf') if x == 0 else float('inf') for x in range(n + 1)]
    for i in range(n):
        j = binary_search(line, seq[i])
        if (line[j-1] < seq[i] and seq[i] <= line[j]):
            line[j] = seq[i]
    return line


def build_route(line: List[int]) -> List[int]:
    route = []
    max_seq = line[-1]
    for i in range(1, max_seq+1):
        route.append(line.index(i))
    return route


if __name__ == '__main__':
    _ = input()
    seq = [int(x) for x in input().split()]
    line = find_NONM(seq)
    print(line[-1])
    # route = build_route(line)
    # print(' '.join([str(x) for x in route]))
