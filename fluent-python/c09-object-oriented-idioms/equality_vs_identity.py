'''
Function Parameters as references

In Python function parameters are aliases of its arguments

An alias is a reference to one object. That means it has the same identity of that object.

Other than a name a variable can have multiple aliases, and all of them will be references to the same object

Identity check is performed by "is" statement, while value check is performed by "==" operator.
'''

def f(a, b): # "a" and "b" are the function parameters
	print(f'id(a): {id(a)}')
	print(f'id(b): {id(b)}')
	print(f'a == x: {a == x}') # Value check returns True
	print(f'a is x: {a is x}') # Identity check returns True
	print('Now let\'s change "a" value')
	a = 4
	print(f'a is x: {a is x}')
	a += b
	return a

x = 1
y = 2
z = f(x,y) # "x" and "y" are the function's arguments

# Two objects can carry the same value but not the same identity

me = {'nome':'Pierre','sobrenome':'Dechery'}

# alias for "me" variable
pierre = me

# new variable copying my data
false_me = {'nome':'Pierre','sobrenome':'Dechery'}

if __name__ == '__main__':
	
	print(f'z value is: {z}')

	# id() built-in function returns integer representing object's identity, which is unmutable
	print(f'id(x): {id(x)}') 
	print(f'id(y): {id(y)}')

	print(f'pierre is me {pierre is me}')
	print(f'false_me is me {false_me is me}')