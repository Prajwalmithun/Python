# Exercise 18: Name, Variables , Code , Functions

#this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# *args is pointless we can just do this
def print_two_again(arg1, arg2):
    print("arg1: {arg1}, arg2: {arg2}")

#this just takes one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

#this doesnt take any arument
def print_none():
    print("I am nothing")

# function calls
print_two("Prajwal","Kushal")
print_two_again("kabir","khalidh")
print_one("Rocky!")
print_none()
