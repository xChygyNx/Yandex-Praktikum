if __name__ == '__main__':
    n = input()
    colleges = [x for x in input().split()]
    k = int(input())
    result = {}
    for college in colleges:
        result[college] = result.get(college, 0) + 1
    result = list(result.items())
    result.sort(key=lambda elem: elem[1], reverse=True)
    print(' '.join([str(x[0]) for x in result[:k]]))