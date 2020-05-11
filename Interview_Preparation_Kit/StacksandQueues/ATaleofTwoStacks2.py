# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=stacks-queues
#!/bin/python3

import math
import os
import random
import re
import sys


class MyQueue(object):
    def __init__(self):
        self.inbound = []

    def peek(self):
        return self.inbound[0]

    def pop(self):
        del self.inbound[0]

    def put(self, value):
        self.inbound.append(value)


if __name__ == '__main__':
    q = MyQueue()
    for i in range(int(input())):
        s = input()
        if s == "3":
            print(q.peek())
        elif s == "2":
            q.pop()
        else:
            q.put(int(s[2:]))


