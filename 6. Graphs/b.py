from typing import List


def construct_adjancency_matrix(edges: List[List[int]], vertex_count: int) -> List[List[int]]:
    result = [[0 for _ in range(vertex_count)] for _ in range(vertex_count)]
    for src_edge, dest_edge in edges:
        result[src_edge - 1][dest_edge - 1] = 1
    return result


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    result = {}
    edges = []
    for _ in range(e):
        edges.append([int(x) for x in input().split()])
    result = construct_adjancency_matrix(edges, v)
    for i in range(v):
        print(" ".join([str(x) for x in result[i]]))
