from typing import List, Dict


class Vertex:
    def __init__(self, value: int):
        self.neighbourhoods = []
        self.value = value

    def add_neighbourhood(self, elem: int) -> None:
        if elem not in self.neighbourhoods:
            self.neighbourhoods.append(elem)


class Stack:
    def __init__(self):
        self.store = []

    def add(self, vertex: int):
        self.store.append(vertex)

    def pop(self):
        return self.store.pop()


def collect_adjancency_dict(edges: List[List[int]]) -> Dict[int, Vertex]:
    result = {}
    for src_vertex, dest_vertex in edges:
        vertex1 = result.get(src_vertex, Vertex(src_vertex))
        vertex2 = result.get(dest_vertex, Vertex(dest_vertex))
        vertex1.add_neighbourhood(dest_vertex)
        vertex2.add_neighbourhood(src_vertex)
        result[src_vertex] = vertex1
        result[dest_vertex] = vertex2
    return result


def dfs(init_vertex: Vertex, result: List[int], vertex_color: List[int], vertexes: Dict[int, Vertex]) -> None:
    stack = Stack()
    stack.add(init_vertex.value)
    while len(stack.store) > 0:
        vertex = vertexes[stack.pop()]
        if vertex_color[vertex.value - 1] == 0:
            result.append(vertex.value)
            vertex_color[vertex.value - 1] += 1
            stack.add(vertex.value)
            for neighbourhood in vertex.neighbourhoods:
                if vertex_color[neighbourhood - 1] == 0:
                    stack.add(neighbourhood)
        elif vertex_color[vertex.value - 1] == 1:
            vertex_color[vertex.value - 1] += 1



if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    result = {}
    edges = []
    for _ in range(e):
        edges.append([int(x) for x in input().split()])
    result = collect_adjancency_dict(edges)
    init_vertex = result.get(int(input()))
    vertex_color = [0 for _ in range(v)]
    print_result = []
    dfs(init_vertex, print_result, vertex_color, result)
    print(' '.join([str(x) for x in print_result]))

