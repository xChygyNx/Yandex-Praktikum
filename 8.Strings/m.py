from typing import List


def prefix_func(word: str) -> List[int]:
    result = [None for _ in range(len(word))]
    result[0] = 0
    for i in range (1, len(word)):
        k = result[i-1]
        while k > 0 and word[i] != word[k]:
            k = result[k - 1]
        if word[i] == word[k]:
            k += 1
        result[i] = k
    return result


if __name__ == '__main__':
    word = input()
    result = prefix_func(word)
    print(' '.join([str(x) for x in result]))