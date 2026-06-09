
# Emputy Tuple
empty_tuple = ()
print(empty_tuple)

# Single Element Tuple - Must Use Comma at Last
single_element_tuple = ("Abeeha",)
print(single_element_tuple, type(single_element_tuple))

# Final Tuple with same data type
fruits = ("Apple", "Mango", "Banana", "cherry", "Wallnuts")
print("Same Daata-Type in same Tuple:", fruits)

#Tuple with Different Data Types
fruites_2 = ("Peach", 175.2, True)
print("Different Daata-Type in same Tuple:",fruites_2)

# Accessing Tuples / Positive Indexing
fruits = ("Apple", "Mango", "Banana", "Cherry", "Wallnuts")
print(fruits[0])        #out-put: 'Apple'
print(fruits[3])        #out-put: 'Cherry'

# Negative Indexing
print(fruits[-1])        #out-put: 'Wallnuts'
print(fruits[-3])        #out-put: 'Banana'

# Slicing
fruits = ("Apple", "Mango", "Banana", "cherry", "Wallnuts")
print(fruits[0:3])  #out-put: 'Apple', 'Mango', 'Banana'
print(fruits[0:])   #out-put: 'Apple', 'Mango', 'Banana', 'cherry', 'Wallnuts'
print(fruits[:4])   #out-put: left to right humaray pass total_04 Elements majood hai
  # to yeah 0 se start kr k 04 se pehlay pehlay tak print kr dy gi

# Tuple Packing - When we simply assign Tuple values with a variable with it's name so, it's called a 'Tuple Packing'.
students = ("00", "10", "20", "30", "40", "50") #hence: tuple is packed
print(students) #out-put: '00', '10', '20', '30', '40', '50'

#Tuple Un-Packing - When we simply assign Tuple values with those families or conditions so , it's called 'Tuple Un-Packing'.
students = ("00", "10", "20", "30", "40", "50") 
A, B, C, D, E, F = students
print(A)
print(B)
print(C)
print(D)
print(E)
print(F)

#Using *(Advanced Un-Packing):-(*b remaining values collect karta hai.)
countries = ("UK", "Japan", "New York", "Malaysia", "Berlin", "Luxembourg")
a, *b, c = countries
print(a)
print(b)
print(c)

# Tuples Method

# 1- .count
accounts = ("HBL", "Meezan", "UBL", "Habib", "Muslim", "UBL", "MCB")
print(accounts.count("UBL"))
print(accounts.count("MCB"))

# 2- index()
accounts = ("HBL", "Meezan", "UBL", "Habib", "Muslim", "UBL", "MCB")
print(accounts.index("Meezan"))
print(accounts.index("MCB"))

# Length len()
accounts = ("HBL", "Meezan", "UBL", "Habib", "Muslim", "UBL", "MCB")
print("Accounts Lenght:", len(accounts))

# Nested Tuple
classmates_with_ages = (
    ("Khizer", 21),
    ("Mugees", 24),
    ("Hussnain", 23)
)
print(classmates_with_ages[1])
print(classmates_with_ages[1][0])

#Convert Tuple into List
students_2 = ("Ali", "Bilal", "Usman")

students_list = list(students_2)

print(type(students_list)) #output: <class 'list'>

#Convert List into Tuple
student_3 = ["Aani", "Nimra", "Sahar", "Abeeha"]
student_tuple = tuple(student_3)
print(type(student_tuple))