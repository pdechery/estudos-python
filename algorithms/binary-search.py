# https://realpython.com/binary-search-python/#implementing-binary-search-in-python

def find_index(elements, value):
    '''
    Este algoritmo assume que os elementos da lista estão ordenados.
    '''
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            return middle

        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value:
            right = middle - 1


if __name__ == '__main__':
    
    um_array = [-1,0,3,5,9,12]
    print(find_index(um_array, 9))

    '''
    Na primeira iteração:

    value = 9
    elements = [-1,0,3,5,9,12]
    left = 0
    right = 5
    middle = 2

    elements[2] != 9

    elements[2] < 9, então:
    left = 2 + 1
    right = 5

    Segunda iteração do while.

    middle = 3 + 5 // 2 (4)

    Sucessiva incrementação do left.
    
    '''
