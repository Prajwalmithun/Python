# Exercise 17: More Files
# Copying of one file to another


from sys import argv
#to check if the file is present or not
from os.path import exists

script , from_file , to_file = argv

print(f"Copying from {from_file} to {to_file}")

# We could do this is both on on line how?
in_file = open(from_file)
indata = in_file.read()

#print(f"The input file is {len(indata)} bytes long")

#print(f"Does the output file exist? {exists(to_file)}")
#print("Ready, hit return to continue,CTRL-C to abort")
#input()

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done")

out_file.close()
in_file.close()
