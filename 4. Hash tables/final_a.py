from typing import List, Tuple, Dict

COUNT = 0


class SearchIndex:
    def __init__(self):
        self.docs = {}
        self.requests = {}

    def hashing_words(self):
        words = {}
        global COUNT
        COUNT = int(input())
        for i in range(COUNT):
            doc = [x for x in input().split()]
            for word in doc:
                tmp = words.get(word, {})
                tmp[i+1] = tmp.get(i+1, 0) + 1
                words[word] = tmp
        return words

    def sort_requests(self, requests: List[Dict[int, int]]):
        requests = requests[1:]
        result = []
        for num_elem, request in enumerate(requests):
            line = []
            for key, value in request.items():
                line.append((-1 * value, key))
            line.sort()
            result.append(line[:5])
        return result

    def analysis(self) -> List[List[Tuple[int, int]]]:
        result = [{} for _ in range(COUNT + 1)]
        for request_word, request_word_info in self.requests.items():
            try:
                elem = self.docs[request_word]
                for num_doc, score in elem.items():
                    for num_request in request_word_info.keys():
                        result[num_request][num_doc] = result[num_request].get(num_doc, 0) + score
            except KeyError:
                pass
        result = self.sort_requests(result)
        return result


def print_relevant_info(relevant_info: List[List[Tuple[int, int]]]) -> None:
    for line in relevant_info:
        print(' '.join((str(x[1]) for x in line if x[0] != 0)))

if __name__ == '__main__':
    s_ind = SearchIndex()
    s_ind.docs = s_ind.hashing_words()
    s_ind.requests = s_ind.hashing_words()
    relevant_info = s_ind.analysis()
    print_relevant_info(relevant_info)
