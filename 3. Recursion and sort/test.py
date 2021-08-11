from typing import NamedTuple

class A(NamedTuple):
    num: int
    word: str
    num2: int


def sort_list(lst: list) -> list:
    length = len(lst)
    if length <= 1:
        return lst
    if length == 2:
        if lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
            return lst
    start = 1
    end = length - 1
    pivot = lst[0]
    while start < end:
        while lst[start] <= pivot and start < end:
            start += 1
        while lst[end] >= pivot and end > start:
            end -= 1
        if lst[start] > pivot and lst[end] < pivot:
            lst[start], lst[end] = lst[end], lst[start]
    lst[0], lst[start - 1] = lst[start - 1], lst[0]
    return sort_list(lst[:start-1]) + [lst[start-1]] + sort_list(lst[start:])

if __name__ == '__main__':
    # a = A(1, 'main', -1)
    # b = A(1, 'maban', -1)
    # c = A(0, 'main', -1)
    # d = A(1, 'main', 8)
    # e = A(1, 'yes', -1)
    # res = [a, b, c, d, e]
    result = [35, 33, 42, 10, 14, 19, 27, 44, 26, 31]
    result = sort_list(result)
    print(result)