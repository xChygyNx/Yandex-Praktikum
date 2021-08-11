if __name__== '__main__':
    a = input()
    b = input()
    print(len(a) == len(b))
    print(a == b)
    for i in range(len(a)):
        if a[i] != b[i]:
            print(f'a = {a[i]}, b = {b[i]}, i = {i}')