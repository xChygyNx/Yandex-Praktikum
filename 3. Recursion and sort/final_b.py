'''
ID решения: 52328264


--- ПРИНЦИП РАБОТЫ ---
    После считывания входных данных мы получаем список именнованных кортежей, сформированных
    так, чтобы они по умолчанию сравнивались как нам надо, т.е. сначала идет количество решенных
    задач, помноженное на -1 (чтобы при сортировке по возрастанию сначала шли те, кто решил
    большее количество задач), потом идет штраф (без изменений) и потом имя участника. Этот
    список именованных кортежей на сортировку.
    Сортировка осуществляется in-place, т.е. элементы сортируются в списке путем замены  местами элементов
    в списке. Сначала выбираем опорный элемент, в моем случае берется первый элемент в списке. Затем
    создается 2 "указателя" (start и end), start на второй элемент, end - на последний элемент.
    После этого start передвигается вправо, пока не встанет на элемент меньший или равный опорному
    элементу, или пока не достигнет элемента на который указывает указатель end. Затем передвигается
    указатель end, он сдвигается влево пока не достигнет элемента меньшего чем опорный или того, на котором
    стоит указатель start. После этого если элемент на который указывает указатель start больше того,
    на который указывает указатель end, элементы в списке меняются местами. Если нет, то это
    подразумевает что указатели сошлись. Высчитывается коэффициент к, который определяет, куда
    будет вставлен опорный элемент - перед элементом на который указывает start (стандартный случай), или
    меняется местами с элементом на который указывает start (если опорный элемент оказался наибольшим на
    заданном участке списка). После того, как опорный элемент меняется местами с нужным элементом, рекурсивно по такому
    алгоритму сортируются подсписки который оказался до опорного элемента (там содержатся элементы меньше
    или равные опорному) и подсписок после опорного элемента (там содержатся элементы строго больше
    опорного элемента). Базовый случай этой рекурсии - списки длиной менее 2 элементов - они по
    умолчанию отсортированны и функция просто возвращается по стеку вызовов на уровень вверх.

--- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
    Временная сложность быстрой сортировеи в срерднем составляет O(n * log n). В худшем случае
    O(n^2).

--- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
    Пространственная сложность алгоритма составляет О(1), так как сортировка осуществляется
    перестановкой элементов внутри изначального списка без создания дополнительных структур данных
'''


from typing import NamedTuple, List


class Participant(NamedTuple):
    solved: int
    penalty: int
    name: str


def read_data() -> List[Participant]:
    n = int(input())
    result = [None] * n
    for i in range(n):
        data = input().split()
        participant = Participant(solved=-1*int(data[1]), penalty=int(data[2]), name=data[0])
        result[i] = participant
    return result


def sort_list(lst: list, start_ind: int, end_ind: int) -> None:
    length = end_ind - start_ind + 1
    if length <= 1:
        return
    pivot = lst[start_ind]
    start = start_ind + 1
    end = end_ind
    while start < end:
        while lst[start] <= pivot and start < end:
            start += 1
        while lst[end] >= pivot and end > start:
            end -= 1
        if lst[start] > pivot > lst[end]:
            lst[start], lst[end] = lst[end], lst[start]
    k = 1 if lst[start] > pivot else 0
    lst[start_ind], lst[start - k] = lst[start - k], lst[start_ind]
    sort_list(lst, start_ind, start-k-1)
    sort_list(lst, start+1-k, end_ind)



if __name__ == '__main__':
    participants = read_data()
    length = len(participants)
    sort_list(participants, 0, length - 1)
    for record in participants:
        print(record.name)
