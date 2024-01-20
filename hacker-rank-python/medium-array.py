#!/bin/python3

import math
import os
import random
import re
import sys

def missingNumbers(arr, brr):
    for value in arr:
        if value in arr:
            brr.remove(value)

    aux = brr
    print(aux.sort())
    return(aux)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
