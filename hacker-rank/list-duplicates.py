'''
Encontrar valores duplicados em listas e calcular o total de vezes em que aparecem
'''

test = ["pe","pa","pe","pi"]
test2 = [(x,test.count(x)) for x in test]

'''
>>> test2
[('pe', 2), ('pa', 1), ('pe', 2), ('pi', 1)]
'''

test3 = set(test2)

'''
>>> test3
{('pi', 1), ('pa', 1), ('pe', 2)}
''' 
