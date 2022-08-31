'''
Da especificação do Python:
[https://docs.python.org/3/library/string.html#formatspec]

"{" [field_name] ["!" conversion] [":" format_spec] "}"
'''

if __name__ == '__main__':

	# Exemplos

	# conversion

	# !s -> string

	print("Eu tenho {idade!s}".format(idade=47))

	# !r -> repr()

	print("O método repr() será chamado nessa string: {bacana!r}".format(bacana='legal'))

	print("repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2'))

	# format_spec

	'''
	Format Specification (format_spec) é como uma mini-linguagem que pode ser usada nas strings com o format()

	Sempre é precedido por ":" 

	A definição seria essa:

	format_spec     ::=  [[fill]align][sign][#][0][width][grouping_option][.precision][type]
	fill            ::=  <any character>
	align           ::=  "<" | ">" | "=" | "^"
	sign            ::=  "+" | "-" | " "
	width           ::=  digit+
	grouping_option ::=  "_" | ","
	precision       ::=  digit+
	type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"


	O 'precision' (precedido por um ponto) serve para especificar:
	1) Quantos dígitos devem aparecer após o "." (quando usado com 'f' ou 'F')
	2) Quantos dígitos devem aparecer antes ou depois do '.' (quando usado com 'g' ou 'G')
	Se usado com strings vai limitar o número de caracteres da string
	'''

	# Exemplos

	# type

	# 'd' converte pra decimal
	# 's' converte pra string
	# 'n' igual a 'd' mas respeita o locale
	# 'f' e 'F' converte pra float (Só funciona se o valor for um inteiro)

	print("Vamos testar {:s}".format('12000'))
	print("Vamos testar {:.2f}".format(83.333))
	print("Vamos testar {:.2}".format('aloualou'))

	# fill

	coisafofa = 1
	
	f'{coisafofa:0>2}'
	#'01'
	
	f'{coisafofa:0<2}'
	# '10'
	
	coisafofa = 12
	
	f'{coisafofa:0<2}'
	#'12'








