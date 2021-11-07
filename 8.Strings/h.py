from typing import List


def find_match(line: List[int], pattern: List[int]) -> List[int]:
    result = []
    if len(line) < len(pattern):
        return result
    else:
        for i in range(len(line)):
            c = pattern[0] - line[i]
            if len(line[i:]) < len(pattern):
                break
            if line[i: i+len(pattern)] == pattern or line[i: i+len(pattern)] == [x - c for x in pattern] :
                result.append(i+1)
    return result


if __name__ == '__main__':
    _ = input()
    line = [int(x) for x in input().split()]
    _ = input()
    pattern = [int(x) for x in input().split()]
    res = find_match(line, pattern)
    print(' '.join([str(x) for x in res]))