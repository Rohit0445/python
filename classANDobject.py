class student:
    name= "Rohit Meena"
    city = "Vidisha"

# same Address not a object 
# x = student
# print(id(x))
# print(id(student))

# difference address is an object 
x = student()
print(id(x))
print(id(student))
print(dir(student))