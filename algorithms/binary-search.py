# https://realpython.com/binary-search-python/#implementing-binary-search-in-python

def find_index(elements, value):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        print(f'left {left}')
        print(f'middle {middle}')

        if elements[middle] == value:
            return middle

        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value:
            right = middle - 1


if __name__ == '__main__':
    
    um_array = [-1,0,3,5,9,12]
    print(find_index(um_array, 9))