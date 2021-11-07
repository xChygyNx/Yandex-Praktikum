from math import fabs


class Comparator:
    def __init__(self, name1: str, name2: str):
        self.name1 = name1
        self.name2 = name2

    def cmp_lefts(self, ind: int) -> bool:
        if self.name1[ind+1:] == self.name2[ind:] or self.name1[ind:] == self.name2[ind+1:] or\
            self.name1[ind+1:] == self.name2[ind+1:]:
            return True
        return False

    def is_pass(self) -> str:
        if int(fabs(len(self.name1) - len(self.name2))) > 1:
            return 'FAIL'
        for i in range(len(self.name1)):
            if self.name1[i] != self.name2[i]:
                if self.cmp_lefts(i+1):
                    return 'OK'
                else:
                    return 'FAIL'
        return 'OK'



if __name__ == '__main__':
    name1 = input()
    name2 = input()
    cmp = Comparator(name1, name2)
    print(cmp.is_pass())