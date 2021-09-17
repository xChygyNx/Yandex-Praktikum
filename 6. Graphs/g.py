from typing import Tuple


class Queue:
    def __init__(self):
        self.store = []
        self.pos = 0

    def add(self, vertex: Tuple[int]):
        self.store.append(vertex)

    def get(self):
        elem = self.store[self.pos]
        self.pos += 1
        return elem


class BFS:
    def __init__(self, vertex_count: int):
        self.adjencency_lst = []
        self.queue = Queue()
        self.vertex_count = vertex_count

    def define_adjencency_list(self, edge_count: int):
        self.adjencency_lst = [[] for _ in range(self.vertex_count)]
        for _ in range(edge_count):
            i, j = ([int(x) for x in input().split()])
            self.adjencency_lst[i - 1].append(j)
            self.adjencency_lst[j - 1].append(i)
        for lst in self.adjencency_lst:
            lst.sort()

    def define_distance(self, init_vertex: int) -> int:
        not_in_queue = set([x + 1 for x in range(self.vertex_count) if x+1 != init_vertex])
        self.queue.add((init_vertex, 0))
        max_distance = 0
        while len(self.queue.store) > self.queue.pos:
            vertex, distance = self.queue.get()
            distance += 1
            for v in self.adjencency_lst[vertex - 1]:
                if v in not_in_queue:
                    max_distance = distance
                    self.queue.add((v, distance))
                    not_in_queue.remove(v)
        return max_distance


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    bfs = BFS(v)
    bfs.define_adjencency_list(e)
    init_vertex = int(input())
    print(bfs.define_distance(init_vertex))
