#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    reverseArray = []
    while n != 0:
        reverseArray.append(arr.pop())
        n = n-1

    for num in reverseArray:
        print(num, end=" ")
    
