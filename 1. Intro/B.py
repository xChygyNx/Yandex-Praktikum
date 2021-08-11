# ID 52221215
from typing import List
import array


FIELD_SIZE = 4


def read_field() -> List[str]:
    field = []
    for _ in range(FIELD_SIZE):
        field.extend([x for x in input().strip()])
    return field


def count_buttons_on_field(field: List[str]) -> array.array:
    result = array.array('i', [0]*10)
    for num in field:
        try:
            num = int(num)
        except ValueError:
            continue
        result[num] += 1
    return result


def count_successes(k: int, buttons: array.array) -> int:
    success = 0
    for button_count in buttons:
        if 0 < button_count <= 2 * k:
            success += 1
    return success


if __name__ == '__main__':
    k = int(input())
    field = read_field()
    buttons = count_buttons_on_field(field)
    success = count_successes(k, buttons)
    print(success)