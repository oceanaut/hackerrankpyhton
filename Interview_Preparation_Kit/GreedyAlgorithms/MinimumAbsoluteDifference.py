# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=greedy-algorithms

#!/bin/python3

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference1(arr):
    srt_arr = sorted(arr)
    min_dist = abs(srt_arr[0] - srt_arr[1])
    for i in range(1, len(srt_arr) - 1):
        min_dist = abs(srt_arr[i] - srt_arr[i + 1]) if abs(srt_arr[i] - srt_arr[i + 1]) < min_dist else min_dist
    return min_dist

def minimumAbsoluteDifference(arr):
    srt_arr = sorted(arr)
    min_dist=999999999
    for i in range(0, len(srt_arr) - 1):
        min_dist = abs(srt_arr[i] - srt_arr[i + 1]) if abs(srt_arr[i] - srt_arr[i + 1]) < min_dist else min_dist
    return min_dist

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    result = minimumAbsoluteDifference(arr)
    print(result)
    # fptr.write(str(result) + '\n')
    # fptr.close()