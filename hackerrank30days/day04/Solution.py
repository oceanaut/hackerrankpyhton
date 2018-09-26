#https://www.hackerrank.com/challenges/30-class-vs-instance/problem
class Person:
    age = 0
    def __init__(self,initialAge):
        # Add some more code to run some checks on initialAge
        if initialAge>0: age=initialAge
        if initialAge<0: print("Age is not valid, setting age to 0.")
    def amIOld(self):
        # Do some computations in here and print out the correct statement to the console
        if age < 13 : print("You are young.")
        if age in range(13,18): print("You are a teenager.")
        if age >= 18 : print("You are old.")
    def yearPasses(self):
        # Increment the age of the person in here
        global age
        age+=1
t = int(input())
for i in range(0, t):
    age = int(input())
    p = Person(age)
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()
    p.amIOld()
    print("")