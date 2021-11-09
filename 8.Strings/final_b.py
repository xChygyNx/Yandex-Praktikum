"""
ID решения: 56346680

---ПРИНЦИП РАБОТЫ---
    Считываются строка и слова, которые будем искать в строке. Потом из искомых слов создаем
    синтаксическое дерево, причем помечаем булевым атрибутом ноды, которые соответствуют буквам,
    на которые оканчивались какие-либо из искомых слов.
    Дальше начинается поиск слов в строке методом динамического программирования. Мы создаем
    динамику размером длина строки + 1 с заполненными False'ом ячейками, кроме первой,
    в ней True. Динамика показывает какие префиксы из строки можно собрать из имеющихся строк,
    индекс ячейки обозначает длину префикса, потому ячейка с индексом 0 изначально заполнена
    значением True, потому что пустой префикс можно собрать при любых искомых словах. Дальше
    мы начинаем идти по динамике слева направо, и если в ячейке динамики лежит True, то с помощью
    раннее собранного префиксного дерева начинаем просматривать буквы строки, начиная с текущего
    индекса и проверять, есть ли такие последовательности в префиксном дереве. Если есть, то
    идем по дереву и сохраняем текущий индекс если в очередном узле дерева есть пометка, что
    на данную букву оканчивается какое-либо из искомых слов. Если очередная последовательность
    в дереве не найдена, то мы возвращаем собранные индексы, и в этих индексах динамики ставим
    True. Так идем до конца динамики, и если в конце в последней ячейке будет лежать True,
    то рассматриваемую строку можно составить из искомых слов.

---ВРЕМЕННАЯ СЛОЖНОСТЬ---
    Построение префиксного дерева занимает O(n) времени, где n - общее количество букв в
    искомых словах (даже если рассматриваемая последовательность была добавлена ранее
    ее все равно надо просмотреть до конца и перейти по ранее созданным узлам). Создание
    динамтики занимает O(m+1) времени, где m - количество букв в рассматриваемой строке.
    Наконец сам проход по динамике занимает O(2(m+1)), потому что раз мы проходим диапазон
    индексов когда ищем индексы на которых проставим True, и второй раз когда просматриваем
    динамику на наличие этих самых True, чтобы начать с них просмотр префиксного дерева. Итоговая
    временная сложность составляет O(n * m)

---ПРОСТРАНСТВЕННАЯ СЛОЖНОСТЬ---
    Для алгоритма требуется одномерная динамика размером (m + 1), где m - число букв в рассматриваемой
    строке, и еще нужно создать префиксное дерево, которое в случае, если у искомых слов вообще нет
    общих префиксов займет O(p + 1) места, где p - общее количество символов в искомых словах, а +1
    потому что первая ноды создается под пустой префикс. Итоговая пространственная сложность составляет
    O(n + m)
"""


from typing import List


class Node:
    def __init__(self):
        self.complete = False
        self.dict = {}

    def add_node(self, ch: str):
        self.dict[ch] = Node()


def build_trie(words: List[str]) -> Node:
    head = Node()
    for word in words:
        cur = head
        for ch in word:
            if ch in cur.dict.keys():
                cur = cur.dict[ch]
            else:
                cur.add_node(ch)
                cur = cur.dict[ch]
        cur.complete = True
    return head


def find_words(line: str, trie: Node, begin_ind: int) -> List[int]:
    cur = trie
    offsets = []
    for i in range(begin_ind, len(line)):
        try:
            cur = cur.dict[line[i]]
            if cur.complete:
                offsets.append(i+1)
        except KeyError:
            break
    return offsets


def find_match(trie: Node, line: str) -> bool:
    dp = [False for _ in range(len(line) + 1)]
    dp[0] = True
    for i in range(len(dp) - 1):
        if dp[i]:
            offsets = find_words(line, trie, i)
            for offset in offsets:
                dp[offset] = True
    return dp[-1]


if __name__ == '__main__':
    line = input()
    n = int(input())
    words = []
    for _ in range(n):
        words.append(input())
    trie = build_trie(words)
    match = find_match(trie, line)
    print('YES' if match else 'NO')
