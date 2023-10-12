def validateString(S):
	
	validators = ['isalnum','isalpha','isdigit','islower','isupper']
	
	for val in validators:

		result = "False"   
		
		for s in S:
			
			validation = f'"{s}".{val}()'

			if eval(validation):
				#print(f'{s} did pass {val}')
				result = "True"
				break

		#print(f'{string} testando {val}')
		print(result)
    
       
if __name__ == '__main__':
    
    # ATTENTION: input() is a builtin for grabbing user input on console! 
    # is not to be used as user function!
    s = input()

    #validateString(s)

    # other cool ways of doing the same thing I did above:

    for method in [str.isalnum, str.isalpha, str.isdigit, str.islower, str.isupper]:

    	cool_result = {method(ch) for ch in s}

    	# any() returns True if any item is True
    	print(any(cool_result))

