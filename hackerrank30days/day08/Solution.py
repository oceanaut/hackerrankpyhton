#!/bin/python3

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

