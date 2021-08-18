from random import randint
from datetime import datetime, timedelta


A = 1000
M = 123987123


def create_seq() -> str:
    n = randint(10, 25)
    res = []
    for _ in range(n):
        res.append(randint(97, 122))
    return ''.join([chr(x) for x in res])


def define_hash(line) -> int:
    n = len(line)
    _sum = ord(line[0]) % M
    for i in range(1, n):
        _sum = _sum * A + ord(line[i])
        _sum %= M
    return _sum


def separate_hash(hash):
    res = [0] * 3
    for i in range(2, -1, -1):
        res[i] = hash % 1000
        hash //= 1000
    return res


if __name__ == '__main__':
    t = datetime.now()
    s1 = 'rst'
    s2 = 'pyimprwizfgfnhec'
    print(define_hash(s1), define_hash(s2))
    # while True:
    #     s1 = create_seq()
    #     h1 = define_hash(s1)
    #     # sep_h1 = separate_hash(h1)
    #     # if 97 <= sep_h1[0] <= 122 and\
    #     #     97 <= sep_h1[1] <= 122 and\
    #     #     97 <= sep_h1[2] <= 122:
    #     #     print(f'{s1}\t{h1}\t{sep_h1}')
    #     #     break
    #     # if h1 == h2:
    #     #     print('FIND!!!!!')
    #     #     break
    #     if datetime.now() - t > timedelta(seconds=10):
    #         print("Still work ...")
    #         t = datetime.now()


