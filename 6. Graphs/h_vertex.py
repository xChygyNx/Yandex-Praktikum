from typing import Dict, List


class Vertex:
    def __init__(self, value: int):
        self.entry: int = None
        self.exit: int = None
        self.value: int = value
        self.neighbourhoods: List[Vertex] = []

    def sort_neighbourhoods(self):
        self.neighbourhoods.sort(key=lambda x: -1 * x)


def collect_vertexes(vertex_count: int) ->List[Vertex]:
    result = [None for _ in range(vertex_count)]
    for i in range(1, vertex_count + 1):
        result[i - 1] = Vertex(i)
    return result


def dfs_entry(vertexes: List[Vertex], vertex_color: List[int]) -> None:
    time = -1
    stack = [vertexes[0]]
    while len(stack) > 0:
        vertex = stack.pop()
        if vertex_color[vertex.value - 1] == 0:
            vertex_color[vertex.value - 1] += 1
            time += 1
            vertex.entry = time
            stack.append(vertex)
            for neighbourhood in vertex.neighbourhoods:
                if vertex_color[neighbourhood - 1] == 0:
                    stack.append(vertexes[neighbourhood - 1])
        elif vertex_color[vertex.value - 1] == 1:
            vertex_color[vertex.value - 1] += 1
            time += 1
            vertex.exit = time


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    vertexes = collect_vertexes(v)
    for _ in range(e):
        src, dst = [int(x) for x in input().split()]
        vertex = vertexes[src - 1]
        vertex.neighbourhoods.append(dst)
    for vertex in vertexes:
        vertex.sort_neighbourhoods()
    vertex_color = [0 for _ in range(v)]
    dfs_entry(vertexes, vertex_color)
    for elem in vertexes:
        print(f'{elem.entry} {elem.exit}')