# Print numbers from 1 to 10:
for i in range(1, 11):
    print("1 to 10")
    print(i)

# Print numbers from 10 to 1 backward:
for i in range(10, 0, -1):
    print("10 to 1 backward")
    print(i)

# Print only even numbers from 1 to 20:
for i in range(2, 21, 2):
    print(i)

# Print only odd numbers from 1 to 20:
for i in range(1, 21, 2):
    print(i)

# Pirnt addition of 1 to 10:
total = 0
for num in range(1, 11):
    total = total + num
    print(total)

# Pattern name: Sequential Loops
for i in range(1, 4):
    print(i)
for i in range(4, 7):
    print(i)

for i in range(1, 4):
    print(i)
    print(i + 1)  

# Accumulation Pattern:
total = 0
for i in range(1, 5):
    total = total + i
print(total)

#Decrementation Pattern:
total = 10
for i in range(1, 4):
    total = total - i
    print(total)

# Print the cube of each number from range(1, 6):
for m in range(1, 6):
    cube = m ** 3
    print(f"The cube of {m} is {cube}") # I just learn it didn't know before: How it work: m = 1 cube = 1*1 = 1*1 = 1, same till end 5*5 = 25*5 = 125

names = ["Ali", "Sara", "Ahmed"]

for index, name in enumerate(names, start = 1):
    print(f"Index: {index}, {name}")
    for i in name:
        print(i)

# Divisible numbers nahi aata
for a in range(1, 11):
    if a % 3 == 0:  # % = remainder, agar 0 hai to divisible hai
       print(a)
# Output: 3, 6, 9

# Accumulation on a LIST:
numbers = [5, 10, 15, 20, 25]
total_sum = 0
for num in numbers:
    total_sum = total_sum + num
print(total_sum)

for i in range(1, 4):
    for j in range(1, 3):
        print(i * j)


for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print("Boom")
    elif i % 3 == 0:
        print("Tik")
        continue
    elif i % 5 == 0:
        print("Tok")
        continue

for i in range(30, 0, -1):
    if i % 2 == 0:
        print("success")
    else:
        print(i * 2)

m = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23]
total = 0

for i in range(1, 21):
    if i % 4 == 0:
        total = total + i
        print(i)
print(total)

data = {
    "a" : 1,
    "b" : 2,
    "a" : 3,
}
print(data)

# Continue in Nested For Loop:
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)

# Print any Table:
n = int(input("enter the number:"))
for i in range(1, 11):
    print(n * i)