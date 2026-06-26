
# 1. Basic Loop Iteration:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# 2. Repeating Code a Specific Number of Times (range())
#    To repeat an action a set number of times (we set 5 times in below example), use Python's built-in range(stop) function.
#    It starts at 0 by default and stops right before the specified number.

for i in range(5):
    print("hello")      # output: It repeats hello 5 times [hello, hello, hello, hello, hello]

# 3. 
# Sequence Type:
# Loop can be run on any sequence
# [List, Range, Strings, Tuple, Dictionaries]

# 4. Basic Loop using List:
animals = ["Lion", "Elephent", "Crocodile"]
for species in animals:
    print(species)

# 5. Range, Types of Range starting from Line # 75 below:
for i in range(5):
    print(i)            # output: 0, 1, 2, 3, 4 [naturally start from '0' and end befor stop point, in this code (5) was stopping point]

# In Range you can choose specific starting point: 
# Like here:
j = (10)
for i in range(3, 9):   # # output: 3, 4, 5, 6, 7, 8 [This is your own choice]
    print(i)
# In Range you can choose specific starting, stopig points with skipping Iterations(called steps) Like: (start, stop, step)


# 6. Looping Through a String:
#    Strings are sequences of individual characters, so you can loop through them letter by letter.
name = "Ali"
for letter in name:
    print(letter)       # output: It prints the string letters and print separately (A, l, i)

# 7. Loop through Tuples:
colors = ("yellow", "red", "green" )
for color in colors:
    print(color)

mixed_tup = (219, 5.9, "house", "True" )
for tup in mixed_tup:
    print(tup)

# 8. Loops through Dictionaries:

# For keys:
    
person = {
    "name" : "Zing",
    "age" : 20,
    "city" : "Japan"
}
for key in person:
    print(key)      # output: It print just Keys (name, age, city)

# For Values:

for values in person.values():
    print(values)      # output: It print just Values (Zing, 20, Japan)

# For Key & Values

for key ,value in person.items():
    print(key, value)      # output: It print Both Keys & Values: (name Zing, age 20, city Japan)

# 5.1 Types of Range:
# Start and Stop: stop never include 
for num in range(2, 6):         # Output: 2, 3, 4, 5
    print(num)

# Start, Stop and Step: How much jumps for backward:
for num in range(0, 10, 2):
    print(num)                     # Output: 0, 2, 4, 6, 8. ['10' print nahi hoga q k wo list k ander aik stop element hai or range() stop ko print nahi krti]

#Reverse Counting: Just use negative step element in range(10, 0, -2):
for num in range(10, 0, -2):
    print(num)                     # Output: 10, 8, 6, 4, 2. ['0' will not be printed because its a stop element at last in List]

for num in range(10, 0, -1):
    print(num)                     # output: 10, 9, 8, 7, 6, 5, 4, 3, 2, 1 ['0' will not be printed its its a stoping point in leat at last]

# Negative step.

# Convert range() into List:
range(0, 5)
numbers = list(range(0, 5))
print(numbers, type(numbers))      # output: [0, 1, 2, 3, 4] <class 'list'>

# Create any Table by using range(): Here we will print Table of 5:
for numbers in range(1, 11):
    print(5 * numbers)             # output: 5, 10, 15, 20, 25, 30, 35, 40, 45, 50

for numbers in range(1, 21):
    print(8 * numbers)

print("Types of numbers",type(numbers))

# Lenght in Range:
m = range(1, 10)
print(len(m))

# range(5)
#      ↑
#     stop

# 0 1 2 3 4
#        ↑
#     last value

# range(2, 8)

# 2 3 4 5 6 7
#           ↑
#      stop se pehle

# range(5)         # 0,1,2,3,4

# range(1,5)       # 1,2,3,4

# range(1,10,3)    # 1,4,7

# range(10,0,-2)   # 10,8,6,4,2

# break in For Loop:
students = ("Abeeha", "Sahar", "Sara", "Ali")
for student in students:
    if student == "Sara":
        print("Sarah is here")
        break

# continue in For Loop:
fruites = ["appke", "cherry", "grapes", "mango", "banana", "melon"]
for fruit in fruites:
    if fruit == "mango":
        continue
    print(fruit)

# Neted For Loop:
# A nested for loop is a loop iside another loop:
# Syntax:

for i in range(3):
    for j in range(2):
        print(i, j)

# output:
# i = 0 : j = 0, 1
# 00
# 01
# i = 1 : j = 0, 1
# 10
# 11
# i = 2 : j = 0, 1
# 20
# 21



for i in range(3):
    for j in range(2):
        print(i * j)

# output:
# i = 0 : j = 0, 1
# 0
# 0
# i = 1 : j = 0, 1
# 0
# 1
# i = 2 : j = 0, 1
# 0
# 2

for a in range(3):
    for b in range(5, 10):
        print(a, b)

index = 0
for i in range(1, 11):
    print(index, 6 * i)
    index += 1

index = 0
for i in range(1, 11):
    print(f"Index: {index} -> 6 * {i} = {6 * i}")
    index += 1  # اب یہ لوپ کے اندر ہے، ہر چکر میں بڑھے گا

index = 1
for x in range(1, 11):
    print(f"Index: {index} > 7 * {x} = {7 * x}")
    index += 1

for index, y in enumerate(range(1, 11), start=1):
    print(f"Index: {index} > 9 * {y} = {9 * y}")
else:
    print("Table of 9 is Cmpleted")