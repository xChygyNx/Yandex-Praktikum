from typing import List


def give_cookie(kids: List[int], sizes: List[int]) -> int:
    happy = 0
    pos = 0
    cookies_count = len(sizes)
    for size in kids:
        for i in range(pos, cookies_count):
            if sizes[i] >= size:
                pos = i+1
                happy += 1
                break
    return happy


if __name__ == '__main__':
    kids = input()
    f_greedy = [int(x) for x in input().split()]
    cookies = input()
    sizes = [int(x) for x in input().split()]
    f_greedy.sort()
    sizes.sort()
    happy = give_cookie(f_greedy, sizes)
    print(happy)