# python's built-in method : id :
name = "Amit"
age = 27

print(id(name))
print(id(age))

y = 27

if(id(age) == id(y)):
    print(True)
else:
    print(False)

# Variable names are case-sensitive :
place = "Hajipur"
PLACE = "Patna"
pLace = "Vaishali"

print(place, PLACE, pLace)

# reserved keywords cannot be used as a variable name :
# def = 99
# True = False
# print(True)

# Variable names should be a single word only :
# first name = "Amit"
# print(first name)
firstname = "Amit"
print(firstname)

# variables name should be logical :
lastName = "Raj"
last = "Raj"