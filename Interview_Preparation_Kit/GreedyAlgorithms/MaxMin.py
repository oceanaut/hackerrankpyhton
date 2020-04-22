# https://www.hackerrank.com/challenges/angry-children/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms
# !/bin/python3
import sys
# Complete the maxMin function below.
def maxMin(k, arr):
    arr.sort()
    a = 0
    diff = 0
    min = sys.maxsize
    while( a < (len(arr)-k +1) ):
        diff = arr[a+k-1] - arr[a]
        if(diff < min):
              min = diff
        a +=1
    return min

def maxMin1(k, arr):
    unfair = sys.maxsize
    arr.sort()
    for j in range(n-k+1):
        if arr[j+k-1] - arr[j] <= unfair:
            unfair = arr[j+k-1] - arr[j]
    return unfair

def maxMin2(k, arr):
    unfair = sys.maxsize
    arr.sort()
    for j in range(len(arr)-k+1):
        unfair = min(unfair, (arr[j+k-1]-arr[j]) )
    return unfair

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    k = int(input())
    arr = []
    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)
    result = maxMin(k, arr)
    print(result)

    # fptr.write(str(minimumCost) + '\n')
    # fptr.close()
