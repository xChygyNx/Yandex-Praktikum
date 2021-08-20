from typing import List, Tuple

A = 107
M = 1000007


class SearchIndex:
    def __init__(self):
        self.docs = []
        self.requests = []
        self.read_data()
        self.hash_docs = []
        self.hash_requests = []
        self.relevant_score = []

    def read_data(self):
        doc_count = int(input())
        for _ in range(doc_count):
            self.docs.append(input().split())
        req_count = int(input())
        for _ in range(req_count):
            self.requests.append(input().split())

    def hash_word(self) :
        for phrase in self.docs:
            line = []
            for word in phrase:
                _sum = 0
                for ch in word:
                    _sum = _sum * A + ord(ch)
                    _sum %= M
                line.append(_sum)
            self.hash_docs.append(line)
        for phrase in self.requests:
            line = []
            for word in phrase:
                _sum = 0
                for ch in word:
                    _sum = _sum * A + ord(ch)
                    _sum %= M
                line.append(_sum)
            self.hash_requests.append(line)

    def analysis(self) -> List[List[Tuple[int, int]]]:
        result = []
        meet_words = set()
        for num_request, phrase_request_hash in enumerate(self.hash_requests):
            request_scores = []
            for num_doc, phrase_doc_hash in enumerate(self.hash_docs):
                score = 0
                meet_words.clear()
                for num_request_word, word_request_hash in enumerate(phrase_request_hash):
                    if self.requests[num_request][num_request_word] not in meet_words:
                        meet_words.add(self.requests[num_request][num_request_word])
                        for num_doc_word, word_doc_hash in enumerate(phrase_doc_hash):
                            if word_request_hash == word_doc_hash and\
                                self.requests[num_request][num_request_word] == self.docs[num_doc][num_doc_word]:
                                score += 1
                request_scores.append((-1 * score, num_doc+1))
            request_scores.sort()
            result.append(request_scores)
        return result


def print_relevant_info(relevant_info: List[List[Tuple[int, int]]]) -> None:
    result = []
    for line in relevant_info:
        line = line[: 5]
        tmp = [str(x[1]) for x in line if x[0] != 0]
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
