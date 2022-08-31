def testDocTest(arg):
	'''
	O que vai dentro deste bloco é chamado DocString e serve de documentação para funções ou classes

	Também existe o DocTest, que será exemplificado abaixo,

	>>> numero = 2
	>>> testDocTest(numero)
	>>> numero
	1433
	'''
	return arg * 2

if __name__ == '__main__':
	numero = 2
	testDocTest(numero)