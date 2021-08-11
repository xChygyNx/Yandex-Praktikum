buttons = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h.py', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}

def generate_text(seq, nums, store):
    if len(nums) == 0:
        store.append(seq)
    else:
        for letter in buttons.get(nums[0]):
            generate_text(seq+letter, nums[1:], store)


if __name__ == '__main__':
    nums = input()
    result = []
    generate_text('', nums, result)
    result.sort()
    print(' '.join(result))