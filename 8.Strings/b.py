if __name__ == '__main__':
    line = [x for x in input().split()]
    i, j = 0, len(line) - 1
    while i < j:
        line[i], line[j] = line[j], line[i]
        i += 1
        j -= 1
    print(' '.join(line))
