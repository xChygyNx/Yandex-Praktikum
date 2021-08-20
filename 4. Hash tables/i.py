from typing import List, Dict


def find_max_subseq(first: Dict[str, List[int]], second: List[str], s_len: int) -> int:
    max_eq_seq_len = 0
    for i, num in enumerate(second):
        try:
            indexes = first[num]
        except KeyError:
            continue
        for ind in indexes:
            tmp_eq_seq_len = 1
            k = 1
            while i+k < s_len:
                try:
                    if ind + k in first.get(second[i+k]):
                        tmp_eq_seq_len += 1
                        k += 1
                    else:
                        break
                except TypeError:
                    break
            max_eq_seq_len = tmp_eq_seq_len if tmp_eq_seq_len > max_eq_seq_len else max_eq_seq_len
    return max_eq_seq_len


def get_line_dict() -> Dict[str, List[int]]:
    result = {}
    line = [x for x in input().split()]
    for i, num in enumerate(line):
        try:
            result[num].append(i)
        except KeyError:
            result[num] = [i]
    return result


if __name__ == '__main__':
    _ = int(input())
    first = get_line_dict()
    s_len = int(input())
    second = [x for x in input().split()]
    print(find_max_subseq(first, second, s_len))
