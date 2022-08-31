#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here

    sums = []

    sub = arr

    for i in arr:
        sub = arr.copy()
        sub.remove(i)
        #print(f'sub: {sub}')
        sums.append(sum(sub))
        #print(f'arr: {arr}')

    print(f'{int(min(sums))} {int(max(sums))}')


if __name__ == '__main__':

    #arr = list(map(int, input().rstrip().split()))

    arr = [1,2,3,4,5]

    miniMaxSum(arr)
