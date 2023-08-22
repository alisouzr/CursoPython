# /usr/bin/python3


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
    # Write your code here
    positive = 0
    negative = 0
    other = 0
    size = 0
    for x in arr:
        size += 1
        if x > 0:
            positive += 1
        elif x < 0:
            negative += 1
        else:
            other += 1
    print(f'{round(positive/size,6)}\n{round(negative/size,6)}\n{round(other/size,6)}')


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
