from typing import List, Optional


def count_prices_difs(prices: List[int]) -> List[int]:
    difs = [0] * len(prices)
    difs[0] = prices[0]
    for i in range(1, len(prices)):
        difs[i] = prices[i] - prices[i - 1]
    return difs


def next_buy(difs: List[int], i: int) -> Optional[int]:
    for day in range(i, len(difs)):
        if difs[day] > 0:
            return day - 1


def maximize_profit(prices: List[int], difs: List[int]) -> int:
    profit = 0
    buy = prices[0]
    i = 1
    while i < len(difs):
        if difs[i] < 0:
            profit += prices[i - 1] - buy
            i = next_buy(difs, i)
            if i is not None:
                buy = prices[i]
            else:
                break
        i += 1
    if difs[-1] > 0:
        profit += prices[-1] - buy
    return profit


if __name__ == '__main__':
    n = int(input())
    prices = [int(x) for x in input().split()]
    difs = count_prices_difs(prices)
    profit = maximize_profit(prices, difs)
    print(profit)