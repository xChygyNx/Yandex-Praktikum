from array import array

def fibonachi(n: int) -> int:
    seq = array('I', [0]*(n+1))
    seq[0] = 1
    if n == 0:
        return seq[0]
    else:
        seq[1] = 1
        i = 1
        for i in range(2, n+1):
            seq[i] = (seq[i-1] + seq[i-2]) % 1000000000
        return seq[i]


def count_divisor(k: int) -> int:
    result = 1
    for _ in range(k):
        result *= 10
    return result


if __name__ == '__main__':
    line = input().strip().split()
    n, k = int(line[0]), int(line[1])
    divisor = count_divisor(k)
    print(fibonachi(n) % divisor)
