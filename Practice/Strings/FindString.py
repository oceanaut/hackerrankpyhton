#https://www.hackerrank.com/challenges/find-a-string/problem

#!/bin/python3
def count_substring(string, sub_string):
    return sum(1 for i in range(len(string)) if sub_string in string[i:i+len(sub_string)] and len(string) in range(1,201) )
if __name__ == '__main__':
     string = input().strip()
     sub_string = input().strip()
     count = count_substring(string, sub_string)
     print(count)