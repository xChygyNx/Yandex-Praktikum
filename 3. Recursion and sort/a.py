def generate_seq(n):
    if n == 0:
        return ['']
    else:
        tmp = generate_seq(n-1)
        a = [('(' + x) for x in tmp]
        b = [(')' + x) for x in tmp]
        result = a + b
        return result


def seq_correct(seq):
    sum = 0
    for symbol in seq:
        if symbol == '(':
            sum += 1
        else:
            sum -= 1
        if sum < 0:
            return False
    if sum > 0:
        return False
    return True


def clear_seq(seq):
    result = []
    for s in seq:
        if seq_correct(s):
            result.append(s)
    result.sort()
    return result


if __name__ == '__main__':
    n = int(input())
    result = generate_seq(2*n)
    result = clear_seq(result)
    for elem in result:
        print(elem)