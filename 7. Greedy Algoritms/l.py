from typing import List, Any


def fill_first_row(bag_row: List[int], bullion: int) -> List[int]:
    row = [0 if x < bullion else bullion for x in range(len(bag_row) + 1)]
    return row


def find_true_indexes(lst: List[int], bag: List[bool]) -> None:
    lst.clear()
    for i in range(1, len(bag)):
        if bag[i]:
            lst.append(i)


def pack_bag(bullions: List[int], place: int) -> List[bool]:
    bag = [False for _ in range(place + 1)]
    true_indexes = []
    for i in range(len(bullions)):
        find_true_indexes(true_indexes, bag)
        for ind in true_indexes:
            try:
                bag[ind + bullions[i]] = True
            except IndexError:
                break
        try:
            bag[bullions[i]] = True
        except IndexError:
            pass
    return bag


def rfind(bag: List[bool], elem: Any) -> int:
    for i in range(len(bag) -1, -1, -1):
        if bag[i] == elem:
            return i
    return 0



if __name__ == '__main__':
    place = int(input().split()[1])
    bullions = [int(x) for x in input().split()]
    bag = pack_bag(bullions, place)
    print(rfind(bag, True))
