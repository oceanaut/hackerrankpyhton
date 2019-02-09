#!/bin/python3

"""
https://www.hackerrank.com/challenges/validate-a-roman-number/problem
"""
import re
# Enter your code here. Read input from STDIN. Print output to STDOUT
regex_pattern = r'M{0,3}'+'(C[MD]|D?C{0,3})'+'(X[CL]|L?X{0,3})'+'(I[VX]|V?I{0,3})'+'$'
# Do not delete 'r'.
print(str(bool(re.match(regex_pattern, input()))))

