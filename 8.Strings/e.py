class Node:
    def __init__(self, ch: str):
        self.ch = ch
        self.next = None

    def add_node(self, ch: str):
        self.next = Node(ch)

    def shrink(self):
        self.next = None

    def __iter__(self):
        return self

    def __next__(self):
        return self.next

    def __len__(self):
        result = 0
        node = self
        while node is not None:
            result += 1
            node = node.next
        return result


def build_trie(word: str) -> Node:
    it = iter(word)
    head = Node(next(it))
    cur_node = head
    for ch in it:
        cur_node.add_node(ch)
        cur_node = cur_node.next
    return head


def shrink_trie(trie: Node, word: str) -> Node:
    cur = trie
    if cur is None or cur.ch != word[0]:
        return None
    i = 1
    while cur is not None:
        try:
            if cur.next.ch != word[i]:
                cur.shrink()
                return trie
        except (AttributeError, IndexError):
            return trie
        i += 1
        cur = cur.next
    return trie


if __name__ == '__main__':
    n = int(input())
    word = input()
    trie = build_trie(word)
    for _ in range(n-1):
        trie = shrink_trie(trie, input())
    print(len(trie) if trie is not None else 0)
