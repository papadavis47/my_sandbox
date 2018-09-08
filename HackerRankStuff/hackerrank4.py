# this is an exercise to create a simple for loop on HackerRank 30 Days of Code

#!/bin/python3


import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

for i in range(1, 11):
    result = n * i
    print(str(n)+ " x " + str(i) + " = " + str(result))