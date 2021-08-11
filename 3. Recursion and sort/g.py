if __name__  == '__main__':
    n = int(input())
    clothes = [int(x) for x in input().split()]
    colors = [0] * 3
    for ind in clothes:
        colors[ind] += 1
    for i in range(3):
        if colors[i] > 0:
            line = ' '.join([str(i)] * colors[i])
            print(line, end=' ')