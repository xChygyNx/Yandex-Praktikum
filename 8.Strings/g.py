if __name__ == '__main__':
    n = int(input())
    words = {}
    for _ in range(n):
        word = input()
        words[word] = words.get(word, 0) + 1
    max_retry = max(words.values())
    max_retry_words = [x for x, num in words.items() if num == max_retry]
    max_retry_words.sort()
    print(max_retry_words[0])
