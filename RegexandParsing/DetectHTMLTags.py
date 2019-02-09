#!/bin/python3

"""
https://www.hackerrank.com/challenges/detect-html-tags-attributes-and-attribute-values/problem
"""
# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        [print('-> {} > {}'.format(*attr)) for attr in attrs]


if __name__ == '__main__':
    html = '\n'.join([input() for _ in range(int(input()))])
    parser = MyHTMLParser()
    parser.feed(html)
    parser.close()
