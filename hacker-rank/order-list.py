'''
Codility "Missing String"
'''

def solution(A):

    print(f'A: {A}')

    maxv = max(A)

    if maxv <= 0:
        return 1

    if maxv == 1:
        return 2

    numbers = sorted(list(set(A)))

    print(f'numbers: {numbers}')

    pointer = 0

    for i in range(len(numbers)):

        curr = numbers[i]

        if curr <= 0:
            continue

        pointer = pointer + 1

        print(f'curr: {curr}')
        print(f'pointer: {pointer}')

        if curr != pointer: 
            return pointer

    return maxv + 1



if __name__ == '__main__':
    
    input = [-1, -3]
    
    res = solution(input)
    print(res)