'''
Find max value in nested lists

Input example (score and students)

Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

'''

students = [['Harry', 0.50], ['Berry', 0.25], ['Akriti', 0.25], ['Harsh', 0.50]]

scores = [score for name, score in students] # somente as notas

scores.sort() # ordem Ascendente, menor pro maior. ex: 1, 2, 3.

# ou: sorted(scores)

scores = list(set(scores)) # remover duplicados

result = [s[0] for s in students if s[1] == scores[1]] # index 1 é o segundo menor

result.sort()

if __name__ == '__main__':

	# scores = list()

	# for _ in range(int(input())):
	#     name = input()
	#     score = float(input())

	#     scores.append([name,score])

	quant_students = len(students)

	if quant_students >= 2 and quant_students <= 5:

		for r in result:

			print(r)
