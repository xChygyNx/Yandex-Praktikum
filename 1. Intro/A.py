# ID 52221034
from typing import NamedTuple, List


class Street(NamedTuple):
    length: int
    house_distance: List[int]


def read_street() -> Street:
    length = int(input())
    street = [int(x) for x in input().split()]
    return Street(length=length, house_distance=street)


def direct_distance(street: Street) -> None:
    pos = 0
    while street.house_distance[pos] != 0:
        street.house_distance[pos] = None
        pos += 1
    distance = 0
    for i in range(pos + 1, street.length):
        if street.house_distance[i] != 0:
            distance += 1
        else:
            distance = 0
        street.house_distance[i] = distance


def reverse_distance(street: Street) -> None:
    for i in range(street.length-1, -1, -1):
        if street.house_distance[i] == 0:
            break
    distance = 0
    for pos in range(i, -1, -1):
        try:
            if street.house_distance[pos] == 0:
                distance = 0
            elif distance < street.house_distance[pos]:
                distance += 1
            else:
                continue
        except TypeError:
            distance += 1
        street.house_distance[pos] = distance


if __name__ == '__main__':
    street = read_street()
    direct_distance(street)
    reverse_distance(street)
    print(' '.join([str(x) for x in street.house_distance]))

