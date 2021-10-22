from typing import List, Union, NamedTuple


class NONM(NamedTuple):
    dp: List[int]
    pos: List[int]
    prev: List[int]


def binary_search(dp: List[Union[int, float]], num: int) -> int:
    start, end, n = 0, len(dp) - 1, len(dp)
    k = 0
    while end - start > 1:
        k = (start + end) // 2
        if dp[k] >= num:
            end = k
        else:
            start = k
    if dp[k] < num:
        return k+1
    else:
        return k


def find_NONM(seq: List[int]) -> List[int]:
    n = len(seq)
    dp = [-1 * float('inf') if i == 0 else float('inf') for i in range(n + 1)]
    pos, prev = [-1 for _ in range(n+1)], [-1 for _ in range(n+1)]
    for i in range(1, n + 1):
        j = binary_search(dp, seq[i - 1])
        if dp[j-1] < seq[i-1] and seq[i-1] < dp[j]:
            dp[j] = seq[i-1]
            pos[j] = seq[i-1]
            prev[j] = pos[j-1]
    dp = [x for x in dp if x != float('inf') and x != -1 * float('inf')]
    pos = [x for x in pos if x != -1]
    a = [-1]
    a.extend([x for x in prev if x != -1])
    return NONM(dp=dp, pos=pos, prev=a)


def find_elem(elem: int, seq: List[int], end: int) -> int:
    for i in range(end, -1, -1):
        if seq[i] == elem:
            return i



def build_route(seq: List[int], nonm: NONM) -> List[int]:
    route = []
    elem = nonm.pos[-1]
    end = len(seq) - 1
    for i in range(len(nonm.pos)-1, -1, -1):
        ind = find_elem(elem, seq, end)
        route.append(ind)
        end = ind - 1
        elem = nonm.prev[i]

    route.reverse()
    return route


if __name__ == '__main__':
    _ = input()
    seq = [int(x) for x in input().split()]
    nonm = find_NONM(seq)
    print(len(nonm.dp))
    route = build_route(seq, nonm)
    print(' '.join([str(x) for x in route]))
