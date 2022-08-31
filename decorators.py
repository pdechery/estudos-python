'''
Decorators
'''

def outro_decorator(func):
	# print(func)
	# <function diga_algo at 0x7f76c20340d0
	def qq_nome(*args):
		# faça coisas aqui
		print('Estamos felizes aqui também')
		# Depois executa a função pai
		func(*args)
	return qq_nome

def um_decorator(func):
	# print(func)
	# <function diga_algo at 0x7f76c20340d0
	def qq_nome(*args):
		# faça coisas aqui
		print('Estamos felizes aqui')
		# Depois executa a função pai
		func(*args)
	return qq_nome

@um_decorator
@outro_decorator
def diga_algo(algo):
	isto = f"Digo isto: {algo}"
	return isto


if __name__ == '__main__':
	
	res = diga_algo('carai')

	print(res)