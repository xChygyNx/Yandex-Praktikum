from typing import List


def final_merge(regions: List[dict]) -> List[dict]:
    pos = 0
    ind = [0]
    result = []
    for i, region in enumerate(regions):
        if region.get('start') <= regions[pos]['finish']:
            if region.get('finish') > regions[pos]['finish']:
                regions[pos]['finish'] = region.get('finish')
        else:
            pos = i
            ind.append(pos)
    for index in ind:
        result.append(regions[index])
    return result


def sort_dict(elem: dict) -> int:
    return elem.get('start')


if __name__ == '__main__':
    n = int(input())
    result = []
    for _ in range(n):
        a, b = [int(x) for x in input().split()]
        result.append({'start': a, 'finish': b})
    result.sort(key=sort_dict)
    result = final_merge(result)
    for region in result:
        print(f"{region.get('start')} {region.get('finish')}")
