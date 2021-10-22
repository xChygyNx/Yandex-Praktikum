from typing import List


def read_field(rows_count: int) -> List[List[int]]:
    field = []
    for _ in range(rows_count):
        field.append([int(x) for x in input()])
    return field


def maximize_flowers(field: List[List[int]]) -> None:
    for i in range(len(field) - 1, -1, -1):
        for j in range(len(field[i])):
            if i == len(field) - 1 and j == 0:
                max_near_value = 0
            elif i == len(field) - 1:
                max_near_value = field[i][j-1]
            elif j == 0:
                max_near_value = field[i+1][j]
            else:
                max_near_value = max(field[i+1][j], field[i][j-1])
            field[i][j] += max_near_value


if __name__ == '__main__':
    n, m = [int(x) for x in input().split()]
    field = read_field(n)
    maximize_flowers(field)
    print(field[0][-1])