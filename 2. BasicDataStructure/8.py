OPEN_BRACKETS = {'(', '{', '['}
CLOSE_BRACKETS = {')', '}', ']'}
bracket_match = {
    '(': ')',
    '[': ']',
    '{': '}'
}

class Stack:
    def __init__(self):
        self.store = []

    def push(self, symbol: str) -> None:
        self.store.append(symbol)

    def pop(self):
        return self.store.pop()


def check_seq(seq: str) -> bool:
    stack = Stack()
    for symbol in seq:
        if symbol in OPEN_BRACKETS:
            stack.push(symbol)
        elif symbol in CLOSE_BRACKETS:
            try:
                open_bracket = stack.pop()
            except IndexError:
                return False
            if not symbol == bracket_match.get(open_bracket):
                return False
    if len(stack.store) > 0:
        return False
    return True


if __name__ == '__main__':
    seq = input().encode(encoding='ascii', errors='ignore')
    seq = seq.decode(encoding='ascii')
    print(check_seq(seq))