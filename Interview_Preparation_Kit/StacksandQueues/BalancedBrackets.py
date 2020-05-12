# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues
#!/bin/python3

import math
import os
import random
import re
import sys



# Complete the isBalanced function below.
def funcBalanced(semiBracket):
    if semiBracket == ')':
        return '('
    elif semiBracket == '}':
        return '{'
    else:
        return '['


def isBalanced(s):
    stack = []
    for semiBracket in s:
        if semiBracket in '{([':
            stack.append(semiBracket)
        elif len(stack) == 0:
            return 'NO'
        elif stack.pop() == funcBalanced(semiBracket):
            continue
        # elif stack.pop() in '})]':
        #     continue
        else:
            return 'NO'
    return 'YES' if len(stack) == 0 else 'NO'

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        print(result)
    #     fptr.write(result + '\n')
    #
    # fptr.close()

