# https://www.hackerrank.com/challenges/the-minion-game/problem

#!/bin/python3



def minion_game(string):
    vowels = 'aeiou'.upper()
    strl = len(string)
    kevin = sum(strl-i for i in range(strl) if string[i] in vowels)
    stuart = strl*(strl + 1)/2 - kevin

    if kevin == stuart:
        print("Draw")
    elif kevin > stuart:
        print('Kevin %d' % kevin)
    else:
        print('Stuart %d' % stuart)

if __name__ == '__main__':
    s = input()
    minion_game(s)




