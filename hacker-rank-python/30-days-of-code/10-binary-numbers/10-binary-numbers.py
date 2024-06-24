#!/bin/python3

import math
import os
import random
import re
import sys

def counter_of(option, number_str):
    aux = 0

    while len(number_str) > 0 :
        aux += 1 if number_str[0] == option else 0
        number_str = number_str[1:]
    return aux

def to_binary(number):
    if number == 0 or number == 1:
        return str(number)
    
    return to_binary(number // 2) + str(number % 2)



if __name__ == '__main__':
    n = int(input().strip())
    number = str(to_binary(n))
    print(counter_of('1', number))
    