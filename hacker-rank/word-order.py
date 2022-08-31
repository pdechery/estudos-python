'''
Word Order

https://www.hackerrank.com/challenges/word-order

Sample input:

4
bcdef
abcdefg
bcde
bcdef

'''

def wordCount(words):

	count = []

	for i in words:
		count.append(words.count(i))

	uniques = len(set(words))

	res = count[:uniques-len(count)]
	
	print(' '.join(map(str,res)))


if __name__ == '__main__':

	n = input()
	words = list()

	for _ in range(int(n)):
		word = input().strip()
		words.append(word[:len(word)-1])

	words = ['bcdef','abcdefg','bcde','bcdef']

	wordCount(words)

	'''
	Solução melhor que a minha. Muito simples e funcional.
	'''

	n = int(input().strip())
	counter = {}
	words = []
	
	for i in range(n):
		word = input().strip()
		if word in counter:
			counter[word] += 1
		else:
			counter[word] = 1
			words.append(word)

	print(f'counter: {counter}')

	print(len(words))
	print(' '.join([str(counter[word]) for word in words]))

