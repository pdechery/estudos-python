'''
Minion Game

https://www.hackerrank.com/challenges/the-minion-game

# https://programs.programmingoneonone.com/2021/01/hackerrank-the-minion-game-solution-python.html

Criar dois grupos com todas substrings possivels de uma palavra.

O primeiro grupo deve criar substrings que se iniciam por vogal. O segundo, por consoantes

Cada substring vale 1 ponto. Se a substring se repetir o ponto é incrementado.

Comparar os pontos e calcular o grupo com total maior.

'''

def minion_game(word):

	kevin_score, stuart_score = 0,0

	for i in range(len(word)):

		if word[i] in ('A','E','I','O','U'):

			'''
			O segredo aqui é criar substrings de trás pra frente.
			Por exemplo:
			ANANAS tem valor 6
			pq contém todas substrings que começam com sua primeira letra, que é A
			ANANAS
			ANANA
			ANAN
			ANA
			AN
			A
			Cada uma valendo 1 o total é 5. E todas são substrings válidas.
			'''

			#print(f'word V {word[i]}')
			#print(len(word) - i)

			kevin_score += len(word) - i

		else:

			print(f'word C {word[i]}')
			print(len(word) - i)

			stuart_score += len(word) - i

	if kevin_score > stuart_score:
		print(f"Kevin {kevin_score}")
	elif stuart_score > kevin_score:
		print(f"Stuart {stuart_score}")
	else:
		print("Draw")



def minion_game_old(word):

	print(word)

	vowels = ('A','E','I','O','U')
	consonants = ('B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z')

	def create_substrings(type):

		res = list()
	
		for index in range(len(word)):

			if word[index] in type:

				loop = len(word)-index

				for x in range(loop):
					
					substr = word[index:index+(x+1)]

					res.append(substr)

		return res

	
	kevin_set = create_substrings(vowels)
	stuart_set = create_substrings(consonants)

	print(kevin_set)
	print(stuart_set)

	if len(kevin_set) > len(stuart_set):
		print(f"Kevin {len(kevin_set)}")
	elif len(stuart_set) > len(kevin_set):
		print(f"Stuart {len(stuart_set)}")
	else:
		print("Draw")


if __name__ == '__main__':

	string = "ANANAS"

	minion_game(string)