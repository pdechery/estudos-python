'''
https://www.hackerrank.com/challenges/most-commons
'''

from collections import defaultdict, Counter
from operator import itemgetter

def three_top_most_with_counter(name):

	'''
	Mesma definição abaixo, porém usando o Counter e itemgetter para a ordenação (em dois niveis)
	'''

	test = Counter(name)

	test = sorted(test.items(), key=itemgetter(1,0))

	for k,v in test:
		print(f'{k} {v}')


def three_top_most(name):

	'''
	Encontra ocorrências de elementos iguais numa string
	Calcula o número de ocorrências de cada elemento
	Ordena resultado por 1) número ocorrências 2) ordem alfabética de cada letra (chave)

	Esta solução usa o defaultdict
	'''

	ddict = defaultdict(int)

	for i in name:

		if ddict[i]:
			ddict[i] += 1
			continue

		ddict[i] = 1

	ddict = sorted(ddict.items(), key=lambda t: (-t[1], t[0]))

	for k,v in ddict[:3]:
		print(f'{k} {v}')

if __name__ == '__main__':
	
	#three_top_most('aabbbccde')
	three_top_most_with_counter('aabbbccde')