'''
Retomando o desafio em Fevereiro de 2023
'''


def minion_game_hacker_rank_other_guy_solution(w):

	count_vowel = count_cons = 0

	for i in range(len(w)):

		if w[i] in ['A','E','I','O','U']:

			#print(f'vogal encontrada {w[i]}')
			#print(f'valor {len(w)-i}')

			count_vowel += len(w) - i

		else:

			#print(f'consoante encontrada {w[i]}')
			#print(f'valor {len(w)-i}')

			count_cons += len(w) - i

	return count_vowel, count_cons



def minion_game_v(w):
	
	count_vowel = 0

	for c in w:

		if c in ['A','E','I','O','U']:

			z = w.find(c)

			count_vowel += len(w[z:])

			w = w[z+1:]

			#print(f'char "{c}", index {z}, value {count_vowel}')
			#print(f"transformed: {string}")

	return count_vowel


def minion_game_c(w):
	
	count_cons = 0

	for c in w:

		if c not in ['A','E','I','O','U']:

			z = w.find(c)

			count_cons += len(w[z:])

			w = w[z+1:]

			#print(f'char "{c}", index {z}, value {count_cons}')
			#print(f"transformed: {string}")

	return count_cons



if __name__ == '__main__':
	
	#s = input()
	#rkevin = minion_game_v(s.upper())
	#rstuart = minion_game_c(s.upper())

	val1, val2 = minion_game_hacker_rank_other_guy_solution("eleonora".upper())

	print(val1)
	print(val2)

	# if rkevin > rstuart:
	# 	print(f'Kevin {rkevin}')
	# elif rstuart > rkevin:
	# 	print(f'Stuart {rstuart}')
	# else:
	# 	print("Draw")
