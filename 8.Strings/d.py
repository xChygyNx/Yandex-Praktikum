def str_to_dict(line: str) -> str:
    tmp_dict = {}
    for ch in line:
        tmp_dict[ch] = tmp_dict.get(ch, 0) + 1
    odd_lst, even_dict = [], {}
    for ch, num in tmp_dict.items():
        if num % 2 == 0:
            even_dict[ch] = num
        else:
            even_dict[ch] = num - 1
            odd_lst.append(ch)
    odd_lst, even_lst = sorted(odd_lst), sorted(list(even_dict.keys()))
    if len(odd_lst) > 0:
        odd_elem = odd_lst[0]
    else:
        odd_elem = ''
    result = []
    for ch in even_lst:
        for _ in range((even_dict[ch]) // 2):
            result.append(ch)
    final_result = ''.join(result) + odd_elem + ''.join(reversed(result))
    return final_result



if __name__  == '__main__':
    line = input()
    line = str_to_dict(line)
    print(line)