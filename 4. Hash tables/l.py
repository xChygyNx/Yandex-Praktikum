from typing import Dict


A = 123
M = 100003


class MyString:
    def __init__(self, line: str):
        self.str = line

    def __hash__(self) -> int:
        _sum = 0
        for s in self.str:
            _sum = _sum * A + ord(s)
            _sum %= M
        return _sum

    def __eq__(self, other):
        if self.__hash__() == other.__hash__():
            if len(self.str) == len(other.str):
                for s1, s2 in zip(self.str, other.str):
                    if s1 != s2:
                        return False
                return True
        return False

    def count(self, pattern) -> int:
        result = 0
        len_pattern = len(pattern.str)
        len_line = len(self.str)
        for i in range(len_line - len_pattern):
            if pattern == MyString(self.str[i: i + len_pattern]):
                result += 1
        return result


def extract_substrings(line: str, n: int, len_line: int) -> Dict[MyString, int]:
    result = {}
    for i in range(len_line - n):
        substring = MyString(line[i: i + n])
        try:
            _ = result[substring]
        except KeyError:
            result[substring] = i
    return result





def print_substrings(line: str, match: int, substrings_inds: Dict[MyString, int]) -> None:
    ind = []
    line = MyString(line)
    for key, value in substrings_inds.items():
        if line.count(key) >= match:
            ind.append(value)
    print(' '.join([str(x) for x in ind]))


if __name__ == '__main__':
    n, k = [int(x) for x in input().split()]
    line = input()
    len_line = len(line)
    substring_inds = extract_substrings(line, n, len_line)
    print_substrings(line, k, substring_inds)