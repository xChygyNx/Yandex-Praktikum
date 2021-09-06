"""
ID решения: 52610764

---ПРИНЦИП РАБОТЫ---

    Для хранения элементов по принципу минимальной кучи создается экземпляр класса
    Heap, в котором прописаны методы добавления и изъятия минимального значения
    с сохранением структуры кучи. У класса есть 2 атрибута: хранилище, где в определенном
    порядке хранятся элементы (обычный список) и текущий размер хранилища, чтобы при
    вставке и изъятии элемента не приходилось заново пересчитывать размер.
    При вставке элемента инкрементируется размер хранилища, в конец списка
    вставляется элемент и для последнего элемента осуществляется просеивание
    вверх, чтобы он занял соответствующую его величине почицию в куче.
    При изъятии элемента из кучи, размер уменьшается на единицу, берется первый
    элемент из хранилища (там всегда лежит минимальный элемент), на его позицию
    встает последний элемент в хранилище, и для него осуществляется просеивание
    вниз. Блок try except нужен для извлечения последнего элемента из хранилища,
    так как сначала происходит забор последнего элемента и потом его на место
    первого, при заборе последнего элемента получается что роль первого и последнего
    элемента исполняет один и тот же элемент, и после его удаления из хранилища
    мы удаляем и мемто куда его следует вставить.
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

---ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ---
    Дополнительная память нужна только для хранения входящих данны в списке
    размером O(n), где n - количество элементов
"""
from typing import Tuple


class Heap:
    def __init__(self):
        self.size = 0
        self.store = [None]

    def add(self, value: Tuple[int, int, str]):
        self.store.append(value)
        self.size += 1
        self.sift_up()

    def pop(self) -> Tuple[int, int, str]:
        self.size -= 1
        answer = self.store[1]
        try:
            self.store[1] = self.store.pop()
            self.sift_down()
        except IndexError:
            pass
        return answer

    def sift_up(self):
        idx = self.size
        while True:
            if idx == 1:
                break
            if self.store[idx] >= self.store[idx // 2]:
                break
            self.store[idx], self.store[idx // 2] = self.store[idx // 2], self.store[idx]
            idx //= 2

    def get_idx_min_elem(self, idx) -> int:
        if self.store[idx * 2] < self.store[idx * 2 + 1]:
            return idx * 2
        return idx * 2 + 1

    def sift_down(self):
        idx = 1
        while True:
            try:
                left_child = self.store[idx * 2]
            except IndexError:
                break
            try:
                right_child = self.store[idx * 2 + 1]
            except IndexError:
                right_child = None
            if right_child is None:
                new_idx = idx * 2
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
    while min_heap.size > 0:
        result.append(min_heap.pop()[2])
    print('\n'.join(result))