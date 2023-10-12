'''
Decorators
'''

def factory_decorator():
	'''
	Estudar
	https://docs.pytest.org/en/6.2.x/fixture.html#factories-as-fixtures
	'''
	def wrap(arg1,arg2):
		return arg1 + arg2
	return wrap

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

@factory_decorator()
def test_factory_decorator(a1,a2):
	print(a1)
	print(a2)


if __name__ == '__main__':
	
	#res = diga_algo('carai')

	# estudo factory pattern com decorator
	res = test_factory_decorator(35,70)

	print(res)