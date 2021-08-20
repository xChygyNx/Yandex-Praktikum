from typing import Tuple, List, Dict
from itertools import permutations

NEAR = 20

def round_coordinate():
    result = []
    sqr_near = NEAR ** 2
    for x, y in permutations(range(-20, 21), 2):
        distance = x ** 2 + y ** 2
        if distance <= sqr_near:
            result.append((x, y))
    return result


ROUND = round_coordinate()


def read_stations_lst(n: int) -> List[Tuple[int, int]]:
    stations = []
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        stations.append((x, y))
    return stations


def read_stations_set(n: int) -> Dict[Tuple[int, int], int]:
    stations = {}
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        stations[(x, y)] = stations.get((x, y), 0) + 1
    return stations


def count_near_stations(metro: List[Tuple[int, int]], bus: Dict[Tuple[int, int], int]) -> int:
    ind_max = 0
    max_station = 0
    for i, s_metro in enumerate(metro):
        near_stations = 0
        for dif in ROUND:
            n = bus.get((s_metro[0] + dif[0], s_metro[1] + dif[1]), 0)
            near_stations += n
        if near_stations > max_station:
            max_station = near_stations
            ind_max = i
    return ind_max + 1


if __name__ == '__main__':
    n_metro = int(input())
    metro_station = read_stations_lst(n_metro)
    n_bus = int(input())
    bus_station = read_stations_set(n_bus)
    near_stations = count_near_stations(metro_station, bus_station)
    print(near_stations)
