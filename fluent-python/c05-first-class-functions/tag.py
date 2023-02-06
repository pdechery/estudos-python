'''
Using * and ** to pass multiple arguments to a function
* is for position (non-keyword) arguments
** is for keyword arguments

Everything that's passed beyond "name" and "cls", which are defined in the function's signature, will be captured by *content or **attrs
'''

def tag(name, *content, cls=None, **attrs): # -> parameters
	'''Generate one or more HTML tags'''
	
	if cls is not None:
		attrs['class'] = cls

	if attrs:
		attr_str = ' '.join(' %s="%s"' % (attr, value) for attr, value in sorted(attrs.items()))
	else:
		attr_str = ''
	
	if content:
		return '\n'.join('<%s%s>%s<%s>' % (name, attr_str, c, name) for c in content)
	else:
		return '<%s%s />' % (name, attr_str)

if __name__ == '__main__':

	# Function introspection attributes

	print(tag.__doc__) 

	print(tag.__defaults__) 

	print(tag.__kwdefaults__) 

	print(tag.__code__) 
	
	print(tag('br')) # -> argument	

	'''
	Look the function signature.
	'name' is a positional argument and it's the first one.
	Everything that comes after and it's positional will be captured by the *content parameter as a tuple
	'''
	print(tag('br', 'hello', 'world')) 

	'''
	Here I'm passing an unknow keyword argument, "id"
	It will be captured by **attrs as a dict
	'''
	print(tag('p', 'hello', id=33))

	'''
	Now, other than two extra positional arguments I'm passing a keyword argument that's on the function's signature
	'''
	print(tag('p', 'hello', 'world', cls='sidebar'))