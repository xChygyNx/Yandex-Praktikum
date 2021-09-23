from typing import List, Set, Tuple


def get_full_graph(n_vertex: int) -> List[int]:
    return [0 for _ in range(n_vertex)]


def write_adjecency(graph: List[int], edges: Set[Tuple[int]]) -> None:
    for edge in edges:
        graph[edge[0]-1] += 1
        graph[edge[1]-1] += 1



def check_full_graph(graph: List[int], n_vertex: int) -> bool:
    for n_neigbourhoods in graph:
        if n_neigbourhoods != n_vertex - 1:
            return False
    return True


def read_edges(n_edges: int) -> Set[Tuple[int]]:
    edges = set()
    for _ in range(n_edges):
        v1, v2 = [int(x) for x in input().split()]
        if v1 != v2:
            src, dst = min(v1, v2), max(v1, v2)
            edges.add((src, dst))
    return edges


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    graph = get_full_graph(v)
    edges = read_edges(e)
    write_adjecency(graph, edges)
    print('YES' if check_full_graph(graph, v) else 'NO')