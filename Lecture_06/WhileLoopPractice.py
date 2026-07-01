# 1.
count = 1
while count < 11:
    print(count)
    count += 1

count = 10
while count > 0:
    print(count)
    count -= 1
# 2.
count = 1
while count < 21:
    if count % 2 != 0:
        count += 1
        continue
    print(count)
    count += 1
# 3. 
count = 1
while count < 21:
    if count % 2 == 0:
        count += 1
        continue
    print(count)
    count += 1
# 4. 
i = 1
while i <= 10:
    print(i * 5)
    i += 1
# 5.
number = 1
while number < 31:
    if number % 3 == 0:
        print("Fizz")
        number +=1
        continue
    print(number)
    number += 1
# 6. 
numbers = 1
while numbers <= 50:
    if numbers % 5 == 0:
        print("Nice")
    else:
        print(numbers)
    numbers += 1
# 6.2
number = 1
while number < 21:
    if number % 3 == 0:
        print("Fizz")
    else:
        print(number)
    
    number += 1

# 7.
number = 1
while number <= 30:
    if number % 2 == 0:
        print("even")
    else:
        print("odd")
    number += 1

#  8.
number = 1
while number <= 20:
    if number == 7:
       number += 1
       continue
    else:
        print(number)
    number += 1

# 9.
number = 1
while number <= 20:
    if number == 12:
        break
    print(number)
    number += 1

# 10.
number = int(input("Enter number:"))
i = 1
index = 1
while i <= 10:
    print(f"{number} * {index}: {number * i}")
    i += 1
    index += 1

#  11. Yeah mene chrome se dykha tha mujhay nahi ata tha
while True:
    password = input("Enter the password")
    if password == "python":
        print("Access Granted")
        break

# # 12.  Yeah humnay nahi read kia hua nahi ata internet se dykha hai:
while True:
    try:
        user_input = float(input("Enter a positive number: "))
        if user_input > 0:
            print(f"Thank you! You entered: {user_input}")
            break
        else:
            print("That is not a positive number. Try again.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# 13. ni prhaya hua
# 14. ni prhaya hua

# 15.
number = 1
if number % 3 == 0 and number % 5 == 0:
    print("FizzBuzz")
elif number % 3 == 0:
    print("Fizz")
elif number % 5 == 0:
    print("Buzz")
else:
    print(number)
number += 1

# 16.
number = 1
total = 0
while number <= 100:
    total += number
    number += 1
print(total)


# 20. Net se dykha parha hua nahi tha
# Start checking numbers from 2, as 1 is not a prime number
number = 2

while number <= 100:
    is_prime = True
    divisor = 2
    
    # Check for factors from 2 up to the square root of the number
    while divisor * divisor <= number:
        if number % divisor == 0:
            is_prime = False  # Found a factor, so it's not prime
            break             # Exit the inner loop immediately
        divisor += 1
        
    # If no factors were found, the number is prime
    if is_prime:
        print(number, end=" ")
        
    number += 1
