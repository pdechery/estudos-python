# Implement a merge sort with recursion


items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]

def merge_sort_recursion(arr):

    if len(arr) > 1:

        midpoint = len(arr) // 2
        L = arr[:midpoint]
        R = arr[midpoint:]

        merge_sort_recursion(L)
        merge_sort_recursion(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else: 
                arr[k] = R[j]
                j += 1
            k += 1


def merge_sort_two_arrays(arr1, arr2):
    
    # create indexes
    i = j = k = 0
    b = ['a','a','a','a','a']

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            b[k] = arr1[i]
            i += 1
        else:
            b[k] = arr2[j]
            j += 1
        k += 1

    return b


if __name__ == '__main__':
    
    #print(items)
    #merge_sort_recursion(items)
    res = merge_sort_two_arrays([3,8],[2,1])
    print(res)
    #print(items)