# Find the greatest common denominator of two numbers
# using Euclid's algorithm

def gcd(a,b):
	while(b != 0):
		t = a
		a = b
		b = t % b

	return a

if __name__ == '__main__':
	
	print(gcd(20,8))