def recursive_money(money, price, start_ind, end_ind):
    k = (end_ind - start_ind) // 2
    mid = start_ind + k
    if price >= money[k-1] and price <= money[k]:
        if price == money[k-1]:
            return mid
        else:
            return mid + 1
    elif money[0] == price:
        return start_ind + 1
    elif money[-1] == price:
        return end_ind + 1
    elif price < money[k]:
        return recursive_money(money[:k+1], price, start_ind, mid)
    elif price > money[k]:
        return recursive_money(money[k+1:], price, mid+1, end_ind)


def check_early(money, day):
    while(money[day] == money[day - 1]):
        day -= 1
    return day + 1


def define_day(money, price, start_ind, end_ind):
    if price > money[-1]:
        return -1
    elif price < money[0]:
        return 1
    else:
        day = recursive_money(money, price, start_ind, end_ind)
        day = check_early(money, day - 1)
        return day


if __name__ == '__main__':
    days = int(input())
    d_moneys = [int(x) for x in input().strip().split()]
    bycicle_price = int(input())
    last_ind = len(d_moneys) - 1
    one_buy = define_day(d_moneys, bycicle_price, 0, last_ind)
    two_buy = define_day(d_moneys, 2 * bycicle_price, 0, last_ind)
    print(f'{one_buy} {two_buy}')