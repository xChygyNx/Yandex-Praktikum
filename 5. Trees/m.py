def sift_up(heap, idx):
    while True:
        if idx == 1:
            break
        if heap[idx] <= heap[idx // 2]:
            break
        heap[idx], heap[idx//2] = heap[idx//2], heap[idx]
        idx //= 2
    return idx


def test():
    sample = [-1, 12, 6, 8, 3, 15, 7]
    assert sift_up(sample, 5) == 1


if __name__ == '__main__':
    test()