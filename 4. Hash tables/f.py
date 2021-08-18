from typing import Dict, List


def hash(s: str) -> Dict[str, int]:
    result = {}
    for ch in s:
        result[ch] = result.get(ch, 0) + 1
    return result


class AnagramsGroup:
    def __init__(self, anagrams: List[str]):
        self.anagrams = anagrams
        self.hash_store = []
        self.groups = []
        self.set_groups()

    def set_groups(self):
        for i, an in enumerate(self.anagrams):
            hash_an = hash(an)
            try:
                ind = self.hash_store.index(hash_an)
                self.groups[ind].append(i)
            except ValueError:
                self.hash_store.append(hash_an)
                self.groups.append([i])

    def print(self):
        for group in self.groups:
            print(' '.join([str(x) for x in group]))


if __name__ == '__main__':
    _ = input()
    anagrams = input().split()
    ob = AnagramsGroup(anagrams)
    ob.print()
