class Queue:
    def __init__(self):
        self.store = []
        self.pos = 0
        self.init_vertex = None

    def add(self, vertex: int):
        self.store.append(vertex)

    def get(self):
        elem = self.store[self.pos]
        self.pos += 1
        return elem

    def __iter__(self):
        self.store = [self.init_vertex]
        return self

    def __next__(self):
        while len(self.store) > self.pos:
            return self.get()
        else:
            raise StopIteration


class BFS:
    def __init__(self, vertex_count: int):
        self.adjencency_lst = []
        self.queue = Queue()
        self.vertex_count = vertex_count
        self.component_lst = [None for _ in range(vertex_count)]
        self.unvisit_vertex = set([x+1 for x in range(vertex_count)])

    def define_adjencency_list(self, edge_count: int):
        self.adjencency_lst = [[] for _ in range(self.vertex_count)]
        for _ in range(edge_count):
            i, j = ([int(x) for x in input().split()])
            self.adjencency_lst[i - 1].append(j)
            self.adjencency_lst[j - 1].append(i)

    def get_init_vertex(self):
        for i in range(len(self.component_lst)):
            if self.component_lst[i] is None:
                self.component_lst[i] = 1
                return i + 1

    def run(self) -> bool:
        not_in_queue = set([x + 1 for x in range(self.vertex_count)])
        self.queue.init_vertex = self.get_init_vertex()
        for vertex in self.queue:
            for v in self.adjencency_lst[vertex - 1]:
                if self.component_lst[v-1] is None:
                    self.component_lst[v-1] = (self.component_lst[vertex-1] + 1) % 2
                elif self.component_lst[v - 1] == self.component_lst[vertex-1]:
                    return False
                if v in not_in_queue:
                    self.queue.add(v)
                    not_in_queue.remove(v)
        return True


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    bfs = BFS(v)
    bfs.define_adjencency_list(e)
    print('YES' if bfs.run() else 'NO')

