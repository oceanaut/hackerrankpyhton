#!/bin/python3

'''
https://www.hackerrank.com/challenges/validate-list-of-email-address-with-filter/problem
 A Lambda function can be used with filters.
'''

def fun(s):
    # return True if s is a valid email, else return False
    try:
        username, url = s.split("@")
        website, extension = url.split(".")
    except ValueError:
        return False
    if not username.replace("-", "").replace("_", "").isalnum():
        return False
    elif not website.isalnum():
        return False
    elif len(extension) > 3:
        return False
    return True


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


