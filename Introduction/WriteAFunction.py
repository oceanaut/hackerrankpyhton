#https://www.hackerrank.com/challenges/write-a-function/problem
import calendar
def is_leap(year):
    leap = False

    # Write your logic here
    # return year % 4 == 0 and (year % 400 == 0 or year % 100 != 0)
    return calendar.isleap(year)


year = int(input())
print(is_leap(year))
