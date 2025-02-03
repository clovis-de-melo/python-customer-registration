print("Welcome to Python!")

# this is a comment 

name = "Placeholder"
print(name)

name = input("What is your name? ")
print("Welcome to Python, " + name)

# "a" means to "add"

# "f" means f string which is used to concatenate

# "\n" is used to break the line 

with open("data_base.csv", "a") as databasefile:
    databasefile.write(f"Welcome to Python {name}.\n")
    
age = int(input("How old are you? "))

if age > 21:
    print("You can join the party!")
else:
    print("You can not join the party!")

