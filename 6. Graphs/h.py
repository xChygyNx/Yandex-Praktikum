from typing import List, Dict


def create_list(vertex_count: int) -> List[List[int]]:
    lst = [[] for _ in range(vertex_count)]
    return lst


def dfs_entry(adjancency_list: Dict[int, List[int]], entry_list: List[List[int]], vertex_color: List[int]) -> None:
    time = -1
    stack = [1]
    while len(stack) > 0:
        vertex = stack.pop()
        if vertex_color[vertex - 1] == 0:
            vertex_color[vertex - 1] += 1
            time += 1
            entry_list[vertex - 1].append(time)
            stack.append(vertex)
            for neighbourhood in adjancency_list.get(vertex, []):
                if vertex_color[neighbourhood - 1] == 0:
                    stack.append(neighbourhood)
        elif vertex_color[vertex - 1] == 1:
            vertex_color[vertex - 1] += 1
            time += 1
            entry_list[vertex - 1].append(time)


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    adjancency_list = {}
    entry_list = [[] for _ in range(v)]
    for _ in range(e):
        edges = input().split()
        i, j = int(edges[0]), int(edges[1])
        adjancency_list[i] = adjancency_list.get(i, [])
        adjancency_list[i].append(j)
    for lst in adjancency_list.values():
        lst.sort(reverse=True)
    vertex_color = [0 for _ in range(v)]
    dfs_entry(adjancency_list, entry_list, vertex_color)
    print_lst = '\n'.join([f'{line[0]} {line[1]}' for line in entry_list])
    print(print_lst)