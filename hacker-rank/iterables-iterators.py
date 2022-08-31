'''
Iterables and iterators

https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true

Resposta para estudar: 

https://programs.programmingoneonone.com/2021/01/hackerrank-iterables-and-iterators-solution-python.html

'''

import itertools

if __name__ == '__main__':
	
	list_len = int(input())
	string = input().split()
	repeat = int(input())

	# print(f'list_len: {list_len}')
	# print(f'string: {string}')
	# print(f'repeat: {repeat}')

	indexes = [key+1 for key,l in enumerate(string) if l == 'a']

	print(f'indexes: {indexes}')

	combinations = list(itertools.combinations(range(1,len(string)+1), repeat))

	res = 0
	
	for c in combinations:
		for i in indexes:
			if i in c:
				res += 1
				break

	#print(f'combinations: {combinations}')

	#print(f'res: {res}')

	print(f'{res/len(combinations)}')