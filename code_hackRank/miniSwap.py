#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
   res = 0
   pos = 0
   while pos < len(arr):
       if(arr[pos] == (pos+1)):
           pos += 1
       else:
            move = arr[pos]-1
            arr[move], arr[pos] = arr[pos], arr[move]
            res += 1
   return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
