# # Print numbers from 1 to 10:
# for i in range(1, 11):
#     print("1 to 10")
#     print(i)

# # Print numbers from 10 to 1 backward:
# for i in range(10, 0, -1):
#     print("10 to 1 backward")
#     print(i)

# # Print only even numbers from 1 to 20:
# for i in range(2, 21, 2):
#     print(i)

# # Print only odd numbers from 1 to 20:
# for i in range(1, 21, 2):
#     print(i)

# # Pirnt addition of 1 to 10:
# total = 0
# for num in range(1, 11):
#     total = total + num
#     print(total)

# # Pattern name: Sequential Loops
# for i in range(1, 4):
#     print(i)
# for i in range(4, 7):
#     print(i)

# for i in range(1, 4):
#     print(i)
#     print(i + 1)  

# # Accumulation Pattern:
# total = 0
# for i in range(1, 5):
#     total = total + i
# print(total)

# #Decrementation Pattern:
# total = 10
# for i in range(1, 4):
#     total = total - i
#     print(total)

# # Print the cube of each number from range(1, 6):
# for m in range(1, 6):
#     cube = m ** 3
#     print(f"The cube of {m} is {cube}") # I just learn it didn't know before: How it work: m = 1 cube = 1*1 = 1*1 = 1, same till end 5*5 = 25*5 = 125

# names = ["Ali", "Sara", "Ahmed"]

# for index, name in enumerate(names, start = 1):
#     print(f"Index: {index}, {name}")
#     for i in name:
#         print(i)

# # Divisible numbers nahi aata
# for a in range(1, 11):
#     if a % 3 == 0:  # % = remainder, agar 0 hai to divisible hai
#        print(a)
# # Output: 3, 6, 9

# # Accumulation on a LIST:
# numbers = [5, 10, 15, 20, 25]
# total_sum = 0
# for num in numbers:
#     total_sum = total_sum + num
# print(total_sum)

# for i in range(1, 4):
#     for j in range(1, 3):
#         print(i * j)