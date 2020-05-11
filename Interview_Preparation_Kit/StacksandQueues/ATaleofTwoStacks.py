# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=stacks-queues
#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    q = []
    for i in range(int(input())):
        s = input()
        if s == "3":
            print(q[0])
        elif s == "2":
            q.pop(0)
        else:
            q.append(int(s[2:]))


