# ML ke Liye Important

# 1. Basic syntax           ✅
# 2. Condition check        ✅
# 3. Counter variable       ✅
# 4. Break                  ✅
# 5. Continue               ✅
# 6. While vs For           ✅


# 1. Basic Syntax:- While loop ka structure — while keyword, condition, colon, aur indented code block.

count = 0
while count < 5:
    print(count)
    count += 1

# Output:
# 0 = count < 5: True = print 0, count += 1 = now count becomes 1.
# 1 = count < 5: True = print 1, count += 1 = now count becomes 2.
# 2 = count < 5: True = print 2, count += 1 = now count becomes 3.
# 3 = count < 5: True = print 3, count += 1 = now count becomes 4.
# 4 = count < 5: True = print 4, count += 1 = now count becomes 5.
# 5 = count < 5: False = never be print, Loop Finished.

# 2. Condition Check:- Har iteration se pehle condition evaluate hoti hai — True hai to loop chalta hai, False hote hi band ho jaata hai.
number = 20
while number > 0:
    print(number)
    number -= 2
# Output:
# 20 = number > 0: True = print 20, number -= 2 = now = number decreases and newly becomes 18.
# 18 = number > 0: True = print 18, number -= 2 = now = number decreases and newly becomes 16.
# 16 = number > 0: True = print 16, number -= 2 = now = number decreases and newly becomes 14.
# 14 = number > 0: True = print 14, number -= 2 = now = number decreases and newly becomes 12.
# 12 = number > 0: True = print 12, number -= 2 = now = number decreases and newly becomes 10.
# 10 = number > 0: True = print 10, number -= 2 = now = number decreases and newly becomes 08.
# 08 = number > 0: True = print 08, number -= 2 = now = number decreases and newly becomes 06.
# 06 = number > 0: True = print 06, number -= 2 = now = number decreases and newly becomes 04.
# 04 = number > 0: True = print 04, number -= 2 = now = number decreases and newly becomes 02.
# 02 = number > 0: True = print 02, number -= 2 = now = number decreases and newly becomes 00.
# At least now:
# 00 = number > 0: False = never be printed, Here is while loop Stops automatically.

# 3. Counter Variable: Definition: Loop ko control karne ke liye ek variable jo har iteration mein update hota hai — warna loop kabhi band nahi hoga.

counter = 0                     # initialize: Set Starting Value
while counter < 5:              # condition:  How long it runs
    print(counter)
    counter += 1                # update — Imoportant : Change after every Iteration

# What if counter variale is missing: Loop Becomes infinite Lets check it!
# 👇👇👇👇👇
# counters = 0
# while counters < 10:
#     print(counters)
# ☝️☝️☝️☝️☝️
# 4. Break in while Loop: Definition: Condition false hone ka wait kiye bina loop ko forcefully band karo.
counter = 0
while counter < 10:
    if counter == 5:
        break
    print(counter)
    counter += 1

counter = 0
while counter < 10:
    if counter == 6:
        counter += 1        # If you skip this step while using continue your program will hang and stuck on "if counter == 6 > True", So, you need to add counter before continue.
        continue
    print(counter)
    counter += 1

# "Continue in For Loop:"

counter = 0
for counter in range(11):
    if counter == 6:
       continue
    print(counter)
    counter += 1

# Continue in Nested For Loop:
for i in range(3):
    for j in range(3):
        if j == 1:
            continue
        print(i, j)
# Output: 
# 0 0
# 0 1 --- not print skip by continue
# 0 2
# 1 0
# 1 1 --- not print skip by continue
# 1 2
# 2 0
# 2 1 --- not print skip by continue
# 2 2

# Finally Output of continue i nested loop is:
# 0 0
# 0 2
# 1 0
# 1 2
# 2 0
# 2 2

