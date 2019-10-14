# Exercise 8: Printing, printing

formatter = "{} {} {} {}"

#ouput of each print looks like the above format
print(formatter.format(1,2,3,4))
print(formatter.format("one","two","three","four"))
print(formatter.format(True,False,True,False))
print(formatter.format(formatter,formatter,formatter,formatter))
print(formatter.format(
    "Hello",
    "Everyone",
    "Look whos here",
    "Come on bro!"
))
