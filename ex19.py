# Exercise 19: Functions and Variables

# Different ways of calling a function

# A function for printing the cheese and cracker boxes count
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get a blanket\n")

# Function call with numbers directly
print("We can give the function numbers directly")
cheese_and_crackers(20,30)

# With variables
print("OR we can use variables from our script")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# You can do math also
print("We can even do math inside too..")
cheese_and_crackers(10+20,5+8)

# You can do math and variable simultaneoulsy
print("We can combine the two, variables and math: ")
cheese_and_crackers(amount_of_cheese+10, amount_of_crackers+20)

# Get the input from the user
cheese_number = int(input("Enter the cheese count : "))
cracker_box = int(input("Enter the cracker box count : "))
cheese_and_crackers(cheese_number,cracker_box)