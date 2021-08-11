def sort(seq):
    length = len(seq)
    was_replace = True
    while was_replace:
        was_replace = False
        for i in range(length - 1):
            if seq[i] > seq[i+1]:
                was_replace = True
                seq[i], seq[i+1] = seq[i+1], seq[i]
        if was_replace:
            length -= 1
            print(' '.join([str(x) for x in seq]))
    if length == len(seq):
        print(' '.join([str(x) for x in seq]))



if __name__ == '__main__':
    n = int(input())
    seq = [int(x) for x in input().strip().split()]
    sort(seq)