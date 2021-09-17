from typing import Tuple, List, Set


class Vertex:
    def __init__(self, value: int):
        self.value: int = value
        self.neighbourhoods: List[Vertex] = []

    def sort_neighbourhoods(self):
        self.neighbourhoods.sort(key=lambda x: -1 * x)


def collect_vertexes(vertex_count: int) -> Tuple[List[Vertex], Set[int]]:
    vertexes = [Vertex(x + 1) for x in range(vertex_count)]
    output_vertexes = set([x + 1 for x in range(vertex_count)])
    return vertexes, output_vertexes


def topology_sort(vertexes: List[Vertex], vertex_color: List[int], output_vertexes: List[int]) -> List[int]:
    topology = []
    for out in output_vertexes:
        vertex = vertexes[out - 1]
        stack = [vertex]
        while len(stack) > 0:
            vertex = stack.pop()
            if vertex_color[vertex.value - 1] == 0:
                vertex_color[vertex.value - 1] += 1
                stack.append(vertex)
                for neighbourhood in vertex.neighbourhoods:
                    if vertex_color[neighbourhood - 1] == 0:
                        stack.append(vertexes[neighbourhood - 1])
            elif vertex_color[vertex.value - 1] == 1:
                vertex_color[vertex.value - 1] += 1
                topology.append(vertex.value)
    return topology


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    vertexes, output_vertexes = collect_vertexes(v)
    for _ in range(e):
        src, dst = [int(x) for x in input().split()]
        vertex = vertexes[src - 1]
        vertex.neighbourhoods.append(dst)
        try:
            output_vertexes.remove(dst)
        except KeyError:
            pass
    for vertex in vertexes:
        vertex.sort_neighbourhoods()
    vertex_color = [0 for _ in range(v)]
    topology = topology_sort(vertexes, vertex_color, output_vertexes)
    print(' '.join([str(x) for x in topology.__reversed__()]))