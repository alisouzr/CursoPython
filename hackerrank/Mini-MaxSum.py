#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    newArr = []
    minValue = 0
    maxValue = 0
    for x in arr:
        newArr.append(x)
    newArr.remove(min(newArr))
    arr.remove(max(arr))
    for x in arr:
        minValue+=x
    for a in newArr:
        maxValue+=a
    print(minValue, maxValue)
    
if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
