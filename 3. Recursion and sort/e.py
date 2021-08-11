if __name__ == '__main__':
	n, money = [int(x) for x in input().split()]
	houses = [int(x) for x in input().split()]
	houses.sort()
	buy_houses = 0
	for house in houses:
		if money < house:
			break
		else:
			buy_houses += 1
			money -= house
	print(buy_houses)