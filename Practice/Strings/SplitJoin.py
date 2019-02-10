#https://www.hackerrank.com/challenges/python-string-split-and-join/problem

#!/bin/python3

def split_and_join(line):
    # write your code here
    #return line.replace(" ","-")
    return '-'.join(line.split())

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)