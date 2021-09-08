"""
ID решения: 52761524

---ПРИНЦИП РАБОТЫ---
    Нужно удалить узел из бинарного дерева поиска сохранив его структуру,
    т.е. чтобы после удаления оно осталось бинарным деревом поиска. Сначала
    я ищу в дереве ноду, которую надо удалить, при этом возвращаю не только
    саму удаляемую ноду, но и ее родителя (если поиск ноды не привел к успеху,
    то просто возвращаю корень исходного дерева без изменений). После этого
    ищу ноду, которую поставлю на место удаляемой. Для этого если у этой ноды
    есть левое поддерово, то иду в него и ищу самый правый узел в нем, если есть
    только правое поддерево, то иду в него и нахожу самого левый узел. Функция
    поиска узла на замену помимо возврата найденной подходящей ноды так же
    редактирует ссылку на эту ноду у родителя (ставит туда или детей ноды, которая
    вщята на замену, или 'зануляет' ее. После этого, чтобы не менять ссылки
    на узлы в поддереве в котором произошло удаление ноды, я ставлю в ноду, которую
    надо удалить значение из ноды найденной на замену и просто спускаюсь
    по дереву вниз и так же меняю значения нод, чтобы сохранить свойства
    бинарного дерева поиска

---ВРЕМЕННАЯ СЛОЖНОСТЬ---
    В алгоритме нам требуется O(h) времени чтобы найти элемент, который
    требуется удалить, где h - высота дерева. Затем так же O(h) времени
    чтобы найти ноду на замену удаляемой. O(1) на смену у удаляемой ноды
    значения и O(h) для просеивания вниз от удаленной ноды для восстановления
    свойств бинарного дерева поиска

---ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ---
    Дополнительная память нужна только для хранения входящих данных в виде
    бинарного дерева (связанного списка где каждая нода может иметь максимум
    одного предка и макмимум двух потомков). Для этого требуется O(n) дополнительной
    памяти, где n - количество элементов
"""

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


def test():
    node1 = Node(None, None, 932)
    node2 = Node(None, node1, 912)
    node3 = Node(None, None, 822)
    node4 = Node(node3, node2, 870)
    node5 = Node(None, None, 701)
    node6 = Node(node5, node4, 702)
    node7 = Node(None, None, 266)
    node8 = Node(None, node7, 191)
    node9 = Node(node8, None, 298)
    node10 = Node(node9, node6, 668)
    newHead = remove(node10, 545)
    assert newHead.value == 1
    assert newHead.right is node3
    assert newHead.right.value == 2


if __name__ == '__main__':
    test()