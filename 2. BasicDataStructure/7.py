class StackMaxEffective:
    def __init__(self):
        self.max_value = [None]
        self.max_len = 0
        self.store = []
        self.store_length = 0

    def push(self, value: int) -> None:
        try:
            if self.max_value[self.max_len] <= value:
                self.max_value.append(value)
                self.max_len += 1
        except TypeError:
            self.max_value.append(value)
            self.max_len += 1
        self.store.append(value)
        self.store_length += 1

    def pop(self):
        if self.store_length == 0:
            print('error')
        else:
            pop_value = self.store.pop()
            if pop_value == self.max_value[self.max_len]:
                self.max_value.pop()
                self.max_len -= 1
            self.store_length -= 1

    def get_max(self):
        print(self.max_value[self.max_len])



def execute_command(stack: StackMaxEffective):
    count_command = int(input())
    for _ in range(count_command):
        command = input().strip()
        if command.startswith('push'):
            value = int(command.split()[1])
            stack.push(value)
        elif command == 'pop':
            stack.pop()
        elif command == 'get_max':
            stack.get_max()



if __name__ == '__main__':
    stack = StackMaxEffective()
    execute_command(stack)
