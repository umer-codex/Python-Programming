
#To Create a List
empty_list = []
print("Empty List", empty_list)

#Final List
fruites_name = ["apple", "mango", "banana", "Water-Melon", "Melon", "Grapes"]
print(fruites_name)

#.append
fruites_name.append("cherry")
print(fruites_name)

#.insert
fruites_name.insert(1, "Pomigranite")
print(fruites_name)

#indexing
print(fruites_name[0])
print(fruites_name[-2])

#Update specific Element
idx = fruites_name.index("apple")
fruites_name[idx] = "blueberry"
print(fruites_name)

#Lenght & Type
print("Total Fruites", len(fruites_name))
print("Type of this Collection", type(fruites_name))

#Slicing
print(fruites_name[:3])
print(fruites_name[3:])
print(fruites_name[0:])
print(fruites_name[0:6])
print(fruites_name[:-1])

#For Remove and .pop fuctions

fruits_name_2 = ["Strawberry", "Pineapple", "kiwi", "Papaya"]
fruits_name_2.pop(0)
print(fruits_name_2)

fruits_name_2.remove("kiwi")
print(fruits_name_2)


#.sort
fruits = ["A", "D", "E", "B", "F", "C"]
fruits.sort()
print(fruits)

#reverse .sort
fruits_2 = ["G", "H", "I", "J", "K"]
fruits_2.sort(reverse=True)
print(fruits_2)

#.extend 
fruits_3 = ["U", "V", "W"]
fruits_3.extend(["X", "Y", "Z"])
print(fruits_3)

#reverse
fruits_4 = [1, 2, 3, 4, 5]
fruits_4.reverse()
print(fruits_4)

#.copy
fruits_5 = [4, 5, 6, 7, 8]
fruits_6 = fruits_5.copy() 
print(fruits_6)
print(fruits_5)

#.clear
fruits_7 = [11, 12, 13, 14, 15]
fruits_7.clear()
print(fruits_7)

# Membership Operators
fruits_8 = [10, 20, 30, 40, 50]
if 10 in fruits_8:
    print("Avialable")