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
