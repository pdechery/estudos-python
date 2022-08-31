#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime as dt

'''
https://www.hackerrank.com/challenges/python-time-delta/problem

Sample Input:

2
Sat 02 May 2015 19:54:36 +0530
Fri 01 May 2015 13:54:36 -0000

'''

# Complete the time_delta function below.
def time_delta(t1, t2):

    print(f't1: {t1}')
    print(f't2: {t2}')

    format = "%a %d %b %Y %H:%M:%S %z"
    
    time1 = dt.strptime(t1,format)
    time2 = dt.strptime(t2,format)

    print(f'time1: {time1}')
    print(f'time2: {time2}')
    print(f'type: {type(time2)}')
    
    res = time1 - time2

    print(f'res: {res}')
    print(f'type: {type(res)}')
    print(f'total_seconds: {res.total_seconds()}')

    res = abs(int(res.total_seconds()))
    
    return str(res)

if __name__ == '__main__':
    
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()