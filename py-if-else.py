#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    n = int(input())

    if n%2 != 0:
        print("Weird")

    elif n%2 == 0 and n>=2 and n<=5:
        print("Not Weird")

    elif n%2 == 0 and n>=6 and n<=20:
        print("Weird")

    elif n%2 == 0 and n>=20:
        print("Not Weird")
        
    # if n%2 != 0:
    #     print("Weird")
    # else:
    #     if 2 <= n <= 5:
    #         print("Not Weird")
    #     elif 6 <= n <= 20:
    #         print("Weird")
    #     elif n > 20:
    #         print("Not Weird")
