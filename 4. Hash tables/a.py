def polynom_hash(a: int, m: int, line:str) -> None:
    _sum = 0
    for s in line:
        _sum = _sum * a + ord(s)
        _sum %= m
    print(_sum)


if __name__ == '__main__':
    a = int(input())
    m = int(input())
    line = input()
    polynom_hash (a, m, line)
