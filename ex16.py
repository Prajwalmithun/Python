# exercise 16: Reading and Writing Files

from sys import argv

script, filename = argv

print(f"We are going to erase {filename}")
print("If you dont want that hit CTRL-C (^C)")
print("If you do want that hit RETURN")

input("?")

print("Opening the file....")
target = open(filename,'w')

print("Deleting the file...,BYE")
target.truncate()

print("Now I am going to ask 3 question ")

line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

print("And finally , we close it.")
target.close()