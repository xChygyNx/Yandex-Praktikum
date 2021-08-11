'''
ID решения: 52242729

--- ПРИНЦИП РАБОТЫ ---
    Класс Stack представляет собой реализацию стека на списке (пайтоновский list,
    а не двусвязный список). При создании стека создается пустой список, где будут хранится
    добавляемые элементы. Стек содержит номер индекса последнего элемента в списке
    (атрибут tail), с помощью которого вставка и извлечение элементов по принципу
    FILO осуществляется за О(1)

--- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
    Вставка и извлечение элемента происходит за О(1), так как у нас хранится индекс конца
    списка

--- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
    Пространственная сложность алгоритма составляет О(n), так как элементы (причем не все,
    только числа, математические операции выполняются сразу и нигде не сохраняются) хранятся в
    списке без каких-либо дополнительных метаданных
'''


from typing import List, Tuple
import operator


OPERATIONS = '+', '-', '*', '/'


class Stack:
    def __init__(self):
        self.nums = []

    def push(self, value: int) -> None:
        self.nums.append(value)

    def pop(self) -> int:
        return self.nums.pop()


def get_nums(stack: Stack) -> Tuple[int, int]:
    b = stack.nums.pop()
    a = stack.nums.pop()
    return a, b


operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}


def solve(exp: List[str]) -> int:
    stack = Stack()
    for elem in exp:
        if elem in OPERATIONS:
            a, b = get_nums(stack)
            operation = operations.get(elem)
            result = operation(a, b)
            stack.push(result)
        else:
            stack.push(int(elem))
    return stack.pop()


if __name__ == '__main__':
    expression = input().strip().split()
    print(solve(expression))