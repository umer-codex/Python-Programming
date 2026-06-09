# #1 Comman Mistake
empty_dictionary = {} #yeah sik dictionary hai set nai.
print(set)

# #1 sahi set
empty_set = set() # yeah empty set hai.
print(type(empty_set))

# #2 Final set:
student = {"Umer", "Hamza"}

# #3 .add
student = {"Umer", "Hamza"}
student.add("Ali")
print(student)

# #4 .update
student = {"Umer", "Hamza"}
student.update(["Tanzeela", "Abbeeha"])

# #5 .remove
student.add("Ali")              # Pehle Ali ko add kiya
student.remove("Ali")           # ouytput: 'key Error' : if value is not exist

# #6 .discard
student = {"Umer", "Hamza"}
student.discard("Khizer")       # yeah agr value na b ho to error nahi dayga. safer mode hai.

# #7 .pop
student = {"Umer", "Hamza"}
student.pop()                   # random element remove krta hai 

# #8 .clear()
student.clear()

# #9 lenght:
owl = {1, 2, 3, 4, 5}
print(len(owl))

# #10 Member-ship
students = {"Ali", "Bilal", "Umer"}

if "Ali" in students:
    print("Found")

# #11 Loop through set.
students = {"Ali", "Bilal", "Umer"}

for student in students:
    print(student)      # Order guaranteed nahi hota.



# #12   Stop Indexing - Can't support Indexing:
# students =  {"Ali", "Bilal", "Umer"}
# print(students[0])  #Error: TypreError



# #13 Duplicate Values automatically remove
number = {1, 2, 3, 1, 3, 5, 6, 7, 5}
print(number)   #   output: {1, 2, 3, 5 , 6, 7}

# #14   Convert list into sets:
numbers = [1, 2, 3, 1, 3, 5, 6, 7, 5]
number_set = set(numbers)
print(number_set)                                       # number pehley list tha ab usko set mein convert kr diya hai.

# #15   Union .union most Importan, Print all values
python_students = {"Umer", "Bilal", "Khizer"}
ai_learner = {"Mugees", "Bilal", "Umer"}

print(python_students | ai_learner)                     #method # 01
print(python_students.union(ai_learner))                #method # 02           # Its gives us combination od all values as an output {'Umer', 'Mugees', 'Bilal', 'Khizer'}

# #16 Intersection .intersection    Print common values
python_student = {"Huzaifa", "Kareem", "Raheem"}
ai_learners = {"Mugees", "Raheem", "Huzaifa"}

print(python_student.intersection(ai_learners))         # method # 01          # Its gives us comman values as an output Like: {'Huzaifa', 'Raheem'}
print(python_student & ai_learners)                     # method # 02

# #17 Difference .defference        Print only 1st-set's not comman values as an output
python_student = {"Huzaifa", "Kareem", "Raheem"}
ai_learners = {"Mugees", "Raheem", "Huzaifa"}

print(python_student.difference(ai_learners))           # method # 01
print(python_student - ai_learners)                     # method # 02           # Output : Kareem

# #18 Symmetric Difference .symetric_difference
python_student = {"Huzaifa", "Kareem", "Raheem"}
ai_learners = {"Mugees", "Raheem", "Huzaifa"}

print(python_student.symmetric_difference(ai_learners)) # method # 01
print(python_student ^ ai_learners)                     # method # 01           # Output : {'Kareem', 'Mugees'}



# For Union                             = .union(), |                   # print all values
# For Intersection                      = .intersection(), &            # pint common values
# For Difference                        = .difference(), -              # print sets one's values that is not in set 2
# For Symmetric Difference               = .symetric_difference, ^       # print all un-common values from both sets  



# #19 Copying Set   .copy()
set_1 = {"Lahore", "Narowal", "Sialkot"}
set_2  = set_1.copy()
print(set_2)                                             # Output : set_2 = {'Lahore', 'Narowal', 'Sialkot'}

# #20 Allowed Users 
allowed = {
    "Umer",
    "Bilal",
    "Khizer"    
}

if "Khizer" in allowed:
    print("Login Allowed")

# ✅ create set
# ✅ add()
# ✅ update()
# ✅ remove()
# ✅ discard()
# ✅ pop()
# ✅ clear()
# ✅ len()
# ✅ in
# ✅ loop
# ✅ list ↔ set conversion
# ✅ union
# ✅ intersection
# ✅ difference
# ✅ symmetric_difference

# Backend aur AI projects mein sets mostly:

# duplicate removal
# membership checking
# common items finding

# ke liye use hote hain.