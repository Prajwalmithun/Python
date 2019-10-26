print("""You want to go 
DOOR #1 or DOOR #2""")

door = input("> ")

if door == '1':
    print("There's a giant bear here eating something")
    print("What do you do ?")
    print("1. Eat cake ")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == '1':
        print("The bear eats your face off, Good job!")
    elif bear == '2':
        print("The bear eats your legs, Good job!")
    else:
        print(f"Well done {bear} is probably better")
        print("Bear runs away")

elif door == "2":
    print("1. Blueberries ")
    print("2. Yellow jacket clothespins. ")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == '1' or insanity == '2':
        print("one")
    else:
        print("two")

else:
    print("Wrng choice")