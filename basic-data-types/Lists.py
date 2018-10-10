#https://www.hackerrank.com/challenges/python-lists/problem

#!/bin/python3

if __name__ == '__main__':
    N = int(input())
    lis=[]
    for _ in range(N):
        s = input().split()
        if s[0]=="insert":
            lis.insert(int(s[1]),int(s[2]))
        elif s[0]=="append":
            lis.append(int(s[1]))
        elif s[0]=="sort":
            lis.sort()
        elif s[0]=="reverse":
            lis.reverse()
        elif s[0]=="pop":
            lis.pop(-1)
        elif s[0]=="remove":
            if int(s[1]) in lis:
                lis.remove(int(s[1]))
        elif s[0]=="print":
            print(lis)

