"""
ID решения: 52373151

---ПРИНЦИП РАБОТЫ---
    Сначала создается объект класса DB, в котором прописаны методы put, get и delete.
    Затем команды считываются с командной строки, и при помощи getattr вызывается нужный
    метод DB.
    Хранилище элементов представляем из себя массив, размерностью HASH_TABLE_SIZE (в данном
    конкретном решении взято число 9973, как наибольшее простое число меньше 10^5). Индекс
    массива, в который будет записан элемент, определяется как остаток от деления значения
    элемента на HASH_TABLE_SIZE. При созданиии объекта класса DB во всех ячейках хранилища
    лежит None. Коллизии решаются методом цепочек.
    Put - определяется индекс хранилища, где будет лежать информациия, путем получения остатка
    от деления id на HASH_TABLE_SIZE. Если в ячейке лежит None (раньще в эту ячейку ничего
    не записывалось), то создается нода с необходимой
    информацией и в ячейке хранилища сохраняется ссылка на эту ноду. Если же в ячейке уже
    есть ссылка на ноду (произошла коллизия), то мы идем по списку и ищем ноду с заданным
    id. Если нашли, то обновляем значение salary, если дошли до конца списка и не нашли
    ноду с таким id, то добавляем в конец списка ноду с заданныси id и salary
    Get - определяется индекс ячейки хранилища, где должна лежать информация. Если в ячейке
    находится ссылка на голову списка, то мы идем по списку в поиске заданного id. Если
    нашли, то возвразаем salary. Если в списке нет ноды с искомым id, или в ячейке вообще нет
    связного списка (лежит None). то возвращается None.
    Delete - пределяется индекс ячейки хранилища, где должна лежать информация. Если в ячейке
    находится ссылка на голову списка, то смотрим, совпадает ли id ноды с искомым. Если да,
    то сохраняем в ячейке хранилища ссылку на следующую ноду, в текущей ноде затираем ссылку
    из поля next и возвращаем salary удаленной ноды. Если нет, то идем по списку, пока id
    следующей от просматриваемой ноды не совпадет с искомой. В этом случае сохраняем следующую
    ноду во временную переменную, меняем ссылку поля next текущей ноды на ссылку из поля next
    ноды из временной переменной, затираем поле next временно сохраненной ноды и возвращаем
    значение поля salary. Если в списке нет ноды с искомым id, или в ячейке вообще нет
    связного списка (лежит None), то ничего не меняем в списке и возвращается None.

    ---ВРЕМЕННАЯ СЛОЖНОСТЬ---
    Среднее время добавления, получения и удаления информации равнр О(1). При коллизии
    временная сложность данных операций возрастает до O(n)

    ---ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ---
    Размер хранилища постоянный, т.е. пространственная сложность О(1). Но объем информации в каждой
    ячейке зависит от количества коллизий, т.е. равняется O(n)
"""



from typing import Optional, Tuple


HASH_TABLE_SIZE = 9973


class Node:
    def __init__(self, id: int, salary: int, next=None):
        self.id = id
        self.salary = salary
        self.next = next

class DB:
    def __init__(self):
        self.store = [None] * HASH_TABLE_SIZE

    def put(self, args: Tuple[int, int]) -> None:
        key, value = args[0], args[1]
        ind = key % HASH_TABLE_SIZE
        if self.store[ind] is None:
            self.store[ind] = Node(key, value)
        else:
            node = self.store[ind]
            while True:
                if key == node.id:
                    node.salary = value
                    return
                if node.next is None:
                    node.next = Node(key, value)
                    return
                node = node.next

    def get(self, args: Tuple[int]) -> Optional[int]:
        key = args[0]
        ind = key % HASH_TABLE_SIZE
        node = self.store[ind]
        if node is None:
            pass
        else:
            while node is not None:
                if node.id == key:
                    return node.salary
                node = node.next
        return None

    def delete(self, args: Tuple[int]) -> Optional[int]:
        key = args[0]
        ind = key % HASH_TABLE_SIZE
        node = self.store[ind]
        if node is None:
            pass
        elif node.id == key:
            self.store[ind] = node.next
            node.next = None
            return node.salary
        else:
            while node.next is not None:
                if node.next.id == key:
                    tmp = node.next
                    node.next = tmp.next
                    tmp.next = None
                    return tmp.salary
                node = node.next
        return None


def execute_commands() -> None:
    db = DB()
    count = int(input())
    results = []
    res_len = 0
    for _ in range(count):
        line = input().split()
        cmd = line[0]
        if cmd == 'put':
            args = int(line[1]), int(line[2])
        else:
            args = int(line[1]),
        result = getattr(db, cmd)(args)
        if cmd != 'put':
            results.append(result)
            res_len += 1
            if res_len >= 50000:
                print('\n'.join([str(x) for x in results]))
                results.clear()
                res_len = 0
    print('\n'.join([str(x) for x in results]))


if __name__ == '__main__':
    execute_commands()
