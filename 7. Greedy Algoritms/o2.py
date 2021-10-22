from typing import Tuple, List, Dict, Set
from queue import Queue


MOD = 10 ** 9 + 7


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


def define_dsts(edges: List[Tuple[int, int]]) -> Dict[int, Set[int]]:
    dsts = {}
    for edge in edges:
        try:
            vertex_dsts = dsts[edge[0]]
        except KeyError:
            dsts[edge[0]] = set()
            vertex_dsts = dsts[edge[0]]
        vertex_dsts.add(edge[1])
    return dsts


def define_paths_count(v: int, start: int, finish: int, srcs: Dict[int, List[int]], dsts: Dict[int, List[int]]) -> int:
    result = [0 for _ in range(v)]
    queue = Queue()
    result[start - 1] = 1
    queue.put(start)
    while not queue.empty():
        current_vertex = queue.get()
        for dst in dsts.get(current_vertex, []):
            queue.put(dst)
        for src in srcs.get(current_vertex, []):
            result[current_vertex - 1] = (result[current_vertex - 1] + result[src - 1]) % MOD
    return result[finish - 1]


def count_paths(v: int, start: int, finish: int, edges: List[Tuple[int, int]]) -> int:
    srcs = define_srcs(edges)
    dsts = define_dsts(edges)
    paths_count = define_paths_count(v, start, finish, srcs, dsts)
    return paths_count


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    edges = read_edges(e)
    start, finish = [int(x) for x in input().split()]
    paths = count_paths(v, start, finish, edges)
    print(paths)
