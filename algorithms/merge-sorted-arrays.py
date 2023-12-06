def merge_sorted_arrays(A, B):

    print("A", A)
    print("B", B)

    A_len = len(A)
    B_len = len(B)

    Z = [0] * (A_len + B_len)

    l, r, count = 0, 0, 0
    
    while l < A_len and r < B_len:
        if A[l] > B[r]:
            print("R", B[r])
            Z[count] = B[r]
            r += 1
        else:
            print("L", A[l])
            Z[count] = A[l]
            l += 1
        count += 1

    while l < A_len:
        print("adding L", A[l])
        Z[count] = A[l]
        count += 1
        l += 1

    while r < B_len:
        print("adding R", B[r])
        Z[count] = B[r]
        count += 1
        r += 1

    print("final Z", Z)


A = [13,24,45,99,102]
B = [1,2,5,9,68]
merge_sorted_arrays(A,B)