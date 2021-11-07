from typing import List


def transform_str(*args) -> List[str]:
    result = []
    for arg in args:
        tmp = []
        for s in arg:
            if (ord(s) - ord('a')) % 2 == 1:
                tmp.append(s)
        result.append(''.join(tmp))
    return result


def cmp(str1: str, str2: str) -> int:
    i = -1
    for i, symbols in enumerate(zip(str1, str2)):
        s1, s2 = symbols
        if ord(s1) > ord(s2):
            return 1
        elif ord(s1) < ord(s2):
            return -1
    if len(str1[i+1:]) > 0:
        return 1
    elif len(str2[i+1:]) > 0:
        return -1
    return 0


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    str1, str2 = transform_str(str1, str2)
    print(cmp(str1, str2))