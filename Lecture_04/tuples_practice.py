#Task #1    Basic Tuple Creation
cities = ("Karachi", "Lahore", "Islamabad", "Quetta", "Peshawar")
print(cities)
print(cities[0])
print(cities[-1])
print(cities[4])

#Task #2     Positive & Negative Indexing
numbers = (10, 20, 30, 40, 50, 60)
print(numbers[1]) #output: 20
print(numbers[5]) #output: 60
print(numbers[-1]) #output: 60
print(numbers[-4]) #output: 30

#Task #3     Slicing Practice
fruits = ("Apple", "Mango", "Banana", "Orange", "Cherry", "Peach")
print(fruits[:3])
print(fruits[4:])
print(fruits[1:])

#Task #4      Tuple Packing & Un-packing
student = ("Umer", 21, "Python") #: Tuple Packing
name, age, course = student      #: Un-Packing
print(name)
print(age)
print(course)

#Task #5       Advanced Un-packing
data = (1, 2, 3, 4, 5, 6, 7, 8)
a, *b, c = data
print(a)        #output: This prints first index from tuple = 1 
print(b)        #output: It will cover other inner indexes from the no 1 to no 8 = 2, 3, 4, 5, 6, 7
print(c)        #output: This prints last index from tuple = 8

#Task #6        .count() method
colors = ("Red", "Blue", "Red", "Green", "Red", "Black")
print(colors.count("Red"))  #output: 3
print(colors.count("Blue")) #output: 1

#Task #7        .index() method
colors = ("Red", "Blue", "Red", "Green", "Red", "Black")
print(colors.index("Red"))  #output: 0
print(colors.index("Blue")) #output: 1

#Task #8        Nested Tuple
students = (
    ("Ali", 21),
    ("Bilal", 22),
    ("Usman", 20)
)
print(students[1])
print(students[2][1])
print(students[2][0])

#Task #9        Convert Tuple to List
languages = ("Python", "Java", "C++")
languages_list = list(languages)
languages_list.append("Javascript")
print(type(languages_list))

#Task #10       Convert List to Tuple
marks = [80, 90, 70, 85]
marks_tuple = tuple(marks)
print(type(marks_tuple))

#Task #11       Mini-Real World Chanllange
person = ("Umer", "umerm5245@gmail.com", "Pakistan", 21)
username, email, country, age = person
print(username)
print(email)
print(country)
print(age)

#Task #12 = sorry_loops_not_learned / I'm trying to learn & applying what I search just now
courses = ("Python", "AI", "FastAPI", "Docker")
for course in courses:
       print(course)

#Final Challenge(Important)
nested_tuple_5students = (
    ("Ali", 21),
    ("Umer", 22),
    ("Bilal", 23),
    ("Khizer", 24),
    ("Mugees", 25)
)
# #print all students names using Loop
print("All Student Names:")
for student in nested_tuple_5students:
        print(student[0])

# #print all students names Manually
# print("All Student Names:", 
#       nested_tuple_5students[0][0], 
#       nested_tuple_5students[1][0],
#       nested_tuple_5students[2][0],
#       nested_tuple_5students[3][0], 
#       nested_tuple_5students[4][0]
# ) 

# #print all students ages using Loop
print("All Students Ages:")
for student in nested_tuple_5students:
        print(student[1])


# #print all students ages Manually
# print("All Students Ages:", 
#       nested_tuple_5students[0][1],
#       nested_tuple_5students[1][1],
#       nested_tuple_5students[2][1],
#       nested_tuple_5students[3][1],
#       nested_tuple_5students[4][1]
# )

# Breaking Loop
invalid_numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)
for numbers in invalid_numbers:
        print("Checking:", numbers)
        if numbers == 18:
            print("Avialable in Numbers")
            break # Agr break nahi likha to yeah function kaam nahi kreyga