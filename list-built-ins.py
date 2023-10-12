lst = [1,2,-5,4]

# Slice

list[x:y:z]

'''
x => Index start
y => Index End (up to, not including)
z => Step
'''

lst[:2]
# [1,2] 

# Se y ultrapassar o maior index, retorna o ultimo
lst[:8]
# [1,2,-5,4]

# Map

def square(x):
	return x * x

map(square, lst)

list(map(square, lst))

# List Comprehension

[square(n) for n in lst]

# Filter

def is_odd(num):
	return x % 2 == 1

filter(is_odd, lst)

list(filter(is_odd, lst))

# List Comprehension

[n for n in lst if is_odd(n)]

# Max

max(1,2,3)

max(lst)

max(lst, key=lambda x:x*x)

# Min

min(1,2,3)

min(lst)

# Any

any(lst)

any(0, 0, False)

# All
# @todo

# Sort

animals = ['cat','dog', 'cheetah','rhino']

# Returns sorted iterable

newlst = sorted(animals)
# ['cat', 'cheetah', 'dog', 'rhino']

sorted(animals, reverse=True)
# ['rhino', 'dog', 'cheetah', 'cat']

animals = [
	{'type':'cat','name':'Stephanie','age':8},
	{'type':'dog','name':'Devon','age':3}
	{'type':'rhino','name':'Moe','age':5}
]

sorted(animals, key=lambda animal: animal['age'], reverse=True)

# Sort IN PLACE and returns None

animals.sort(key=lambda animal: animal['age']) 