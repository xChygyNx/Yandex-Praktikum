def iterative_money(money, price):
    length = len(money)
    start = 0
    end = length - 1
    while start < end:
        if money[start] == price:
            return start
        mid = (end + start + 1) // 2
        if price == money[mid] or (price <= money[mid] and price > money[mid - 1]):
            return mid
        elif price < money[mid]:
            end = mid
        elif price > money[mid]:
            start = mid


def check_early(money, day):
    while money[day] == money[day - 1]:
        day -= 1
    return day + 1


def define_day(money, price):
    if price > money[-1]:
        return -1
    elif price < money[0]:
        return 1
    else:
        day = iterative_money(money, price)
        day = check_early(money, day)
        return day


if __name__ == '__main__':
    days = int(input())
    d_moneys = [int(x) for x in input().strip().split()]
    bycicle_price = int(input())
    one_buy = define_day(d_moneys, bycicle_price)
    two_buy = define_day(d_moneys, 2 * bycicle_price)
    print(f'{one_buy} {two_buy}')