"""
#variables and formatting strings

facts = input("name: ")

print (f"hello, {facts}")

#conditions
n = int(input("number: "))
if n > 0:
    print("n is positive.")

elif n < 0:
    print("n is negative.")
else:
    print("n is not positive.")
#sequences
name = "Hamza"

print(name[1])


#ff. tuples use paranthesis() no square brackets needed.

coordinatex = 10.0
coordinatey = 20.0

coordinate = (10.0, 20.0)

#list

names = ["hamza", "hafsa", "Ammarah", "areesha"]

names.append("Mama")
names.sort()
print(names)

s = set()

s.add(1)
s.add(2)
s.add(3)
s.add(4)

print(f"this has {len(s)} elements ")


#loops

names = "Hamza"

for characters in names:
    print(characters)
"""

#dictionaries

houses = {"Harry":"Gryffindor", "Draco":"Slytherin"}