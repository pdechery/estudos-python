import time

'''
Decorators are typically used (not only) to replace the decorated function with a new function that accepts the same arguments and (usually) returns whatever the decorated function was supposed to return, while also doing some extra processing.
'''

def clock(func):
	def clocked(*args):
		t0 = time.perf_counter()
		'''
		Call the decorated function and store its result
		The 'func' variable is called a 'free-variable' and it's available here because it's in a closure.
		'''
		result = func(*args) 
		elapsed = time.perf_counter() - t0
		name = func.__name__
		arg_str = ', '.join(repr(arg) for arg in args)
		print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
		return result
	return clocked

@clock
def snooze(seconds):
	time.sleep(seconds)

@clock
def factorial(n):
	return 1 if n < 2 else n * factorial(n-1)

'''
SLIGHT DETOUR: RECURSIVE FUNCTION
'''

def basic_fib(func):
	print('I\'m a basic decorator')
	return func

def fib(func):
	def inner(n):
		print(f'fibonnaci argument: {n}')
		result = func(n)
		return result
	return inner


@basic_fib
def fibonnacci(n):
	if n < 2:
		return n
	return fibonnacci(n-2) + fibonnacci(n-1)

if __name__ == '__main__':

	# print('*' * 40, 'Calling snooze(.123)')
	# print(snooze(.123))
	
	# print('*' * 40, 'Calling factorial(6)')
	# print('6! =', factorial(6))

	print(fibonnacci(10))

