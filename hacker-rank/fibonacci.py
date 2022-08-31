cube = lambda x: x*x*x

def fibonacci(n):

    seq = [0,1]

    for index in range(n):

        print(f'index: {index}')
        print(f'index: {index+1}')

        val1 = seq[index]
        val2 = seq[index+1]

        seq.append(val1 + val2)

        print(f'seq: {seq}')

    return seq[0:n]

def fibonacci_maneiro(n):

    a,b = 0,1

    print(a)

    for _ in range(n):
        
        a, b = b, a+b

        print(a)


if __name__ == '__main__':
    
    # n = int(input())
    
    # print(list(map(cube, fibonacci(n))))

    # print(list(map(cube, fibonacci(5))))

    fibonacci_maneiro(5)