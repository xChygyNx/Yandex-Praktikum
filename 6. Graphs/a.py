from typing import List


def collect_adjancency_list(edges: List[List[int]], vertex_count: int) -> List[List[int]]:
    result = [[] for _ in range(vertex_count + 1)]
    for src_edge, dest_edge in edges:
        result[src_edge].append(dest_edge)
    return result


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    result = {}
    edges = []
    for _ in range(e):
        edges.append([int(x) for x in input().split()])
    result = collect_adjancency_list(edges, v)
    for i in range(1, v + 1):
        result[i].sort()
        print(f'{len(result[i])} {" ".join([str(x) for x in result[i]])}')
