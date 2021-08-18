def compare_str(str1: str, str2: str) -> bool:
    mapping = {}
    reverse_mapping = {}
    if len(str1) != len(str2):
        return False
    for letter1, letter2 in zip(str1, str2):
        try:
            if letter2 != mapping[letter1]:
                return False
        except KeyError:
            mapping[letter1] = letter2
        try:
            if letter1 != reverse_mapping[letter2]:
                return False
        except KeyError:
            reverse_mapping[letter2] = letter1
    return True


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    if compare_str(str1, str2):
        print('YES')
    else:
        print('NO')