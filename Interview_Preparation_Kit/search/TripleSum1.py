# https://www.hackerrank.com/challenges/triple-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=search
# !/bin/python3

import os
import sys

def binary_search(arr, key):
    index = -1
    low = 0
    high = len(arr) - 1

    while high >= low:
        mid = low + (high - low) // 2
        if key >= arr[mid]:
            index = mid
            low = mid + 1
        else:
            high = mid - 1

    return index

# Complete the triplets function below.
def triplets(a, b, c):
    a = list(sorted(set(a)))
    b = list(sorted(set(b)))
    c = list(sorted(set(c)))

    triplets = 0

    for number in b:
        a_pos = binary_search(a, number) + 1
        c_pos = binary_search(c, number) + 1
        triplets += a_pos * c_pos

    return triplets


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
