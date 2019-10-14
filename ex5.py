my_name = "Prajwal"
my_age = 21 # not a lie
my_height = 6 # feet
my_weight = 61 # in kgs
my_eyes = 'Black'
my_teeth = 'white'
my_hair = 'Brown'

print(f"Lets talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} kgs heavy.")
print(f"Actually that's not too heavy.")

#this line is tricky , try get it exactly right
total = my_age + my_height + my_weight
print(f"If I add {my_age},{my_height} and {my_weight} I get {total}")

#convert inches to centimeter
height_inches = 10
height_cm = 2.54 * height_inches
print(f"Height in centimeters{height_cm}.")

#convert pounds to kilogram
weight_pound = 10
weight_kg = weight_pound * 0.453
print(f"Weight in kilogram{weight_kg}.")
