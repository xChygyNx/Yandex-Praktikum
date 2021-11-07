from typing import List


SENTINEL = '#'


def prefix_func(word: str, pattern: str) -> List[int]:
    line = pattern + SENTINEL + word
    result = []
    dp = [None for _ in range(len(pattern))]
    dp[0] = 0
    k_prev = 0
    for i in range(1, len(line)):
        k = k_prev
        while k > 0 and line[i] != line[k]:
            k = dp[k - 1]
        if line[i] == line[k]:
            k += 1
        if i < len(pattern):
            dp[i] = k
        k_prev = k
        if k == len(pattern):
            result.append(i - 2 * len(pattern))
    return result


def replace_str(word: str, pattern: str, replace: str, places: List[int]) -> str:
    l = len(pattern)
    places.reverse()
    for place in places:
        word = word[:place] + replace + word[place + l:]
    return word


if __name__ == '__main__':
    word, pattern, replace = input(), input(), input()
    places = prefix_func(word, pattern)
    print(replace_str(word, pattern, replace, places))
