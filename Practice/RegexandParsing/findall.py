#!/bin/python3

"""
https://www.hackerrank.com/challenges/re-findall-re-finditer/problem
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
s = '[qwrtypsdfghjklzxcvbnm]'
a = re.findall('(?<=' + s +')([aeiou]{2,})' + s, input(), re.I)
print('\n'.join(a or ['-1']))

