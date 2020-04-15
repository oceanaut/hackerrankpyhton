# https://www.hackerrank.com/challenges/ctci-bubble-sort/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=sorting

#!/bin/python3

# Complete the countSwaps function below.
def countSwaps(a):
    # Complete the countSwaps function below.
    def countSwaps(a):
        counter = 0
        for i in range(len(a)):
            for j in range(len(a) - 1):
                if (a[j] > a[j + 1]):
                    a[j], a[j + 1] = a[j + 1], a[j]
                    counter += 1
        print('Array is sorted in {} swaps.'.format(counter))
        print('First Element:', a[0])
        print('Last Element:', a[-1])

    n = int(input())
    a = list(map(int, input().rstrip().split()))
    countSwaps(a)