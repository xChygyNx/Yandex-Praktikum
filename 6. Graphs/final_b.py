from typing import List, Set


def read_paths(paths: List[List[int]], n_cities: int) -> None:
    for i in range(n_cities - 1):
        routes = input()
        for j, route in enumerate(routes):
            if route == 'R':
                paths[i].append(i + j + 1)
            elif route == 'B':
                paths[i + j + 1].append(i)


def exist_cycle(adjancency_list: List[List[int]], init_vertex: int, vertex_color: List[int]) -> bool:
    stack = [init_vertex]
    while len(stack) > 0:
        vertex = stack.pop()
        if vertex_color[vertex] == 0:
            vertex_color[vertex] += 1
            stack.append(vertex)
            for neighbourhood in adjancency_list[vertex]:
                if vertex_color[neighbourhood] == 0:
                    stack.append(neighbourhood)
                elif vertex_color[neighbourhood] == 1:
                    return True
        elif vertex_color[vertex] == 1:
            vertex_color[vertex] += 1
    return False


def get_init_vertex(vertex_color: List[int]) -> int:
    for vertex, color in enumerate(vertex_color):
        if color == 0:
            yield vertex



def check_paths(n_vertex: int, paths: List[List[int]]) -> None:
    vertex_color = [0 for _ in range(n_vertex)]
    for init_vertex in get_init_vertex(vertex_color):
        if exist_cycle(paths, init_vertex, vertex_color):
            print('NO')
            return
    print('YES')


if __name__ == '__main__':
    n_cities = int(input())
    paths = [[] for _ in range(n_cities)]
    read_paths(paths, n_cities)
    check_paths(n_cities, paths)