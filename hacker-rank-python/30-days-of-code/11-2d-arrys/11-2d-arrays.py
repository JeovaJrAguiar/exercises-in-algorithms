#!/bin/python3

import math
import os
import random
import re
import sys

def max_hourglasses(arr):
    max_sum = -float('inf')
    
    for i in range(4):
        for j in range(4):
            sum = (
                arr[i][j] + 
                arr[i][j+1] + 
                arr[i][j+2] + 
                arr[i+1][j+1] + 
                arr[i+2][j] + 
                arr[i+2][j+1] + 
                arr[i+2][j+2]
                )
            
            if sum > max_sum:
                max_sum = sum
            
    
    return max_sum
    

if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
        
    result = max_hourglasses(arr)
    print(result)
