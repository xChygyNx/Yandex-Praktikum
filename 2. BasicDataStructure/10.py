class Node:
    def __init__(self, value: int):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class MyQueueSized:
    def __init__(self):
        self.queue = None

    def put(self, num: int):
        if self.queue is None:
            self.queue = Node(num)
        else:
            current_node = self.queue
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = Node(num)

    def get(self):
        if self.queue is None:
            return 'error'
        else:
            get_node = self.queue
            self.queue = self.queue.next
            return get_node

    def size(self):
        size = 0
        node = self.queue
        while node is not None:
            size += 1
            node = node.next
        return size


def execute_command():
    count_command = int(input())
    queue = MyQueueSized()
    for _ in range(count_command):
        command = input()
        if command.startswith('put'):
            value = int(command.strip().split()[1])
            queue.put(value)
        elif command == 'get':
            print(queue.get())
        elif command == 'size':
            print(queue.size())


if __name__ == '__main__':
    execute_command()

