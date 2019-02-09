#!/bin/python3

"""
https://www.hackerrank.com/challenges/introduction-to-regex/problem
"""

import re
regex_pattern = r"[.,]+"	# Do not delete 'r'.
if __name__ == '__main__':
    print("\n".join(re.split(regex_pattern, input())))
