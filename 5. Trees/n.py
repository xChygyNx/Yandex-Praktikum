# Comment it before submitting
from typing import Tuple


class Node:
    def __init__(self, left=None, right=None, value=0, size=0):
        self.right = right
        self.left = left
        self.value = value
        self.size = size


def find_k_th(root, k):
    left_size = 0 if root.left is None else root.left.size
    if k == left_size:
        return root
    elif left_size > k:
        return find_k_th(root.left, k)
    else:
        return find_k_th(root.right, k - left_size - 1)


def left_separate(root, init_root, split_node) -> Tuple:
    while True:
        if root.value == split_node.value:
            left_tree = root
            init_root.size -= left_tree.size
            break
        if root.value < split_node.value:
            root = root.left
        else:
            root = root.right
    return left_tree, init_root


def right_separate(root, init_root, split_node) -> Tuple:
    while True:
        if root.value == split_node.value:
            right_tree = root.left if root.left is not None else root.right
            init_root.size -= root.size - 1
            right_tree.size = root.size - 1
            break
        if root.value < split_node.value:
            root = root.left
        else:
            root = root.right
    return init_root, right_tree


def separate(root, split_node) -> Tuple:
    if root.value == split_node.value:
        left_tree = root.left
        left_size = 0 if root.left is None else root.left.size
        root.size -= left_size
        return left_tree, root
    elif root.value > split_node.value:
        return left_separate(root.left, root, split_node)
    else:
        return right_separate(root.right, root, split_node)


def split(root, k) -> Tuple[Node, Node]:
    split_node = find_k_th(root, k)
    tree_one, tree_two = separate(root, split_node)
    return tree_one, tree_two

def test():
    node1 = Node(None, None, 3, 1)
    node2 = Node(None, node1, 2, 2)
    node3 = Node(None, None, 8, 1)
    node4 = Node(None, None, 11, 1)
    node5 = Node(node3, node4, 10, 3)
    node6 = Node(node2, node5, 5, 6)
    left, right = split(node6, 4)
    assert(left.size == 4)
    assert(right.size == 2)


if __name__ == '__main__':
    test()