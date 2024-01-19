#!/bin/python3

import math
import os
import random
import re
import sys

def lonelyinteger(a):
    element = -1
    for i in a:
        ocorrencia = 0
        for j in a:
            if i == j:
                ocorrencia += 1
        if ocorrencia == 1:
            element = i
        
    return element 

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
