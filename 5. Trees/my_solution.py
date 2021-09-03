from node import Node

# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def insert(root, key):
    result = root
    while True:
        if root.value <= key:
            if root.right is None:
                root.right = Node(value=key)
                break
            else:
                root = root.right
        if root.value > key:
            if root.left is None:
                root.left = Node(value=key)
                break
            else:
                root = root.left
    return result

def test():
    node1 = Node(None, None, 7)
    node2 = Node(node1, None, 8)
    node3 = Node(None, node2, 7)
    new_head = insert(node3, 6)
    assert new_head is node3
    assert new_head.left.value == 6
