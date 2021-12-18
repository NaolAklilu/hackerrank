#!/bin/python3

import math
import os
import random
import re
import sys

def countingSort(arr):
    count = []
    for i in range(0, len(arr)):
        count.append(0)
    
    for j in range(0, len(arr)):
        count[arr[j]] = count[arr[j]] + 1
    
    return count



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
