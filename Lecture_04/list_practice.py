students = []
students.extend(["Ali", "Bilal", "Dawood", "Eman", "Faizan", "Abeeha", "Nabeela"])
print(students)

students.append("Usman")
print(students)

students.insert(4, "Gasheem")
print(students)

print(students[1])

print(students[-3])

print(students[-1])

idx = students.index("Gasheem")
students[idx] = "Farzana"
print(students)

print("Students Lenght:", len(students))
print("Students Type:", type(students))

print(students[0:3])
print(students[-4:])

students.remove("Abeeha")
print(students)

students.pop(3)
print(students)

students.sort()
print(students)

students.sort(reverse=True)
print(students)

students.reverse()
print(students)

students_2 = students.copy()
print(students_2)

if "Abeeha" in students:
    print("Find")

students.clear()
print(students)