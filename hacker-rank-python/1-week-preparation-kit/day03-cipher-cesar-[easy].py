#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    alphaDown = 'abcdefghijklmnopqrstuvwxyz'
    alphaUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    result = ''
    
    k = k % 26
    
    for l in s:
        if l.isalpha():
            if l.isupper():
                indexAux = alphaUpper.index(l)
                result = result+alphaUpper[(indexAux+k)%26]
            else:
                print(l)
                indexAux = alphaDown.index(l)
                result = result+alphaDown[(indexAux+k)%26]
        else:
            result = result+l
        print(result)
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
