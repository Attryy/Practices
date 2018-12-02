#!/bin/python

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    # check for constraints
    if (n<1 or n > 100):
        print("The number of socks should be between 1 and 100")
    else:
        colors = set(ar)
        res = []
        for color in colors:
            if(color <1 or color >100 ):
                print("The colors should be between 1 and 100.")
                break;
            else:
                 res.append(sum(i == color for i in ar))
        out = int(sum(math.floor(i/2) for i in res))
        return(out)


                


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(raw_input())

    ar = map(int, raw_input().rstrip().split())

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
