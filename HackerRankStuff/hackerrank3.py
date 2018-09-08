#!/bin/python3

# a HackerRank exercise re: conditional statements

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    N = int(input())

if N % 2 != 0:
    print("Weird")
elif N >= 2 and N < 5:
    print("Not Weird")
elif N >= 6 and  N <=20:
    print("Weird")
elif N > 20 and N % 2 == 0:
    print("Not Weird")