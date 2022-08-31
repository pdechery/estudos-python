'''
Uso do eval() para executar script a partir de string()

https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true

'''

if __name__ == '__main__':

	N = int(input())
	string_com = ''
	lista = []

	for _ in range(N):
		
		com = input().split()
		
		if com[0] == 'print':
			print(string_com)
		else: 
			if len(com) == 3:
				string_com = 'lista.{command}({arg1},{arg2})'.format(command=com[0],arg1=com[1],arg2=com[2])
				eval(string_com)
			elif len(com) == 2:
				string_com = 'lista.{command}({arg1})'.format(command=com[0],arg1=com[1])
				eval(string_com)
			elif len(com) == 1:
				string_com = 'lista.{command}()'.format(command=com[0])
				eval(string_com)

	print(lista)

