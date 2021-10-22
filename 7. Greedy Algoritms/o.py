from typing import Tuple, List, Dict
from copy import copy


MOD = 10 ** 9 + 7


class Stack:
    def __init__(self):
        self.store = []

    def add(self, vertex: int):
        self.store.append(vertex)

    def pop(self):
        return self.store.pop()

    def is_empty(self):
        return len(self.store) == 0


def read_edges(e: int) -> List[Tuple[int, int]]:
    edges = []
    for _ in range(e):
        src, dst = [int(x) for x in input().split()]
        edges.append((src, dst))
    return edges


def define_srcs(edges: List[Tuple[int, int]]) -> Dict[int, List[int]]:
    srcs = {}
    for edge in edges:
        try:
            vertex_srcs = srcs[edge[1]]
        except KeyError:
            srcs[edge[1]] = []
            vertex_srcs = srcs[edge[1]]
        vertex_srcs.append(edge[0])
    return srcs


def define_paths_count(v: int, start: int, finish: int, srcs: Dict[int, List[int]]) -> int:
    result = [0 for _ in range(v)]
    result[start-1] = 1
    color = copy(result)
    stack = Stack()
    stack.add(finish)
    while not stack.is_empty():
        current_vertex = stack.pop()
        if color[current_vertex-1] == 0:
            color[current_vertex-1] += 1
            stack.add(current_vertex)
            for src in srcs.get(current_vertex, []):
                stack.add(src)
        elif color[current_vertex-1] == 1:
            color[current_vertex-1] = 2
            for src in srcs.get(current_vertex, []):
                result[current_vertex-1] += result[src-1]
                result[current_vertex-1] %= MOD
    answer = result[finish-1] if result[start-1] != 0 else 0
    return answer


def count_paths(v: int, start: int, finish: int, edges: List[Tuple[int, int]]) -> int:
    srcs = define_srcs(edges)
    paths_count = define_paths_count(v, start, finish, srcs)
    return paths_count


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    edges = read_edges(e)
    start, finish = [int(x) for x in input().split()]
    paths = count_paths(v, start, finish, edges)
    print(paths)
