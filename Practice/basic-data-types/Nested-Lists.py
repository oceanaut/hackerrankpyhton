#https://www.hackerrank.com/challenges/nested-list/problem

#!/bin/python3

gradelist = [[input(), float(input())] for _ in  range(int(input()))]
second_highest = sorted(list(set([grade for name, grade in gradelist])))[1]
print('\n'.join([a for a,b in sorted(gradelist) if b == second_highest]))
