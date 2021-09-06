# Comment it before submitting
# class Node:
#     def __init__(self, value, left=None, right=None):
#         self.value = value
#         self.right = right
#         self.left = left


def collect_nums(root, nums, acum_value):
    acum_value = acum_value * 10 + root.value
    if root.left is None and root.right is None:
        nums.append(acum_value)
    else:
        if root.left is not None:
            collect_nums(root.left, nums, acum_value)
        if root.right is not None:
            collect_nums(root.right, nums, acum_value)



def solution(root) -> int:
    nums = []
    collect_nums(root, nums, 0)
    return sum(nums)


def test():
    node1 = Node(2, None, None)
    node2 = Node(1, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(2, None, None)
    node5 = Node(1, node4, node3)

    assert solution(node5) == 275

if __name__ == '__main__':
    test()