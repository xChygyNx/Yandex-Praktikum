from typing import List


def count_variants(n: int, k: int) -> List[int]:
    variants = [0] * (n)
    variants[0] = 0
    for i in range(1, n):
        for j in range(1, k + 1):
            ind = i - j
            if ind > 0:
                variants[i] += variants[ind]
            elif ind == 0:
                variants[i] += 1
    return variants


if __name__ == '__main__':
    n, k = [int(x) for x in input().split()]
    variants = count_variants(n, k)
    print(variants[-1])