student = []
students = [
    ("Ali", 21, "Python"),
    ("Bilal", 22, "AI"),
    ("Usman", 20, "FastAPI"),
    ("Umer", 21, "Backend")
]
print(students, type(students))

for only_students in students:
    print(only_students[0])

for only_courses in students: # yeah students variables mein se saray 2nd walay index ko print kr dayga.
    print(only_courses[2])

students.append(("Abeeha", 20, "Data Science"))
print(students)

idx = students.index(("Usman", 20, "FastAPI"))
students[idx] = ("Usman", 20, "DevOps")
print(students)
                      
students.pop(1)
print(students)