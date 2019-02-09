#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter, OrderedDict

'''
https://www.hackerrank.com/challenges/most-commons/problem
'''

if __name__ == '__main__':
        s = input()
        class OrderedCounter(Counter, OrderedDict):
            pass
        [print(*c) for c in OrderedCounter(sorted(s)).most_common(3)]


