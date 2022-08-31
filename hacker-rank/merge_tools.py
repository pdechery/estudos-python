'''
https://www.hackerrank.com/challenges/merge-the-tools

Dividir uma string em "k" substrings. 
Eliminar os elementos repetidos em cada substring.
Imprimir as substrings em linhas separadas

'''

def merge_the_tools(string, k):

	sstrings = len(string) // k

	for i in range(sstrings):

		res = ''

		start_point = i*k

		sstr = string[start_point:start_point+k]

		for i in range(len(sstr)):

			if sstr[i] in res:
				continue
			
			res += sstr[i]

		print(res)
    


if __name__ == '__main__':

	string, k = 'AABCAAADA', 3
	merge_the_tools(string, k)

