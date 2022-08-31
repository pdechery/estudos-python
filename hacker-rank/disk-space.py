#!/bin/python3

import math
import os
import random
import re
import sys

'''
Disk Space Analysis 

A company is performing an analysis on the computers at its main office. 

The computers are spaced along a single row. The analysis is performed in the following way:
    
    1. Choose a contiguous segment of a certain number of computers, starting from the beginning of the row. 
    2. Analyze the available hard disk space on each of the computers. 
    3. Determine the minimum available disk space within this segment. 

After performing these steps for the first segment, it is then repeated for the next segment, continuing this procedure until the end of the row (i.e. if the segment size is 4, compu 1 to 4 would be analyzed, then 2 to 5, etc.) 

Given this analysis procedure, find the maximum available disk space among all the minima that are found during the analysis. 

Example n = 3, the number of computers space = [8, 2, 4] x = 2, the length of analysis segments 

In this array of computers, the subarrays of size 2 are [8, 2] and [2, 4]. 

Thus, the initial analysis returns 2 and 2 because those are the minima for the segments. 

Finally, the maximum of these values is 2. Therefore, the answer is 2. 

Complete the 'segment' function below.

The function is expected to return an INTEGER.
The function accepts following parameters:
    
    1. INTEGER x
    2. INTEGER_ARRAY space

'''


def segment(x, space):

    print(f'space: {space}')

    mins = []

    for i in range(len(space)):

        if (i+1) >= len(space):
            break

        seg = space[i:i+x]

        print(f'seg: {seg}')

        mins.append(min(seg))

    return max(mins)


if __name__ == '__main__':

    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # x = int(input().strip())

    # space_count = int(input().strip())

    # space = []

    # for _ in range(space_count):
    # space_item = int(input().strip())
    # space.append(space_item)

    # result = segment(x, space)

    # fptr.write(str(result) + '\n')

    # fptr.close()

    result = segment(2,[2, 5, 4, 6, 8])

    print(result)