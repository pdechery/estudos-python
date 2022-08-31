'''
defaultdict lesson

https://www.hackerrank.com/challenges/defaultdict-tutorial

Encontrar palavras do grupo B que existem no grupo A, printando seus índices.
Se não existir índice, printar "-1"

Sample input:

5 2
a
a
b
a
b
a
b

'''

from collections import defaultdict

d = defaultdict(list)

if __name__ == '__main__':
	
	ranges = input().split()

	for i in range(int(ranges[0])):
		d['A'].append(input())

	for i in range(int(ranges[1])):
		d['B'].append(input())

	res = []

	# Logica

	for b in d['B']:
		res.clear()
		for k,v in enumerate(d['A']):
			if b == v:
				res.append(k)
		if not len(res):
			print(-1)
		else:
			print(' '.join(map(lambda x: str(x), res)))

