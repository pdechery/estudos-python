def tryme():
	me = "eu"
	print("globals(): ", globals())
	print("locals(): ", locals())
	print("dir(): ", dir())

if __name__ == "__main__":
	tryme()
	print("let's see globals outside the function: ")
	print(globals())