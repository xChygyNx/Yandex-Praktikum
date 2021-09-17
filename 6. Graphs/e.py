from typing import List, Optional


class Stack:
    def __init__(self):
        self.store = []

    def add(self, vertex: int):
        self.store.append(vertex)

    def pop(self):
        return self.store.pop()


def dfs(init_vertex: int, component_lst: List[Optional[int]], adj_list: List[List[int]], component_num: int) -> List[int]:
    stack = Stack()
    stack.add(init_vertex)
    result = []
    while len(stack.store) > 0:
        vertex = stack.pop()
        if component_lst[vertex - 1] is None:
            result.append(vertex)
            component_lst[vertex - 1] = component_num
            stack.add(vertex)
            for v in adj_list[vertex - 1]:
                if component_lst[v - 1] is None:
                    stack.add(v)
    return result


def create_list(vertex_count: int) -> List[List[int]]:
    lst = [[] for _ in range(vertex_count)]
    return lst


def next_vertex(lst: List[Optional[int]]) -> int:
    for i in range(len(lst)):
        if lst[i] is None:
            yield i + 1


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    edges = []
    adjancency_list = create_list(v)
    for _ in range(e):
        i, j = ([int(x) for x in input().split()])
        adjancency_list[i-1].append(j)
        adjancency_list[j-1].append(i)
    component_list = [None for _ in range(v)]
    traversal_lst = []
    component = 0
    for init_vertex in next_vertex(component_list):
        if init_vertex is not None:
            component += 1
            elem = (dfs(init_vertex, component_list, adjancency_list, component))
            elem.sort()
            traversal_lst.append(elem)
        else:
            break
    print(len(traversal_lst))
    print('\n'.join([' '.join([str(x) for x in line]) for line in traversal_lst]))
