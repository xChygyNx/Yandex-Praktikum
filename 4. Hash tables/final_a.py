from typing import List, Tuple, Set

COUNT_DOCS = 0


class SearchIndex:
    def __init__(self):
        self.docs = {}

    def hashing_docs(self):
        doc_word = {}
        global COUNT_DOCS
        COUNT_DOCS = int(input())
        for i in range(COUNT_DOCS):
            doc = [x for x in input().split()]
            for word in doc:
                tmp = doc_word.get(word, {})
                tmp[i] = tmp.get(i, 0) + 1
                doc_word[word] = tmp
        self.docs = doc_word

    def get_request(self, request: Set[str]):
        request.clear()
        words = input().split()
        for word in words:
            request.add(word)

    def analysis(self) -> List[List[Tuple[int, int]]]:
        result = []
        count_requests = int(input())
        request = set()
        for _ in range(count_requests):
            self.get_request(request)
            line = []
            for i in range(COUNT_DOCS):
                score = 0
                for word in request:
                    tmp = self.docs.get(word, {})
                    score += tmp.get(i, 0)
                line.append((score * -1, i + 1))
            line.sort()
            result.append(line)
        return result


def get_five_docs(relevants: List[Tuple[int, int]]):
    length = len(relevants)
    limit = length if length < 5 else 5
    for i in range(limit):
        yield relevants[i]


def print_relevant_info(relevant_info: List[List[Tuple[int, int]]]) -> None:
    for line in relevant_info:
        print(' '.join((str(x[1]) for x in get_five_docs(line) if x[0] != 0)))

if __name__ == '__main__':
    s_ind = SearchIndex()
    s_ind.hashing_docs()
    relevant_info = s_ind.analysis()
    print_relevant_info(relevant_info)
