item = "Banana"
item = "Apple"
item = "Orange"

print(item)

print("Hello " + item)

# DATATYPES
integer = 2021
word = "text"
isHappy = False
mario_list = ["Luigi", "Mario", "Toad"]

print(integer)
print(word)
print(isHappy)
print(mario_list)

# CONVERSION CONCAT
integer = 2021
name = "Mario"
str_num = "22"

print(name + str(integer))
print(integer + int(str_num))

# BOOLS
age = 28
isHappy = False

if age > 21:
    print("You are old!")
elif age == 18:
    "You are getting old!"
else:
    "You are still young!"

if isHappy:
    "You are happy!"
elif not isHappy:
    "You are not happy"
else:
    "You are okay"

# LOOPS

# FOR LOOP
for i in range(3):
    print("Hello", i + 1)

name_list = ["Luigi", "Mario", "Toad"]

for name in name_list:
    print(name)

# WHILE LOOP ( always executes at least once)
i = 0

while i < 5:
    #i = i + 1 # excludes 0 and makes 5 inclusive
    print(i)
    i += 1
    

while True:
    user_input = input("Enter something: ")
    if user_input == '0':
        print("We are done here")
        break

# FUNCTIONS

def say_hello(name):
    print("Hello " + name)

say_hello("Myla")

def get_internet():
    pass

def run_game():
    pass

# TRY/EXCEPT (similar to if/else but for catching errors)

num = input("Please provide a number: ")

try:
    print(10 + int(num))
except: # won't throw an exception error
    print("This is not a valid number")
