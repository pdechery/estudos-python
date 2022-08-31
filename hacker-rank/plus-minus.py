#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    positive = [i for i in arr if i > 0]
    negative = [i for i in arr if i < 0]
    zero = [i for i in arr if i == 0]

    ratio_p = len(positive) / len(arr)
    ratio_n = len(negative) / len(arr)
    ratio_z = len(zero) / len(arr)

    print(f'{ratio_p:.6f}')
    print(f'{ratio_n:.6f}')
    print(f'{ratio_z:.6f}')


if __name__ == '__main__':
    #n = int(input().strip())

    #arr = list(map(int, input().rstrip().split()))

    arr = [-4,3,-9,0,4,1]

    plusMinus(arr)