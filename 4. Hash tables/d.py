if __name__ == "__main__":
    n = int(input())
    result = {}
    for _ in range(n):
        society = input()
        result[society] = result.get(society, 0) + 1
    for society in result.keys():
        print(society)
