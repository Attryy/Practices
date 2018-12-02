#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    #print(q)
     op =0
   #print(length)
     if any([(m-l)>3 for l, m in enumerate(q)]):
         print( "Too chaotic")
     else:
         for a in range(len(q)-1, -1, -1):
              for b in range(max(0,q[a]-2), a):
                 if(q[b]> q[a]):
                  op+= 1
                  res_2 = op
         print(res_2)
            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
