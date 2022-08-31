# Enter your code here. Read input from STDIN. Print output to STDOUT

def divideThis(num1,num2):
	try:
		res = int(num1) // int(num2)
		print(int(res))
	except TypeError as e:
		print(f'Error Code: {e.args[0]}')
	except ValueError as e:
		print(f'Error Code: {e.args[0]}')
	except ZeroDivisionError as e:
		print(f'Error Code: {e.args[0]}')

if __name__ == '__main__':
	
	test_cases = int(input())

	for _ in range(test_cases):
		nums = input().split()
		divideThis(nums[0],nums[1])