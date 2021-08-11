def less(a, b):
    len_a = len(a)
    len_b = len(b)
    for i in range(100):
        if b[i % len_b] > a[i % len_a]:
            return True
        elif b[i % len_b] < a[i % len_a]:
            break
    return False


def sort(seq):
    was_replace = True
    length = len(seq)
    while was_replace:
        was_replace = False
        for i in range(length - 1):
            if less(seq[i], seq[i+1]):
                was_replace = True
                a = seq[i]
                b = seq[i+1]
                seq[i] = b
                seq[i+1] = a
        length -= 1



if __name__ == '__main__':
    n = int(input())
    nums = [x for x in input().strip().split()]
    sort(nums)
    print(''.join(nums))