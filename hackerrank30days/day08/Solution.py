#!/bin/python3

#Task
#Given names and phone numbers, assemble a phone book that maps friends' names to their respective phone numbers. You will then be given an unknown number of names to query your phone book for. For each queried, print the associated entry from your phone book on a new line in the form name=phoneNumber; if an entry for is not found, print Not found instead.
#Note: Your phone book should be a Dictionary/Map/HashMap data structure.
#https://www.hackerrank.com/challenges/30-dictionaries-and-maps/problem

if __name__ == '__main__':
    n = int(input())
    name_numbers_list = [input().strip().split() for i in range(n)]
    phone_book = {k: v for k,v in name_numbers_list}
    while True:
        try:
            name = input().strip()
            if name in phone_book:
                print("{}={}".format(name, phone_book[name]))
            else:
                print('Not found')
        except:
            break

