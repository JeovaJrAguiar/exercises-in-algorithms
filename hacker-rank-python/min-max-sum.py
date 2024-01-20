#!/bin/python3

import math
import os
import random
import re
import sys

def miniMaxSum(arr):
    arr.sort()
    min = 0
    max = 0
    
    for i, n in enumerate(arr):
        if i != 0:
            max = max+n
        if i != len(arr)-1:
            min = min+n
            
    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
