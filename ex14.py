# Exercise 14: Prompting and Passing

from sys import argv

script,first_name,second_name = argv
prompt = '"'

print(f"Hi {first_name} {second_name}, I'm the {script} script")
print("I'd like to ask you a few questions.")
print(f"Do you like me {first_name} {second_name}?")
likes = input(prompt)

print(f"Where do you live {second_name}?")
lives = input(prompt)

print("What kind of computer do you have ?")
computer = input(prompt)

print(f"""
Alright , so you said you {likes} about liking me.
You live in {lives}. Not sure where it is.
And you have a {computer} computer. Nice
""")