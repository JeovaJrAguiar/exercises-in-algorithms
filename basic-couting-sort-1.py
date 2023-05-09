#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    n = len(arr)
    arrRetorno = [0]
    for i in range(n-1):
        arrRetorno.append(0)

    for value in arr:
        arrRetorno[value] = arrRetorno[value] + 1
        
    return arrRetorno

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
