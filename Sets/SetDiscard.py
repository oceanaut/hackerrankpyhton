# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

#!/bin/python3

if __name__ == '__main__':
    n = int(input())
    s = set(map(int, input().split()))
    number_of_lines = int(input())
    for _ in range(number_of_lines):
        choice = input().split()
        if choice[0] == "pop":
            s.pop()
        elif choice[0] == "remove":
            s.remove(int(choice[1]))
        elif choice[0] == "discard":
            s.discard(int(choice[1]))
    print(sum(s))
