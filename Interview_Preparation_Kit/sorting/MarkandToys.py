# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

#!/bin/python3

# Complete the maximumToys function below.
def maximumToys1(prices, k):
    sum=0
    count=0
    prices.sort()
    for i in range(len(prices)):
        sum += prices[i]
        if sum <= k:
            count += 1
        else:
            break
    return count

def maximumToys2(prices, k):
    i = 1
    prices.sort()
    while sum(prices[:i]) < k:
        i += 1
    return i-1

def maximumToys(prices, k):
    sum = 0
    prices.sort()
    for i, item in enumerate(prices):
        sum += item
        if sum > k:
            return i

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    print(result)

    # fptr.write(str(result) + '\n')
    # fptr.close()