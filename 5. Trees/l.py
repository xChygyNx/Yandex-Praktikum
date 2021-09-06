def get_idx_max_elem(heap, idx) -> int:
    if heap[idx * 2] > heap[idx * 2 + 1]:
        return idx * 2
    return idx * 2 + 1


def sift_down(heap, idx):
    while True:
        try:
            left_child = heap[idx * 2]
        except IndexError:
            break
        try:
            right_child = heap[idx * 2 + 1]
        except IndexError:
            right_child = None
        if right_child is None:
            new_idx = idx * 2
        else:
            new_idx = get_idx_max_elem(heap, idx)
        if heap[idx] >= heap[new_idx]:
            break
        heap[idx], heap[new_idx] = heap[new_idx], heap[idx]
        idx = new_idx
    return idx


def test():
    sample = [-1, 12, 1, 8, 3, 4, 7]
    assert sift_down(sample, 2) == 5


if __name__ == '__main__':
    test()