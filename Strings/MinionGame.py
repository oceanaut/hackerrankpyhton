# https://www.hackerrank.com/challenges/the-minion-game/problem

#!/bin/python3



def minion_game(string):
    s, v = string, 'AEIOU'
    stuart, kevin, ln = 0, 0, len(s)

    for i in range(ln):
        if s[i] in v:
            kevin += ln - i
        else:
            stuart += ln - i

    if stuart > kevin:
        print('Stuart %d' % stuart)
    elif stuart == kevin:
        print('Draw')
    else:
        print('Kevin %d' % kevin)

if __name__ == '__main__':
    s = input()
    minion_game(s)




