#Exercise 13: Parameters , Unpacking,Variables

#sys for command-line arguments
from sys import argv

#Unpacking argv
scrip , first , second , third = argv

print("Script Name: ",scrip)
print("Your first variable: ",first)
print("Your second variable: ",second)
print("Your third variable: ",third)


#NOTE: by default the command-line arguments are strings.