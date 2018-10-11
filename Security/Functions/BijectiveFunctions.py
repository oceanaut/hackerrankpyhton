#https://www.hackerrank.com/challenges/security-tutorial-functions/problem

#!/bin/python3
print ('YES') if int(input()) == len(set(map(int, input().split(' ')))) else print('NO')