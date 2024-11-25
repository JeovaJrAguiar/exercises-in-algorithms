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
    positive = len([x for x in arr if x > 0])
    zero = len([x for x in arr if x == 0])
    negative = len([x for x in arr if x < 0])
    total = len(arr)
    
    positive = positive / total
    negative = negative / total
    zero = zero / total
    
    print(positive)
    print(negative)
    print(zero)

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
