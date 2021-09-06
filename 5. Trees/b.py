from math import fabs

# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


class SubTree:
    def __init__(self, error=False, height=0):
        self.height = height
        self.error = error

    def compare(self, other):
        if self.error or other.error:
            return SubTree(error=True)
        dif = int(fabs(self.height - other.height))
        if dif > 1:
            return SubTree(error=True)
        return SubTree(error=False, height=max(self.height, other.height) + 1)


def define_height_subtrees(root):
    if root is None:
        return SubTree(height=0)
    if root.left is None and root.right is None:
        return SubTree(height=1)
    left_subtree = define_height_subtrees(root.left)
    right_subtree = define_height_subtrees(root.right)
    self_tree = left_subtree.compare(right_subtree)
    return self_tree


def solution(root):
    result = define_height_subtrees(root)
    return not result.error



def test():
    node1 = Node(1)
    node0 = Node(0, right=node1)
    answer = solution(node0)
    print(answer)

if __name__ == '__main__':
    test()