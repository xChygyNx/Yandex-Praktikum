def strange_cmp(str1: str, str2: str) -> str:
    if len(str1) != len(str2):
        return 'NO'
    dict1, dict2 = {}, {}
    for ch1, ch2 in zip(str1, str2):
        try:
            save_ch1 = dict1[ch1]
            if save_ch1 != ch2:
                return 'NO'
        except KeyError:
            dict1[ch1] = ch2
        try:
            save_ch2 = dict2[ch2]
            if save_ch2 != ch1:
                return 'NO'
        except KeyError:
            dict2[ch2] = ch1
    return 'YES'


if __name__ == '__main__':
    str1 = input()
    str2 = input()
    print(strange_cmp(str1, str2))