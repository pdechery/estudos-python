#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())
    if n > 1 and n < 100:
        if n % 2 != 0:
            print("Weird IMPAR")
        else:
            if n in range(2,5):
                print("Not Weird PAR entre 2 e 5")
            if n in range(6,20):
                print("Weird PAR entre 6 e 10")
            if n > 20:
                print("Not Weird PAR maior que 20")