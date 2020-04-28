# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search
# !/bin/python3

import os
import sys


# Complete the triplets function below.
def triplets(a, b, c):
    a = sorted(list(set(a)))
    b = sorted(list(set(b)))
    c = sorted(list(set(c)))
    count = 0
    p1 = 0  # p is an element of a
    p2 = 0
    p3 = 0
    prev_c2 = 0
    prev_c3 = 0
    while p2 < len(b):
        c2 = 0
        c3 = 0
        while p1 < len(a) and a[p1] <= b[p2]: # q => p
            c2 += 1
            p1 += 1
        while p3 < len(c) and c[p3] <= b[p2]: # q => r
            c3 += 1
            p3 += 1
        count += ((prev_c2 + c2) * (prev_c3 + c3))
        prev_c2 +=c2
        prev_c3 +=c3
        p2 += 1
    return count


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()
    lena = int(lenaLenbLenc[0])
    lenb = int(lenaLenbLenc[1])
    lenc = int(lenaLenbLenc[2])
    arra = list(map(int, input().rstrip().split()))
    arrb = list(map(int, input().rstrip().split()))
    arrc = list(map(int, input().rstrip().split()))
    ans = triplets(arra, arrb, arrc)
    print(ans)

    # fptr.write(str(ans) + '\n')
    # fptr.close()
