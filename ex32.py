the_count = [1, 2, 3, 4, 5]
fruits = ['apple', 'banana', 'orange']
change = [1, 'paise', 2, 'rupee']

# for loop goes through the list the_count
for number in the_count:
    print("This is the count {}".format(number))

print('-----------------------------')
# for loop goes through the list fruits
for fruit in fruits:
    print("The fruit name is {}".format(fruit))

print('------------------------------')
# We can also go through the mixed list
for i in change:
    print("I got {}".format(i))

print('-------------------------------')
# Building the new list from scratch
elements = []

for i in range(0,6):
    elements.append(i)

#updated list
print(elements)

print('--------------------------------')
#Another way to print the list
for i in elements:
    print("Element is : {}".format(i))