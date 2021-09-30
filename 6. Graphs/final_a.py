"""
ID решения: 53670332

---ПРИНЦИП РАБОТЫ---

    Переданные пути парсятся и сохраняются в списке смежности (так как в графе присутствуют
    мультиребра с разными весами, то в матрице сохраняется максимальный вес). После сохранения
    всех ребер начинается построение максимального остовного дерева. Обход графа начинается
    с первой вершины. Создается множество с невстреченными вершинами, чтобы не смотреть уже
    просмотренные вершины. Также создается пул, где хранятся непросмотренные ребра, идущие от
    уже посещенных вершин. Пул представляет из себя максимальную очередь с
    приоритетом, там хранятся кортежи, первое значение которых это расстояние между вершинами
    умноженное на -1 для выполнения функцтонала максимальной кучи, так как heapq строит минимальную
    кучу, второй и третьи значения кортежа - это начальная и конечная вершина, нужны для
    того, чтобы удалять уже использованные ребра из списка смежности.
    Перед началом работы алгоритма в пул закидываются все ребра идущие из первой вершины.
    Пока есть непосещенные вершины, берется следующий кортеж из пула. Проверяется, есть ли
    конечная вершина во множестве непосещенных вершин. Если есть, то вешина удаляется из
    множества, ребро удаляется из списка смежности, после чего все ребра
    из конечной вершины закидываются в пул. Вес ребра плюсуется к кумулятивной сумме ребер
    которая является общей длиной ребер остовного дерева. Шаг повторяется.
    Если до опустения множества непосещенных вершин опустеет пул, то это значит что граф не
    связный и остовное дерево из него построить нельзя.
    Если множество непосещенных вершин пуста, то выводится собранная сумма длин ребер остовного
    дерева.

---ВРЕМЕННАЯ СЛОЖНОСТЬ---
    Построение списка смежности занимает O(2е), где е - количество ребер, умноженное на 2 потому
    что в список смежности ребро заносится 2 раза (из каждой из 2 вершин). На вставку
    и забор элемента из кучи тратится по O(log n) времени, для n элементов O(n * log n).
    Построение множества непосещенных вершин надо  O(n), для нахождения в нем элемента и
    удаления элемента из него тратится O(1) времени. Общая временная сложность составляет
    O(n * log n)

---ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ---
    писок смежности занимает O(n * 2е), где n - количество вершин, е - среднее количество ребер,
    выходящих из вершин графа, 2 потому что кождое ребро сохраняется в обоих вершинах, которые
    оно соединяет. Множество непосещенных
    вершин - это еще O(n-1) дополнительной памяти (первая вершина не добавляется). Пул
    вершин в случае полного графа потребует O((n^2) / 2) дополнительной памяти.
    Итоговая пространственная сложность будет O(n * e)
"""

from typing import Set
from typing import Dict, Tuple
import heapq


class MaxPriorityQueue:
    def __init__(self):
        self.queue = []

    def get(self) -> Tuple[int, int, int]:
        info = heapq.heappop(self.queue)
        return -1 * info[0], info[1], info[2]

    def put(self, distance: int, src_vertex: int, dst_vertex: int):
        heapq.heappush(self.queue, (-1 * distance, src_vertex, dst_vertex))

    def extend(self, edges: Dict[int, int], src_vertex: int, unvisit_vertexes: Set[int]):
        for next_vertex, distance in edges.items():
            if next_vertex in unvisit_vertexes:
                self.put(distance, src_vertex, next_vertex)


def read_edges(n_vertex: int, n_edge: int) -> Dict[int, Dict[int, int]]:
    result = dict([(x + 1, {}) for x in range(n_vertex)])
    for _ in range(n_edge):
        src, dst, distance = [int(x) for x in input().split()]
        value = max(distance, result.get(src, {}).get(dst, 0))
        result[src][dst] = value
        result[dst][src] = value
    return result


def find_max_path(edges: Dict[int, Dict[int, int]], unvisit_vertexes: Set[int]) -> int:
    path_length = 0
    pool = MaxPriorityQueue()
    pool.extend(edges[1], 1, unvisit_vertexes)
    while len(unvisit_vertexes) != 0:
        try:
            while True:
                distance, src_vertex, dst_vertex = pool.get()
                if dst_vertex in unvisit_vertexes:
                    path_length += distance
                    unvisit_vertexes.remove(dst_vertex)
                    try:
                        edges[src_vertex].pop(dst_vertex)
                    except KeyError:
                        pass
                    try:
                        edges[dst_vertex].pop(src_vertex)
                    except KeyError:
                        pass
                    pool.extend(edges.get(dst_vertex, {}), src_vertex, unvisit_vertexes)
                    break
        except IndexError:
            break
    return path_length


if __name__ == '__main__':
    v, e = [int(x) for x in input().split()]
    edges = read_edges(v, e)
    unvisit_vertexes = set([x for x in range(2, v+1)])
    max_distance = find_max_path(edges, unvisit_vertexes)
    print(max_distance if len(unvisit_vertexes) == 0 else 'Oops! I did it again')