from functools import reduce
from typing import List, Union


def get_elem(dictionary: dict, keys: List[int]) -> Union[int, float]:
    try:
        result = reduce(lambda x, y: x[y], keys, dictionary)
    except KeyError:
        result = float('inf')
    return result


class BFS:
    def __init__(self, vertex_count: int):
        self.distances = {}
        self.vertex_count = vertex_count

    def define_adjencency_list(self, edge_count: int):
        self.distances = dict([(i, {i: 0}) for i in range(1, self.vertex_count + 1)])
        for _ in range(edge_count):
            i, j = ([int(x) for x in input().split()])
            self.distances[i][j] = 1
            self.distances[j][i] = 1

    def define_distance(self):
        for k in range(1, self.vertex_count + 1):
            for i in range(1, self.vertex_count + 1):
                for j in range(1, self.vertex_count + 1):
                    old = get_elem(self.distances, [i, j])
                    new = get_elem(self.distances, [i, k]) + get_elem(self.distances, [j, k])
                    path = min(old, new)
                    if path != float('inf'):
                        self.distances[i][j] = path
                        self.distances[j][i] = path


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    bfs = BFS(v)
    bfs.define_adjencency_list(e)
    src_vertex, dst_vertex = map(int, input().split())
    bfs.define_distance()
    try:
        print(bfs.distances[src_vertex][dst_vertex])
    except KeyError:
        print(-1)

