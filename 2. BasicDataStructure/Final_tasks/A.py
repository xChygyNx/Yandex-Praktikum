'''
ID решения: 52243853

--- ПРИНЦИП РАБОТЫ ---
    Класс Deque представляет собой реализацию двусторонней очереди на 'закольцованном' списке (пайтоновский list,
    а не двусвязный список). При создании очереди указывается ее максимальный размер, по достижении
    которого попытка добавления нового элемента будет приводить к выдаче сообщения об ошибке.
    Также сообщение об ошибке будет выдаваться при попытке извлечения элемента из пустой
    очереди.
    Для закольцевания списка при добавлении и извлечения элемента пересчитываются указатели head и tail,
    причем при пересчитывании высчитанное значение делится по модулю на максимальный размер списка

--- ВРЕМЕННАЯ СЛОЖНОСТЬ ---
    Вставка и извлечение элемента из очереди происходит за О(1)

--- ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ ---
    Пространственная сложность алгоритма составляет О(n), так как элементы хранятся в
    списке без каких-либо дополнительных метаданных
'''
from typing import NamedTuple, List, Union, Optional


class Params(NamedTuple):
    n_cmd: int
    queue_size: int
    cmd: List[str]


class Deque:
    def __init__(self, max_size: int):
        self.store = [None] * max_size
        self.max_size = max_size
        self.head = 0
        self.tail = 0
        self.size = 0

    def push_front(self, value: int) -> Optional[str]:
        if self.size == self.max_size:
            return 'error'
        else:
            if self.size != 0:
                self.head = (self.head - 1) % self.max_size
            self.store[self.head] = value
            self.size += 1

    def push_back(self, value: int) -> Optional[str]:
        if self.size == self.max_size:
            return 'error'
        else:
            if self.size != 0:
                self.tail = (self.tail + 1) % self.max_size
            self.store[self.tail] = value
            self.size += 1

    def pop_front(self) -> Union[str, int]:
        if self.size == 0:
            return 'error'
        else:
            value = self.store[self.head]
            self.store[self.head] = None
            if self.size != 1:
                self.head = (self.head + 1) % self.max_size
            self.size -= 1
            return value

    def pop_back(self) -> Union[int, str]:
        if self.size == 0:
            return 'error'
        else:
            value = self.store[self.tail]
            self.store[self.tail] = None
            if self.size != 1:
                self.tail = (self.tail - 1) % self.max_size
            self.size -= 1
            return value


def create_deque(max_size: int) -> Deque:
    return Deque(max_size)


def print_result(value: List[Union[str, int, None]]) -> None:
    print('\n'.join([str(x) for x in value if x is not None]))


def execute_cmd(params: Params, deq: Deque) -> List[Union[str, int]]:
    output = []
    for cmd in params.cmd:
        if cmd.startswith('push'):
            cmd, value = cmd.split()
            value = int(value)
            if cmd == 'push_front':
                output.append(deq.push_front(value))
            elif cmd == 'push_back':
                output.append(deq.push_back(value))
        elif cmd.startswith('pop'):
            if cmd == 'pop_back':
                output.append(deq.pop_back())
            elif cmd == 'pop_front':
                output.append(deq.pop_front())
    return output


def read_params() -> Params:
    n_cmd = int(input())
    queue_size = int(input())
    cmd = []
    for _ in range(n_cmd):
        cmd.append(input())
    return Params(n_cmd=n_cmd, queue_size=queue_size, cmd=cmd)


if __name__ == '__main__':
    params = read_params()
    deq = create_deque(params.queue_size)
    output = execute_cmd(params, deq)
    print_result(output)
