cube = lambda x: x*x*x


def fibonacci_basic(n):

    primeiro = 0
    segundo = 1
    count = 1
    
    while count <= n:
        print(f'primeiro {primeiro}')
        print(f'segundo {segundo}')
        print('----')
        fibo = primeiro + segundo
        primeiro = segundo
        segundo = fibo
        count += 1

    return fibo


def fibonacci_unpacking(n):
    '''
    Este exemplo usa iterable unpacking (tupla)
    '''

    a,b = 0,1

    for _ in range(n):

        print(f'a {a}')
        print(f'b {b}')
        print('---------')
        
        a, b = b, a+b

    return b


def fibonacci_sequence(n):

    seq = [0,1]

    for index in range(n):

        val1 = seq[index]
        val2 = seq[index+1]

        seq.append(val1 + val2)

    return seq[0:n]


if __name__ == '__main__':
    
    # n = int(input())

    # print(list(fibonacci(7)))
    
    # print(list(map(cube, fibonacci(n))))

    # print(list(map(cube, fibonacci(5))))

    # print(fibonacci_maneiro(7))

    print(fibonacci_basic(7))