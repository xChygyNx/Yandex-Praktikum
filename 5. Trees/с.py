# Comment it before submitting
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.right = right
        self.left = left


def MLR(root, main_root, nodes):
    if root is None or root == main_root:
        return
    else:
        nodes.append(root.value)
        MLR(root.left, main_root, nodes)
        MLR(root.right, main_root, nodes)


def MRL(root, main_root, nodes):
    if root is None or root == main_root:
        return
    else:
        nodes.append(root.value)
        MRL(root.right, main_root, nodes)
        MRL(root.left, main_root, nodes)


def solution(root):
    left_nodes = []
    right_nodes = []
    MLR(root.left, root, left_nodes)
    MRL(root.right, root, right_nodes)
    if len(left_nodes) != len(right_nodes):
        return False
    for left_node, right_node in zip(left_nodes, right_nodes):
        if left_node != right_node:
            return False
    return True



def test():
    node1 = Node(3,  None,  None)
    node2 = Node(4,  None,  None)
    node3 = Node(4,  None,  None)
    node4 = Node(3,  None,  None)
    node5 = Node(2, node1, node2)
    node6 = Node(2, node3, node4)
    node7 = Node(1, node5, node6)
    assert solution(node7)


if __name__ == '__main__':
    test()