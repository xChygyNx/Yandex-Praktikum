from typing import Tuple, List


def read_input() -> Tuple[int, List[int]]:
    _ = input()
    s = int(input())
    nums = [int(x) for x in input().split()]
    nums.sort()
    return s, nums


def find_quatro(need_sum: int, nums: List[int]) -> List[Tuple[int, int, int, int]]:
    length = len(nums)
    quatros = set()
    look_elems = set()
    for i in range(length - 2):
        if need_sum < nums[i]:
            break
        for j in range(i + 1, length-1):
            if need_sum < nums[i] + nums[j]:
                break
            for k in range(j + 1, length):
                target = need_sum - nums[i] - nums[j] - nums[k]
                if target < 0:
                    break
                if target in look_elems:
                    quatros.add((target, nums[i], nums[j], nums[k]))
        look_elems.add(nums[i])
    quatros = list(quatros)
    quatros.sort()
    return quatros


def print_result(quatros: List[Tuple[int, int, int, int]]) -> None:
    print(len(quatros))
    for quatro in quatros:
        print(' '.join([str(x) for x in quatro]))


if __name__ == '__main__':
    data = read_input()
    quatros = find_quatro(data[0], data[1])
    print_result(quatros)
