#!/bin/python3

import math
import os
import random
import re
import sys

def timeConversion(s):
    hour = s[:8]
    fuso = s[8:]
    aux = int(hour[:2])
    
    if fuso == 'AM':
        if aux == 12:
            aux = 0
    else:
        if aux != 12:
            aux = aux+12
    
    
    if aux < 10:
        return '0'+str(aux)+hour[2:8]
    else:
        return str(aux)+hour[2:8]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
