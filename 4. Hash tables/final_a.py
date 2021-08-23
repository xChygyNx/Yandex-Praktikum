from typing import List, Tuple

A = 107
M = 1000007


class SearchIndex:
    def __init__(self):
        self.docs = []
        self.requests = []
        self.read_data()

    def read_data(self):
        doc_count = int(input())
        for _ in range(doc_count):
            self.docs.append(input().split())
        req_count = int(input())
        for _ in range(req_count):
            self.requests.append(input().split())

    def hashing_docs(self):
        for num_doc, doc in enumerate(self.docs):
            doc_word = {}
            for word in doc:
                doc_word[word] = doc_word.get(word, 0) + 1
            self.docs[num_doc] = doc_word

    def hashing_request(self):
        for num_request, request in enumerate(self.requests):
            request_word = set()
            for req_word in request:
                request_word.add(req_word)
            self.requests[num_request] = request_word

    def hash_word(self):
        self.hashing_docs()
        self.hashing_request()

    def analysis(self) -> List[List[Tuple[int, int]]]:
        result = []
        for request in self.requests:
            request_scores = []
            for num_doc, doc in enumerate(self.docs):
                score = 0
                for request_word in request:
                    score += doc.get(request_word, 0)
                request_scores.append((-1 * score, num_doc + 1))
            request_scores.sort()
            result.append(request_scores[:5])
        return result


def get_five_docs(relevants: List[Tuple[int, int]]):
    length = len(relevants)
    limit = length if length < 5 else 5
    for i in range(limit):
        yield relevants[i]


def print_relevant_info(relevant_info: List[List[Tuple[int, int]]]) -> None:
    result = []
    for line in relevant_info:
        tmp = [str(x[1]) for x in get_five_docs(line) if x[0] != 0]
        try:
            _ = tmp[0]
            result.append(' '.join(tmp))
        except IndexError:
            pass
    print('\n'.join(result))


if __name__ == '__main__':
    s_ind = SearchIndex()
    s_ind.hash_word()
    relevant_info = s_ind.analysis()
    print_relevant_info(relevant_info)
