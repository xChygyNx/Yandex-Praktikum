from typing import List


def final_merge(ranges: List[List[int]]) -> List[List[int]]:
    pos = 0
    ind = [0]
    result = []
    for i, ran in enumerate(ranges):
        if ran[0] <= ranges[pos][1]:
            if ran[1] > ranges[pos][1]:
                ranges[pos][1] = ran[1]
        else:
            pos = i
            ind.append(pos)
    for index in ind:
        result.append(ranges[index])
    return result


if __name__ == '__main__':
    n = input()
    nums = [int(x) for x in input().split()]
    tmp = []
    for i, num in enumerate(nums):
        tmp.append(list((i, nums.index(i))))
    tmp.sort()
    result = final_merge(tmp)
    print(len(result))