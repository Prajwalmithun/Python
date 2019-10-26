# This script has following key points
# 1. append()
# 2. pop()   
# Both happens from the right end
# 3. split() to break a string into list
# 4. join()  to form a string from list

ten_things = "Car Bike cycle truck train bus aeroplane"

print("Wait there are less than 10 elementss in list. Lets fix it!")

# Breaking the sentence into list
stuff = ten_things.split(' ')
#print(stuff)
more_stuff = ["auto","rocket", "scooter", "trackor", "JCB"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    stuff.append(next_one)
    print("There are {} items now".format(len(stuff)))

print(stuff[1])
print(stuff[-1])
print(stuff.pop())

# Making sentence from list
print(' '.join(stuff))
print('#'.join(stuff[0:3]))

sentence = ' '.join(stuff)
print(sentence)