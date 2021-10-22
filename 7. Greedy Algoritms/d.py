MOD = 10 ** 9 + 7


def dynamic_fibonacci(n: int) -> int:
    tab = [0 for _ in range(n + 1)]
    tab[0] = tab[1] = 1
    for i in range(2, n+1):
        tab[i] = (tab[i-1] + tab[i-2]) % MOD
    return tab[-1]


if __name__ == '__main__':
    n = int(input())
    print(dynamic_fibonacci(n))
