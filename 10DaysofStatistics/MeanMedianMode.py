#https://www.hackerrank.com/challenges/s10-basic-statistics/problem

#!/bin/python3

import numpy as np
from scipy import stats


if __name__ == '__main__':
     n = input()
     list1 = list(map(int, input().split()))
     print(np.mean(list1))
     print(np.median(list1))
     print(stats.mode(list1)[0][0])
