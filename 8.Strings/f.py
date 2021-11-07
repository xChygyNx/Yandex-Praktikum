from typing import List, Tuple


def insert_str(rita_str: str, gosha_lines: List[Tuple[str, int]]) -> str:
    result = []
    symbol = iter(rita_str)
    for i in range(len(rita_str)):
        try:
            while gosha_lines[-1][1] == i:
                result.append(gosha_lines[-1][0])
                gosha_lines.pop()
        except IndexError:
            pass
        result.append(next(symbol))
    while len(gosha_lines) != 0:
        result.append(gosha_lines[-1][0])
        gosha_lines.pop()
    return ''.join(result)


if __name__ == '__main__':
    rita_str = input()
    n = int(input())
    gosha_lines = []
    for _ in range(n):
        line = input().split()
        gosha_lines.append((line[0], int(line[1])))
    gosha_lines.sort(key=lambda x: x[1], reverse=True)
    rita_str = insert_str(rita_str, gosha_lines)
    print(rita_str)
