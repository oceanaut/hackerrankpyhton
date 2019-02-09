#!/bin/python3

'''
https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
The map() function applies a function to every member of an iterable and returns the result.
Lambda is a single expression anonymous function often used as an inline function. 
It is a function that has only one line in its body. It proves very handy in functional and GUI programming. 
Lambda can be used inside lists and dictionarie
Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself
'''

cube = lambda x: x ** 3 # complete the lambda function

def fibonacci(n):
    # return a list of fibonacci numbers
    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))


