# https://www.hackerrank.com/challenges/symmetric-difference/problem

#!/bin/python3

if __name__ == '__main__':
    #a, b = [set(input().split()) for _ in range(4)][1::2]
    # print('\n'.join(sorted(a ^ b, key=int)))
    data = ""
    for line in sys.stdin:
        data += line
    print(data)


