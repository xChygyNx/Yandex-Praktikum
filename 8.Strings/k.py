from typing import List
from queue import Queue


class Node:
    def __init__(self):
        self.dict = {}
        self.lines = []

    def add_node(self, ch: str) -> None:
        self.dict[ch] = Node()

    def add_word(self, word: str) -> None:
        self.lines.append(word)
        # self.lines.sort()

    def get_node(self, ch: str):
        return self.dict[ch]




def build_trie(strs: List[str]) -> Node:
    head = Node()
    for word in strs:
        curr_node = head
        it = iter(word)
        for ch in it:
            if ord('A') <= ord(ch) <= ord('Z'):
                try:
                    curr_node = curr_node.get_node(ch)
                except KeyError:
                    curr_node.add_node(ch)
                    curr_node = curr_node.get_node(ch)
        curr_node.add_word(word)
    return head


def BFS(head: Node) -> List[str]:
    matches = []
    queue = Queue()
    queue.put(head)
    while not len(queue.queue) == 0:
        curr_node = queue.get()
        matches.extend([x for x in curr_node.lines])
        for next_node in curr_node.dict.values():
            queue.put(next_node)
    return sorted(matches)



def find_matches(trie: Node, patterns: List[str]) -> List[str]:
    matches = []
    for pattern in patterns:
        curr_node = trie
        interrupt = False
        for symb in pattern:
            try:
                curr_node = curr_node.get_node(symb)
            except KeyError:
                interrupt = True
        if not interrupt:
            matches.extend(BFS(curr_node))
    return matches

if __name__ == '__main__':
    n = int(input())
    strs = []
    for i in range(n):
        strs.append(input())
    trie = build_trie(strs)
    n = int(input())
    patterns = []
    for i in range(n):
        patterns.append(input())
    match = find_matches(trie, patterns)
    print('\n'.join([x for x in match]))
