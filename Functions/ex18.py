#You can create a function by using the word def in Python.
def print_two(*args):
    print(*args)
    arg1, arg2 = args
    print("arg1  ",arg1," arg2 ",arg2)

#other way of passing arguments
def print_one(arg1, arg2):
    ar1, ar2 = arg1, arg2
    print("in print_one() "+"arg1  ",ar1," arg2 ",ar2)

#one more way
def prints(arg1):
    ar1 = arg1
    print("In prints() "+"arg1   ", ar1)

#no way
def printss():
    print("None")

print_two("Rishab Mehrotra", 24)
print_one("rishab", "data engineer")
prints("lucknow")
printss()