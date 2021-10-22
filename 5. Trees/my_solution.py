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
        return find_remove_node(root.right, key)


def find_leaf_node_in_left(parent):
    child_root = parent.left
    if child_root.right is None:
        parent.left = child_root.left
    else:
        while child_root.right is not None:
            parent = child_root
            child_root = child_root.right
        parent.right = child_root.left
    return child_root


def find_leaf_node_in_right(parent):
    child_root = parent.right
    if child_root.left is None:
        parent.right = child_root.right
    else:
        while child_root.left is not None:
            parent = child_root
            child_root = child_root.left
        parent.left = child_root.right
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
        return init_root
    if remove_node.left is not None:
        leaf_node = find_leaf_node_in_left(remove_node)
        remove_node.value = leaf_node.value
    elif remove_node.right is not None:
        leaf_node = find_leaf_node_in_right(remove_node)
        remove_node.value = leaf_node.value
    else:
        if parent_remove_node is None:
            return None
        else:
            direction = 'left' if parent_remove_node.left == remove_node else 'right'
            setattr(parent_remove_node, direction, None)
            return init_root
    restore_BST(leaf_node)

    return init_root
