# Search in list.
# Need to know the index of some value in ordered list

def find_index(my_list, value):
	
	# encontrar indexes dos extremos
	left, right = 0, len(my_list)

	# criar algum loop para repetir a operação até o esgotamento
	while left < right:

		# encontrar index do meio
		index_meio = (left + right) // 2 # '//' significa divisão com resultado sempre inteiro

		# verificar se o valor corresponde ao index do meio na lista passada
		if my_list[index_meio] == value:
			return index_meio

		# se não encontrou dividir a lista baseado na ordem dos elementos
		if my_list[index_meio] < value:
			# se o valor achado for menor vou cortar a lista do meio para a direita (segunda metade)
			left = index_meio
		elif my_list[index_meio] > value:
			# se for maior preciso cortar a lista do meio para a esquerda (primeira metade)
			right = index_meio


# Use recursion to compare neighbor elements in list
# repare que o valor retornado no base case é indiferente para a lógica da função
def equal_neighbors(my_list):
	# recursion base case
	if(len(my_list) == 1):
		return True
	
	if my_list[0] == my_list[1]:
		print(f'got neighbor: {my_list[0]} and {my_list[1]}')

	equal_neighbors(my_list[+1:])


# use the returned value from recursive function to perform math operations (factorial)
def recursive_math(n):
  if n == 1:
    return 1
  return n * recursive_math(n - 1)


# usar o retorno da função como elemento de cálculo
# nesse caso o retorno está na variável "max_val"
# esse valor é que será o retorno da linha 56 em cada iteração
def find_max_recursion(my_list):
	if len(my_list) == 1:
		return my_list[0]

	v1 = my_list[0]
	v2 = find_max_recursion(my_list[1:])

	max_val = v1 if v1 > v2 else v2

	return max_val


def bubble_sort(arr):
	for i in range(len(arr)-1):
		for j in range(len(arr)-1):
			if arr[j] > arr[j+1]:
					arr[j], arr[j+1] = arr[j+1], arr[j] 
	return arr

if __name__ == '__main__':

	#print(find_index([2,3,5,6,9,11,27],2))
	#equal_neighbors([2,3,3,5,6,6,9,11,27,27])
	#print(recursive_math(7))
	#print(find_max_recursion([270,3,9,59,6]))
	print(bubble_sort([270,3,9,59,6]))

