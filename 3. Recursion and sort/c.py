def find_subseq(pattern: str, line: str) -> bool:
    pattern_pos = 0
    if pattern == '':
        return True
    pattern_len = len(pattern)
    for n, symbol in enumerate(line):
        if symbol == pattern[pattern_pos]:
            pattern_pos += 1
            if pattern_pos == pattern_len:
                return True
    return False

if __name__ == '__main__':
    line1 = input()
    line2 = input()
    print(find_subseq(line1, line2))