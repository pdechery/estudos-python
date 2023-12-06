def find_index(arr, val):
	print(arr)
	
	left, right = 0, len(arr) - 1

	while left <= right:
		print(f'left {left}, right {right}')
		middle = (left + right) // 2

		if arr[middle] == val:
			return middle

		if arr[middle] < val:
			left = middle + 1
		elif arr[middle] > val:
			right = middle - 1


if __name__ == '__main__':
    
    um_array = [-1,0,3,5,9,12]
    print(find_index(um_array, 9))