from typing import List


def merge(arr: List[int], left: int, mid: int, right: int) -> List[int]:
	left_arr = arr[left: mid]
	right_arr = arr[mid: right]
	len_left = len(left_arr)
	len_right = len(right_arr)
	i = j = 0
	result = []
	while i < len_left and j < len_right:
		if left_arr[i] <= right_arr[j]:
			result.append(left_arr[i])
			i += 1
		else:
			result.append(right_arr[j])
			j += 1
	if i < len_left:
		result.extend(left_arr[i:])
	else:
		result.extend(right_arr[j:])
	return result


def my_merge_sort(arr: List[int]) -> List[int]:
	len_arr = len(arr)
	if len_arr == 1:
		pass
	else:
		mid = len_arr // 2
		left_part = my_merge_sort(arr[:mid])
		right_part = my_merge_sort(arr[mid:])
		arr = left_part + right_part
		arr = merge(arr, 0, mid, len_arr)
	return arr


def merge_sort(arr: List[int], left: int, right: int) -> None:
	sort_arr = arr[left: right]
	sort_arr = my_merge_sort(sort_arr)
	pos = 0
	for i in range(left, right):
		arr[i] = sort_arr[pos]
		pos += 1


def test():
	a = [1, 4, 9, 2, 10, 11]
	b = merge(a, 0, 3, 6)
	expected = [1, 2, 4, 9, 10, 11]
	assert b == expected
	c = [1, 4, 2, 10, 1, 2]
	merge_sort(c, 0 , 6)
	expected = [1, 1, 2, 2, 4, 10]
	assert c == expected

if __name__ == '__main__':
	test()