from typing import List, Dict
import sys


class Series:
    def __init__(self, first_ind: int = None, last_ind: int = None):
        self.first_ind = first_ind
        self.last_ind = last_ind


def acum_result(games: List[str]) -> List[int]:
    tmp = 0
    result = []
    if len(set(games)) == 1:
        print(0)
        sys.exit()
    for res in games:
        num = -1 if int(res) == 0 else 1
        tmp += num
        result.append(tmp)
    return result


def define_draw_series(acum_res: List[int]) -> Dict[int, Series]:
    series = {}
    for i, res in enumerate(acum_res):
        result = series.get(res, Series())
        if result.first_ind is None:
            result.first_ind = i
        else:
            result.last_ind = i
        series[res] = result
    return series


def define_max_series(series: Dict[int, Series]) -> int:
    series_length = []
    for s in series.values():
        try:
            series_length.append(s.last_ind - s.first_ind)
        except TypeError:
            continue
    return max(series_length)


if __name__ == '__main__':
    n = int(input())
    result = [0]
    try:
        result.extend(acum_result(input().split()))
    except EOFError:
        result = []
    draw_series = define_draw_series(result)
    try:
        print(define_max_series(draw_series))
    except ValueError:
        print(0)
