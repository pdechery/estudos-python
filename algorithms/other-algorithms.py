# Using Hash Tables (dict) to process lists.
# Remember dicts doesn't allow duplicate keys so we can take advantage of that.

fruits = ["orange","apple","orange","pea","cashew"]

# use dict to create list with unique values
# Algorithm time complexity: linear (O(n))

filter = dict()

for name in fruits:
	filter[name] = 0

result = filter.keys()
print(set(result))

# count values with hash table
# Algorithm time complexity: linear (O(n))
# time grows linearly according to the number of items in the list

counter = dict()

for name in fruits:
	if(name in counter.keys()):
		counter[name] += 1
	else:
		counter[name] = 1

print(counter) 





