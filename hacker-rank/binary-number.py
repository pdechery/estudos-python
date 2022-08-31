# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def divideOrSubtract(n):

    if n % 2 == 0:
        n = n / 2
    else:
        n = n - 1

    return n

def solution(S):
    
    operations = 0
    n = int(S,2)
    
    while n > 0:
        operations = operations + 1
        n = divideOrSubtract(n)

    return operations
    


if __name__ == '__main__':
    
    input = '011100'
    
    res = solution(input)
    print(res)