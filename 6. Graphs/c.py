from typing import List


class Stack:
    def __init__(self):
        self.store = []

    def add(self, vertex: int):
        self.store.append(vertex)

    def pop(self):
        return self.store.pop()


def dfs(init_vertex, result: List[int], vertex_color: List[int], adj_list: List[List[int]]) -> None:
    stack = Stack()
    stack.add(init_vertex)
    while len(stack.store) > 0:
        vertex = stack.pop()
        if vertex_color[vertex - 1] == 0:
            result.append(vertex)
            vertex_color[vertex - 1] += 1
            stack.add(vertex)
            for v in adj_list[vertex - 1]:
                if vertex_color[v - 1] == 0:
                    stack.add(v)
        elif vertex_color[vertex - 1] == 1:
            vertex_color[vertex - 1] += 1


def create_list(vertex_count: int) -> List[List[int]]:
    lst = [[] for _ in range(vertex_count)]
    return lst


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    edges = []
    adjancency_list = create_list(v)
    for _ in range(e):
        i, j = ([int(x) for x in input().split()])
        adjancency_list[i-1].append(j)
        adjancency_list[j-1].append(i)
    for lst in adjancency_list:
        lst.sort(reverse=True)
    init_vertex = int(input())
    vertex_color = [0 for _ in range(v)]
    print_result = []
    dfs(init_vertex, print_result, vertex_color, adjancency_list)
    print(' '.join([str(x) for x in print_result]))

