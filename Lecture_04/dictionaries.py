#Empty Dictionary
students_0 = {}
print(students_0)
print(type(students_0))

# #3 dict()constructur - alternative way to create dictionary
student_1 = dict(name="Umer", age=21, course="Python")
print(student_1)        #output = {'name':'Umer', 'age':21, 'course':'Python'}

# #4    Accessing Values
students = {
    "name": "Umer",
    "age": 21
}
print(students["name"])   #output : Umer
print(students["age"])    #21

# #5    .get method_safer method
students = {
    "name": "Umer",
    "age": 21
}
print(students.get("name"))

# Difference:-

#  print(student["city"])       agr kisi dictionary mein wo key : value nahi jo hum mang rahay hain to print(student["city"]) error dygi 
# Error:- KeyError

# But:

# print(student.get("city"))    agr kisi dictionary mein wo key : value nahi jo hum mang rahay hain to print(student.get("city")) none bta dygi
# Output:- None

# #6 Adding New Data - Same as (.append) in Lists, But the difference is [students["course"] = "Python"].
students = {
    "name": "Umer",
    "age": 21
}
students["course"] = "Python"   # same in lists = students.append("Python")
print("6", students)

#output
# {
#  'name':'Umer',
#  'age':21,
#  'course':'Python'
# }

# #7 Updating existing and specific Values - Like .indexing in lists but in different way
students["age"] = 22
print(students)

# #8 .pop() - same as it is in lists
students.pop("age")
print(students)

# #8.1 del - list mein majood jo .remove hai yeah(del) usko kisi trhan replace krta hai
del students["name"]
print(students)

# #8.2 .clear()
students.clear()
print(students)

# #9 lenght same as it is in list and tuple
student = {
    "name": "Umer",
    "age": 21,
    "course": "Python"
}
print(len(student))

# #10 .key - Print all the key names in dictionaries
student = {
    "name": "Umer",
    "age": 21,
    "course": "Python"
}
print(student.keys()) # Output:    dict_keys(['name', 'age'])

# # .values - print all values
student = {
    "name": "Umer",
    "age": 21,
    "course": "Python"
}
print(student.values()) # Output:    dict_values(['Umer', 21, 'Python'])

# #12 .items
student = {
    "name": "Umer",
    "age": 21,
    "course": "Python"
}
print(student.items())  

# # Output:   

# dict_items([
#  ('name','Umer'),
#  ('age',21),
#  ('course', 'Python')
# ])

# #13 for loop in dictionaries
student = {
    "name": "Umer",
    "age": 21,
    "course": "Python"
}

for key in student:
    print(key)  # output name, age, course

# #14 to print specific elements
for value in student.values():
    print(value)    # output: Umer, 21, Pyhton

# #15 to print items = Keys + Values 
for key, value in student.items():
    print(key, value)

# output:
# name Umer
# age 21
# course Python

# #16 .copy() same as it is in list and tuples
student_2 = student.copy()
print("16", student_2)

# #17 Nested Dictionary
nested_dictionary = {

        "fruits" : {                            # sub-dictionary 01
            "name": "Apple",
            "color": "Red",
            "identification": "Black Oxford"
        },

        "bird": {                               # sub-dictionary 02
            "name": "Lovebird",
            "identification": "Green Fisher Small Beak",
            "species": "Agapornies Denmark"
        }
}

print(nested_dictionary, (type(nested_dictionary)))
print(nested_dictionary["fruits"])
print(nested_dictionary["bird"])
print(nested_dictionary["fruits"]["name"])
print(nested_dictionary["fruits"]["color"])
print(nested_dictionary["fruits"]["identification"])
print(nested_dictionary["bird"]["name"])
print(nested_dictionary["bird"]["identification"])
print(nested_dictionary["bird"]["species"])

# #18 Dictionaries inside Lists
banks = [
    {
        "name": "MCB",
        "location": "Lahore",
    },
    
    {
        "names": "JBL" +" "+ "UBL",         #with adding space
        "location": "KPK"
    }
]

print(banks[0]["location"])
print(banks[0]["name"])
print(banks[1]["location"])
print(banks[1]["names"])

# #19 Membership check
books = {
    "islamic": "Islamiyat",
    "historical": "SST",
    "math": "Geography"
}
if "math" in books:
    print("Avialable")

for isl in books:
    print("Checking:", isl)
    if isl == "islamic":
        print("Yes!")
        break

# #20 Dictionay Inside List:

degrees = [
    {
        "catagories" : ["Tech Industrial Degrees", "Medical Degrees", "Engineering Dgrees"],
        "catagory" : "Tech Industrial Degrees",
        "first" : "BBIT",
        "second" : "BSIT",
        "third" : "BSCS"
    },
    
    {
        "catagory" : "Medical Degrees",
        "first" : "BS Zoology",
        "second" : "BS Cardiology",
        "third" : "BS Bootny",
        "skill" : "Python"
    },
    
    {
        "catagory" : "Engineering Degrees",
        "first" : "Engineering Science",
        "second" : "Chemical Engineering",
        "third" : "Mechanical Engineering"
    }
]

print(degrees, type(degrees), len(degrees))
print(degrees[0])
print(degrees[0]["catagory"])
print(degrees[0]["first"])
print(degrees[0]["second"])
print(degrees[0]["third"])

print(degrees[1])
print(degrees[1]["catagory"])
print(degrees[1]["first"])
print(degrees[1]["second"])
print(degrees[1]["third"])

print(degrees[2])
print(degrees[2]["catagory"])
print(degrees[2]["first"])
print(degrees[2]["second"])
print(degrees[2]["third"])

if "first" in degrees[0]:
    print("Mill Gaya")

for skills in degrees[1]:
    print("Checking:", skills)
    if skills == "skill":
        print("Han Han Yahin Hai!")
        break

# #21 .update 
animals = {
    "green" : "parrot",
    "white" : "albino"
}

animals.update({
    "yellow" : "lutino"
})
print(animals)
print(animals["yellow"])

for key in animals:
    print(key)
for value in animals.values():
    print(value)
for key, value in animals.items():
    print(key, value)

for animal in animals:
    print("Checking:", animal)
    if animal == "yellow":
        print("majood")

for yellow in animals:
    print("gg")
    break
