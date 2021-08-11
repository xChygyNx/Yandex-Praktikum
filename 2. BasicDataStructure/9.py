from queue import Queue


class MyQueueSized:
    def __init__(self, max_size: int):
        self.queue = Queue()
        self.max_size = max_size

    def push(self, num: int):
        if self.queue.qsize() == self.max_size:
            print('error')
        else:
            self.queue.put(num)

    def pop(self):
        if self.queue.qsize() == 0:
            return None
        else:
            return self.queue.get()

    def peek(self):
        if self.queue.qsize() == 0:
            return None
        return self.queue.queue[0]

    def size(self):
        return self.queue.qsize()


def execute_command():
    count_command = int(input())
    max_size = int(input())
    queue = MyQueueSized(max_size)
    for _ in range(count_command):
        command = input()
        if command.startswith('push'):
            value = int(command.strip().split()[1])
            queue.push(value)
        elif command == 'pop':
            print(queue.pop())
        elif command == 'peek':
            print(queue.peek())
        elif command == 'size':
            print(queue.queue.qsize())


if __name__ == '__main__':
    execute_command()

