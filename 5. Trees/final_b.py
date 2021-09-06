# Comment it before submitting
# class Node:
#     def __init__(self, left=None, right=None, value=0):
#         self.right = right
#         self.left = left
#         self.value = value


def find_remove_node(root, key):
    if root is None:
        return None, None
    if root.value == key:
        return None, root
    elif root.left is not None and root.left.value == key:
        return root, root.left
    elif root.right is not None and root.right.value == key:
        return root, root.right
    if root.value >= key:
        return find_remove_node(root.left, key)
    else:
        return find_remove_node(root.righy, key)


def find_leaf_node(parent, direction, reverse_direction):
    child_root = getattr(parent, reverse_direction)
    while getattr(child_root, direction) is not None:
        parent = child_root
        child_root = getattr(child_root, direction)
    if child_root.left is None and child_root.right is None:
        setattr(parent, reverse_direction, None)
    else:
        setattr(parent, reverse_direction, getattr(child_root, reverse_direction))
    return child_root


def restore_BST(root):
    if root is None:
        return
    while True:
        if root.left is not None and root.left.value > root.value:
            root.left.value, root.value = root.value, root.left.value
            root = root.left
        elif root.right is not None and root.right.value < root.value:
            root.right.value, root.value = root.value, root.right.value
            root = root.right
        else:
            break


def remove(root, key):
    init_root = root
    if root is None:
        return None
    parent_remove_node, remove_node = find_remove_node(root, key)
    if remove_node is None:
        return None
    if remove_node.left is not None:
        leaf_node = find_leaf_node(remove_node, 'right', 'left')
    elif remove_node.right is not None:
        leaf_node = find_leaf_node(remove_node, 'left', 'right')
    try:
        if parent_remove_node.left == remove_node:
            parent_remove_node.left = leaf_node
        else:
            parent_remove_node.right = leaf_node
        leaf_node.left, leaf_node.right = remove_node.left, remove_node.right
        restore_BST(leaf_node)
    except AttributeError:
        pass
    return init_root



def test():
    node1 = Node(None, None, 2)
    node2 = Node(node1, None, 3)
    node3 = Node(None, node2, 1)
    node4 = Node(None, None, 6)
    node5 = Node(node4, None, 8)
    node6 = Node(node5, None, 10)
    node7 = Node(node3, node6, 5)
    newHead = remove(node7, 10)
    assert newHead.value == 5
    assert newHead.right is node5
    assert newHead.right.value == 8


if __name__ == '__main__':
    test()