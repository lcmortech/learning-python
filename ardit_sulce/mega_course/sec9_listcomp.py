# Intro to List Comprehensions
# A list comprehension is an expression that creates a list by iterating over another container.

temps = [221, 234, 340, 230]

# Not using decimals/floats saves space on servers

new_temps = []
for temp in temps:
    new_temps.append(temp / 10)

print(new_temps)

# A neater way to do this: list comprehension
new_temps = [temp / 10 for temp in temps]

print(new_temps)

# List Comp with Conditionals
temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 for temp iin temps if temp != -9999]

print(new_temps)

# Ex - Only Numbers
def foo(lst):
    return [i for i in lst if  isinstance(i, int)]

# Ex - Only Positive Numbers
def foo(lst):
    return [i for i in lst if i > 0 ]


# List Comp with If-Else
temps = [221, 234, 340, -9999, 230]

new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]

print[new_temps]

# Ex - Zeroes Instead
def foo(lst):
    return [i if not isinstance(i, str) else 0 for i in lst ]

# Ex - Convert and Sum Up
def foo(list):
    return sum([float(i) for i in list])

# break - family emergency 2