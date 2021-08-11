class StackMax:
    def __init__(self):
        self.store = []

    def push(self, value: int) -> None:
        self.store.append(value)

    def pop(self):
        if len(self.store) == 0:
            print('error')
        else:
            self.store.pop()

    def get_max(self):
        if len(self.store) == 0:
            print(None)
        else:
            print(max(self.store))



def execute_command(stack: StackMax):
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
    stack = StackMax()
    execute_command(stack)
