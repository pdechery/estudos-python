def fizzBuzz(n):
    
    for i in range(1,n+1):
        
        #print(f'i: {i}')
        #print(f'type(i): {type(i)}')
        
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0) and not (i % 5 == 0):
            print("Fizz")
        elif (i % 5 == 0) and not (i % 3 == 0):
            print("Buzz")
        elif (i % 3 != 0) or (i % 5 != 0):
            print(i)
    

if __name__ == '__main__':
    n = int(input().strip())

    fizzBuzz(n)