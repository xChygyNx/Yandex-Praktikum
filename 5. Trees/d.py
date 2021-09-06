from itertools import chain


# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def MLR(root, nodes):
    if root is None:
        return
    else:
        MLR(root.left, nodes)
        nodes.append(root.value)
        MLR(root.right, nodes)


def solution(root1, root2):
    nodes1 = []
    nodes2 = []
    MLR(root1, nodes1)
    MLR(root2, nodes2)
    if len(nodes1) != len(nodes2):
        return False
    for node1, node2 in zip(nodes1, nodes2):
        if node1 != node2:
            return False
    return True



def test():
    node1 = Node(1, None, None)
    node2 = Node(2, None, None)
    node3 = Node(3, node1, node2)

    node4 = Node(1, None, None)
    node5 = Node(2, None, None)
    node6 = Node(3, node4, node5)

    assert solution(node3, node6)


if __name__ == '__main__':
    test()


