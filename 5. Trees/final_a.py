"""
ID решения: 52799721

---ПРИНЦИП РАБОТЫ---

    Для хранения элементов по принципу минимальной кучи создается экземпляр класса
    Heap, в котором прописаны методы добавления и изъятия минимального значения
    с сохранением структуры кучи. У класса есть хранилище, где в определенном
    порядке хранятся элементы (обычный список).
    При вставке элемента инкрементируется размер хранилища, в конец списка
    вставляется элемент и для последнего элемента осуществляется просеивание
    вверх, чтобы он занял соответствующую его величине почицию в куче.
    При изъятии элемента из кучи, сначала проверяем, если в хранилище лежит только
    один элемент, то просто удаляем его и возвращаем предварительно сохраненный
    первый элемент. Если больше одного элемента, то берется первый
    элемент из хранилища (там всегда лежит минимальный элемент), на его позицию
    встает последний элемент в хранилище, и для него осуществляется просеивание
    вниз.
    Элементы хранятся в виде кортежей, где первый элемент - это количество решенных
    задач помноженное на -1, второй элемент - штраф участника, третий - его имя.
    Хранение элементов в таком виде обусловлено тем, что так их удобно сравнивать
    между собой.

---ВРЕМЕННАЯ СЛОЖНОСТЬ---
    Вставка элемента в конец списка занимает О(1) времени, просеивание кучи вверх
    равняется O(h), где h - высота кучи, или O(log n), где n - количество
    элементов.
    То же самое касается и изъятия элемента - сам забор минимального элемента - это
    O(1) времени, так как мы знаем его позицию в списке, вставка последнего элемента
    в начало списка еще O(1), и просеивание вниз так же занимает O(h), или
    O(log n).
    В обоих случаях временная сложность действия составляет O(log n)

---ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ---
    Дополнительная память нужна только для хранения входящих данны в списке
    размером O(n), где n - количество элементов
"""
from typing import Tuple


class Heap:
    def __init__(self):
        self.store = []

    def add(self, value: Tuple[int, int, str]):
        self.store.append(value)
        self.sift_up()

    def pop(self) -> Tuple[int, int, str]:
        answer = self.store[0]
        if len(self.store) > 1:
            self.store[0] = self.store.pop()
            self.sift_down()
        else:
            self.store.pop()
        return answer

    def sift_up(self):
        idx = len(self.store) - 1
        while True:
            if idx == 0:
                break
            if self.store[idx] >= self.store[(idx - 1) // 2]:
                break
            self.store[idx], self.store[(idx - 1) // 2] = self.store[(idx - 1) // 2], self.store[idx]
            idx = (idx - 1) // 2

    def get_idx_min_elem(self, idx) -> int:
        if self.store[idx * 2 + 1] < self.store[idx * 2 + 2]:
            return idx * 2 + 1
        return idx * 2 + 2

    def sift_down(self):
        idx = 0
        while True:
            try:
                left_child = self.store[idx * 2 + 1]
            except IndexError:
                break
            try:
                right_child = self.store[idx * 2 + 2]
            except IndexError:
                right_child = None
            if right_child is None:
                new_idx = idx * 2 + 1
            else:
                new_idx = self.get_idx_min_elem(idx)
            if self.store[idx] <= self.store[new_idx]:
                break
            self.store[idx], self.store[new_idx] = self.store[new_idx], self.store[idx]
            idx = new_idx



def construct_heap() -> Heap:
    n = int(input())
    result = Heap()
    for _ in range(n):
        data = input().split()
        elem = -1 * int(data[1]), int(data[2]), data[0]
        result.add(elem)
    return result



if __name__ == '__main__':
    min_heap = construct_heap()
    result = []
    while len(min_heap.store) > 0:
        result.append(min_heap.pop()[2])
    print('\n'.join(result))