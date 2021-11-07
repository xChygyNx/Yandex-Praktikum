def max_retry(word: str) -> int:
    retry = 1
    for i in range(1, len(word)):
        retry = 1
        if len(word) % i == 0:
            prefix = word[:i]
            match = True
            while len(prefix) * retry < len(word):
                next_piece = word[len(word) - retry*len(prefix): len(word) - (retry-1) * len(prefix)]
                if prefix != next_piece:
                    match = False
                    break
                retry += 1
            if match:
                return retry
    return retry


if __name__ == '__main__':
    word = input()
    print(max_retry(word))