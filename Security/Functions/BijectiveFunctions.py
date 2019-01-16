#https://www.hackerrank.com/challenges/security-bijective-functions/problem

#!/bin/python3
def is_bijection(seq1, seq2):
    distinct1 = set(seq1)
    distinct2 = set(seq2)
    distinctMappings = set(zip(seq1, seq2))
    return len(distinct1) == len(distinctMappings) and len(distinct2) == len(distinctMappings)

if __name__ == '__main__':
    print ('YES') if int(input()) == len(set(map(int, input().split(' ')))) else print('NO')