# https://www.hackerrank.com/challenges/ctci-queue-using-two-stacks/problem?h_l=interview&playlist_slugs[]=interview-preparation-kit&playlist_slugs[]=stacks-queues
#!/bin/python3

import math
import os
import random
import re
import sys


class Stack:
    def __init__(self):
        self._stack = []

    def peek(self):
        if self._stack:
            return self._stack[-1]
        return None

    def pop(self):
        if self._stack:
            return self._stack.pop(-1)
        return None

    def put(self, value):
        self._stack.append(value)

    def __len__(self):
        return len(self._stack)


class MyQueue(object):
    def __init__(self):
        # Modes
        self._STACK_MODE = "stack"
        self._QUEUE_MODE = "queue"

        # Stacks and access data
        self._stacks = [Stack(), Stack()]
        self._curr = 0
        self._mode = self._STACK_MODE

    def peek(self):
        if self._mode == self._STACK_MODE:
            curr = self._curr
            other = 1 if curr == 0 else 0
            while len(self._stacks[curr]) > 0:
                top = self._stacks[curr].pop()
                self._stacks[other].put(top)
            self._curr = other
            self._mode = self._QUEUE_MODE

        return self._stacks[self._curr].peek()

    def pop(self):
        if self._mode == self._STACK_MODE:
            curr = self._curr
            other = 1 if curr == 0 else 0
            while len(self._stacks[curr]) > 0:
                top = self._stacks[curr].pop()
                self._stacks[other].put(top)
            self._curr = other
            self._mode = self._QUEUE_MODE

        return self._stacks[self._curr].pop()

    def put(self, value):
        if self._mode == self._QUEUE_MODE:
            curr = self._curr
            other = 1 if curr == 0 else 0
            while len(self._stacks[curr]) > 0:
                top = self._stacks[curr].pop()
                self._stacks[other].put(top)
            self._curr = other
            self._mode = self._STACK_MODE

        self._stacks[self._curr].put(value)

if __name__ == '__main__': # tests fail
    q = MyQueue()
    for i in range(int(input())):
        s = input()
        if s == "3":
            #print(q[0])
            print(q.peek())
        elif s == "2":
            #q.pop(0)
            q.pop()
        else:
            #q.append(int(s[2:]))
            q.put(int(s[2:]))

