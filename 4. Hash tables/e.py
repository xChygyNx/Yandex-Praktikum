def find_unique_seq(line: str, n: int) -> int:
    max_len = 0
    current_len = 0
    seq_symbols = {}
    i = 0
    while i < n:
        try:
            ind = seq_symbols[line[i]]
            max_len = current_len if current_len > max_len else max_len
            current_len = 1
            seq_symbols.clear()
            i = ind + 1
            seq_symbols[line[i]] = i
        except KeyError:
            seq_symbols[line[i]] = i
            current_len += 1
        i += 1
    max_len = current_len if current_len > max_len else max_len
    return max_len


if __name__ == '__main__':
    line = input()
    n = len(line)
    print(find_unique_seq(line, n))