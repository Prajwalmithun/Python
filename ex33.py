items = []

print("-------------------")
print("While loop")

i=0
while i < 10:
    items.append(i)
    print("The value of i is : {}".format(i))
    i=i+1

print("------------------")

a=0
def while_conversion(a,var):
    if a<var:
        print("Inside the function")
        while_conversion(a+1,var)
    
while_conversion(0,6)


print("------------------")
print("For loop")
for x in items:
    print(x)