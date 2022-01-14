#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    valley_counter = 0
    sea_level = 0
    
    for i in range(steps):
        if sea_level == 0:
            if path[i] == "U":
                sea_level += 1
            else:
                sea_level -= 1
                valley_counter += 1
        else:
            if path[i] == "U":
                sea_level += 1
            else:
                sea_level -= 1
    return valley_counter

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
