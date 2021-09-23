"""
ID решения: 53408475

---ПРИНЦИП РАБОТЫ---

    Переданные пути сохраняются в виде ориентированного графа в виде списка смежности.
    У нас все пути даются от "меньшего" города к "большему", но я в списке смежности
    пути R так и записываю, а для путей В записываю в обратную сторону, от "большего"
    города к "меньшему". Получается направленный граф и решение задачи сводится к поиску
    цикла в этом графе. Циклы я ищу с помощью итеративного поиска в глубину. При просмотре
    "соседей" очередной вершины я проверяю "цвет" вершины, если она серая, то есть она
    находится в процессе просмотра ее потомков, то значит в графе имеется цикл.

---ВРЕМЕННАЯ СЛОЖНОСТЬ---
    Обход всех вершин занимает O(n) времени, еще в каждой вершине просматривается каждый
    "сосед", что занимает еще O(e) времени. В сумме получаем временную сложность O(n*e)

---ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ---
    У нас имеются следующие вспомогательные структуры:
    Список смежности - O(n * e) дополнительной памяти, где n - количество вершин,
    а e - среднее количество соседей у каждой вершины,
    Пул вершин, где мы храним данные о вершинах, использующиеся для построения
    максимального остовного дерева. В процессе обхода так же разрастается до O((n - 1) * e)
    (n - 1, потому что мы в процессе обхода удаляем данные об использованных гранях,
    Множкство не посещенных вершин размером O(n)
    Итоговая пространственная сложность O((n*e) + ((n-1) * e) + n) -> O(n * e)
"""

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