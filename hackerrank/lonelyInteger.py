#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    for val in a:
        if a.count(val) == 1:
            result = val
            print(result)
            
    """ repetidos = []
    a.sort()
    if len(a) == 1:
        return a[0]
    for x in a:
        if x not in repetidos:
            if x == a[-1]:
                print(x)
            repetidos.append(x) """

if __name__ == '__main__':

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)