from typing import List, Dict



def get_min(old: int, new1: int, new2: int) -> int:
    if new1 == -1 or new2 == -1:
        return old
    elif old == -1:
        return new1 + new2
    else:
        return min(old, new1 + new2)


def get_min2(old: int, new: int) -> int:
    if new == -1:
        new = float('inf')
    elif old == -1:
        old = float('inf')
    return min(old, new)



def create_distance_matrix(vertex_count: int, bridges: List[List[int]]) -> Dict[int, Dict[int, int]]:
    distance_matrix = [[0 if i == j else -1 for i in range(vertex_count)] for j in range(vertex_count)]
    for src, dst, distance in bridges:
        distance_matrix[src - 1][dst - 1] = get_min2(distance, distance_matrix[src-1][dst-1])
        distance_matrix[dst - 1][src - 1] = get_min2(distance, distance_matrix[dst-1][src-1])
    return distance_matrix


def read_edges(edges_count: int) -> List[List[int]]:
    edges = []
    for _ in range(edges_count):
        edges.append([int(x) for x in input().split()])
    return edges


def floyd_yorshell(distances: Dict[int, Dict[int, int]], vertex_count: int) -> None:
    for k in range(vertex_count):
        for i in range(vertex_count):
            for j in range(vertex_count):
                distances[i][j] = get_min(distances[i][j], distances[i][k], distances[j][k])


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    edges = read_edges(e)
    distances = create_distance_matrix(v, edges)
    floyd_yorshell(distances, v)
    print('\n'.join([' '.join([str(line[x]) for x in range(v)]) for line in distances]))