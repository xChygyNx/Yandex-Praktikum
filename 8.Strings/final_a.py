"""
ID решения: 56338508

---ПРИНЦИП РАБОТЫ---
    Сначала начинают считываться запакрванные строки, по одной считываются и сразу
    распаковываются по одной и сохраняются в список. Распаковка делается при помощи
    двух стеков: стека чисел и стека символов. Если попадается число, то оно добавляется
    в стек чисел, если открывающая скобка или символ, то в стек символов. Когда нам
    попадается закрывающая скобка, то мы изымаем элементы из стека символов пока не
    наткнемся на открывающую скобку, после чего из вынутых символов формируем строку,
    которую будем повторять то количество раз, которое получим из стека чисел, получившуюся
    строку кладем в стек символов. Так идем по конца запакованной строки и в конце возвращаем
    строку, которая является склейкой из элементов, хранящихся в стеке символов.
    И так, мы получили список распакованных строк, теперь приступаем к поиску общего
    префикса. Для начала отсортируем список полученных распакованных строк по длине строки.
    После этого берем в качестве эталона первое (самое короткое) слово из списка распакованных
    слов, его длину записываем в переменную max_prefix_len, которая обозначает, до какого символа
    надо сравнивать очередное слово из списка с эталоном. Затем начинаем идти по словам
    из списка, и посимвольно сравниваем очередное слово с эталоном с символа с индексом 0
    по символ с индексом max_prefix_len.  Kак только символы расходятся, или доходим до
    индекса max_prefix_len, то выхожу из цикла и
    перезаписываю переменную max_prefix_len. Получившийся после прохождения всех
    слов из списка max_prefix_len и есть длина общего для всех слов префикса.

---ВРЕМЕННАЯ СЛОЖНОСТЬ---
    Считывание всех запакованных строк занимает O(n) времени, где n - количество слов. Распаковка
    каждого слова занимает: добавление/взятие элемента в соответствующий стек происходит за O(1)
    времени, при наихудшем варианте (например когда запакованная стока находится полностью в скобках)
    каждый симво будет 1 раз добавлен и 1 раз вынут из стека, значит обработка целого слова будет
    занимать O(2m) времени, где m - количество символов в запакованном слове. Общее время получения
    распакованных строк из запакованных составит O(n * m) времени.
    Дальше приступаем к поиску общего префикса. В самом худшем случае (если общий префикс и первое
    распакованной слово будут полностью совпадать), его поиск займет O(n * k) времени, где k - длина
    первого распакованного слова.
    Общая временная сложность алгоритма составит O((n * m) + (n * k)) = O(n * (m + k))

---ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ---
    Для хранения распакованных строк понадобится список разменром O(n * l), где n - количество слов,
    a l - средняя длина этих слов.
    При распаковке слова необходимы 2 стека, сумма размеров которых составляем максимум O(m), где
    m - длина очередного слова. Так как для каждого слова переменные хранящие стеки перезаписываются,
    то при многократном распаковывании простанственная сложность не аккумулируется, а m будет равна
    длине самого длинного слова.
    При нахождении общего префикса дополнительная память не используется.
    Итоговая пространственная сложность алгоритма составит O(n * l + m)
"""


from typing import Union, List


class Stack:
    def __init__(self):
        self.store = []

    def add(self, elem: Union[int, str]) -> None:
        self.store.append(elem)

    def pop(self) -> Union[str, int]:
        return self.store.pop()

    def look(self) -> Union[str, int]:
        return self.store[-1]

    def __iter__(self):
        return iter(self.store)


def close_bracket(letter_stack: Stack, num_stack: Stack) -> None:
    elem = letter_stack.pop()
    tmp = []
    while elem != '[':
        tmp.append(elem)
        elem = letter_stack.pop()
    num = num_stack.pop()
    elem = ''.join(tmp.__reversed__())
    letter_stack.add(elem * num)


def unpack(packed_word: str) -> str:
    letter_stack = Stack()
    num_stack = Stack()
    for ch in packed_word:
        if ch.isdigit():
            num_stack.add(int(ch))
        else:
            if ch == ']':
                close_bracket(letter_stack, num_stack)
            else:
                letter_stack.add(ch)
    return ''.join([x for x in letter_stack])


def find_union_prefix(pw: List[str]) -> str:
    standard = pw[0]
    max_prefix_len = len(standard)
    for i in range(1, len(pw)):
        word = pw[i]
        cur_len = 0
        while cur_len < max_prefix_len and word[cur_len] == standard[cur_len]:
            cur_len += 1
        max_prefix_len = cur_len
    return standard[:max_prefix_len]


if __name__ == '__main__':
    n = int(input())
    pw = []
    for i in range(n):
        pw.append(unpack(input()))
    pw.sort(key=len)
    print(find_union_prefix(pw))
