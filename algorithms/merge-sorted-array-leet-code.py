class Solution:
    @staticmethod
    def merge(nums1:list, m:int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # mums1 length IS ALWAYS m+n
        # I should merge the first m elements in nums1
        # I should ignore the last n elements in nums1

        l = 0
        r = 0
        c = 0

        numscopy = [i for i in nums1]
        
        while l < m and r < n:
            if numscopy[l] > nums2[r]:
                nums1[c] = nums2[r]
                r += 1
            else:
                nums1[c] = numscopy[l]
                l += 1
            c += 1

        while l < m:
            nums1[c] = numscopy[l]
            l += 1
            c += 1

        while r < n:
            nums1[c] = nums2[r]
            r += 1
            c += 1

        print(nums1)


A = [1,2,3,0,0,0]
B = [2,5,6]
m,n = 3,3

Solution.merge(A,m,B,n)