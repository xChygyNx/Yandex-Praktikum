from typing import List


def prefix_hashes(a: int, m: int, line: str) -> List[int]:
    hashes = [0] * (len(line))
    _sum = 0
    for i, s in enumerate(line):
        _sum = (_sum * a + ord(s)) % m
        hashes[i] = (_sum)
    return hashes


def collect_sqrs(base: int, mod: int, length: int):
    result = [1] * (length + 1)
    for i in range(1, length + 1):
        result[i] = (result[i - 1] * base) % mod
    return result


def print_need_hashes(hashes: List[int], pows: List[int], m: int) -> None:
    n = int(input())
    for _ in range(n):
        start, end = [int(x) for x in input().split()]
        full_hash = hashes[end - 1]
        start_ind = start - 2
        if start_ind < 0:
            prefix_hash = 0
        else:
            prefix_hash = hashes[start_ind]
        p = pows[end - start + 1]
        result = full_hash - (p * prefix_hash)
        print((result % m + m) % m)



if __name__ == '__main__':
    a = int(input())
    m = int(input())
    line = input()
    pows = collect_sqrs(a, m, len(line))
    prf_hashes = prefix_hashes(a, m, line)
    print_need_hashes(prf_hashes, pows, m)

