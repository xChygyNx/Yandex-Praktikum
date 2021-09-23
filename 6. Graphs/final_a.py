from typing import Dict, Set


def read_edges(n_vertex: int, n_edge: int) -> Dict[int, Dict[int, int]]:
    result = dict([(x + 1, {}) for x in range(n_vertex)])
    for _ in range(n_edge):
        src, dst, distance = [int(x) for x in input().split()]
        result[src][dst] = max(distance, result.get(src, {}).get(dst, 0))
        result[dst][src] = max(distance, result.get(dst, {}).get(src, 0))
    return result


def find_max_path(edges: Dict[int, Dict[int, int]], unvisit_vertexes: Set[int]) -> int:
    path_length = 0
    current_vertex = 1
    pool = {}
    pool[current_vertex] = edges[current_vertex]
    while len(unvisit_vertexes) != 0:
        max_distance = 0
        for current_vertex, neighbourhoods in pool.items():
            for next_vertex, distance in pool[current_vertex].items():
                if next_vertex in unvisit_vertexes and distance > max_distance:
                    max_distance = distance
                    far_vertex = next_vertex
                    src_vertex = current_vertex
        if max_distance > 0:
            path_length += max_distance
            unvisit_vertexes.remove(far_vertex)
            pool[far_vertex] = edges[far_vertex]
            edges[src_vertex].pop(far_vertex)
            edges[far_vertex].pop(src_vertex)
        else:
            break
    return path_length


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    edges = read_edges(v, e)
    unvisit_vertexes = set([x for x in range(2, v+1)])
    max_distance = find_max_path(edges, unvisit_vertexes)
    print(max_distance if len(unvisit_vertexes) == 0 else 'Oops! I did it again')