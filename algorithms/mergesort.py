# Implement a merge sort with recursion


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


def merge_sort_two_arrays(l_arr, r_arr):
    
    # create indexes
    l = r = k = 0
    res = list()

    while l < len(l_arr) and r < len(r_arr):
        if l_arr[l] < r_arr[r]:
            res.insert(k, l_arr[l]) 
            l += 1
        else:
            res.insert(k, r_arr[r]) 
            r += 1
        k += 1

    while l < len(l_arr):
        res.insert(k, l_arr[l])
        k += 1
        l += 1

    while r < len(r_arr):
        res.insert(k, r_arr[r]) 
        k += 1
        r += 1

    return res


if __name__ == '__main__':

    #items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]
    items = [3,8,2,1,15]
    
    #print(items)
    merge_sort_recursion(items)
    #res = merge_sort_two_arrays([3,8],[2,1])
    #print(res)
    #print(items)