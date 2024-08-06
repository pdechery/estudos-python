# find max

def find_max_recursive(dataset):
	'''
	O uso da função recursiva aqui vai decrementar o dataset a cada chamada.
	Isto porque o Call Stack preserva o contexto de cada execução. 

	Exemplo:
	
	Na primeira chamada recursiva já tiramos o primeiro item da lista (find_max(dataset[1:])), então ela ficará assim:
	dataset = [0, 3, 5, 9, 12]

	Esta lista passa a ser o parâmetro da próxima chamada, que por sua vez irá usar novamente o slice para remover o primeiro elemento, ficando assim:
	dataset = [3, 5, 9, 12]

	E assim tiramos o primeiro item sucessivamente.

	Lembrar que a função só roda até o final quando as chamadas recursivas se completam, e a ordem é LIFO (last in first out)

	Notar também que o retorno final (return result) é usado nas próximas chamadas do Stack
	'''

	print(f'given data {dataset}')
	
	if len(dataset) == 1:
		return dataset[0]
	
	val1 = dataset[0]
	val2 = find_max_recursive(dataset[1:])

	print(f'val1 {val1}')
	#print(f'val2 {val2}')

	if val1 > val2:
		result = val1
	else:
		result = val2

	#print(f'Will return {result}')

	return result


def find_max_loop(dataset):
	print(f'dataset {dataset}')
	# store max value from each iteration
	res = 0 
	for i in range(0, len(dataset)-1, 2):
		print(f'index {i}')
		val1, val2 = dataset[i], dataset[i+1]
		print(f'val1 {val1}')
		print(f'val2 {val2}')
		if val1 > res:
			res = val1
		if val2 > res:
			res = val2

	return res


if __name__ == '__main__':
	
	values = [-1,0,12,3,2,5]
	print(find_max_recursive(values))