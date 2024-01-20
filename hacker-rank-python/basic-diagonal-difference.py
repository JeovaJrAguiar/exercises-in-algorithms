#!/bin/python3

import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    diagleft = 0
    diagright = 0
    
    i = 0
    j = len(arr[0])
    for index, value in enumerate(arr):
        diagleft +=  value[i]
        diagright += value[j-1]
        
        i+=1
        j-=1
    
    return abs(diagleft-diagright)        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
