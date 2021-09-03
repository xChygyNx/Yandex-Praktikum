# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def find_path_to_start(node, l, r):
    path = []
    while True:
        if node is None:
            break
        path.append(node)
        if l <= node.value <= r or node.value > r:
            node = node.left
        elif node.value < l:
            node = node.right
    return path


def traversal(node, l, r, result):
    if node is None:
        return
    traversal(node.left, l, r, result)
    if l <= node.value <= r:
        result.append(node.value)
    elif node.value > r:
        return
    traversal(node.right, l, r, result)


def traversal_with_path(path, l, r, result):
    for node in path:
        if l <= node.value <= r:
            result.append(node.value)
            traversal(node.right, l, r, result)


def print_range(node, l, r):
    path_to_start = find_path_to_start(node, l, r)
    result = []
    path_to_start.reverse()
    traversal_with_path(path_to_start, l, r, result)
    print(str(result)[1: -1].replace(',', ''))


def test():
    node1 = Node(None, None, 2)
    node2 = Node(None, node1, 1)
    node3 = Node(None, None, 8)
    node4 = Node(None, node3, 8)
    node5 = Node(node4, None, 9)
    node6 = Node(node5, None, 10)
    node7 = Node(node2, node6, 5)
    print_range(node7, 2, 8)
    # expected output: 2 5 8 8

if __name__ == '__main__':
    test()
