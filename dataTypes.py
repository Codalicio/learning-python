# Different data types in python :

# Numerical Data Types :

# Integer :
x = 5
print(x, type(x))

# float :
y = 12.34
print(y, type(y))

num = 3e4
print(num, type(num))

# complex number :
z = 5 + 9j
print(z, type(z))
print(z.real, type(z.real))
print(z.imag, type(z.imag))

# Some in-built method for numbers in python :

# abs() method :
print(abs(-5))

# pow() method :
power = pow(3, 4)
print(power)

# round() method :
print(round(4.75))
print(round(4.5))

# min(), max() and sum() methods for list of numbers :
nums = [4, 5, 1, 2, 8, 3, 6, 7]
print(min(nums))
print(max(nums))
print(sum(nums))

# List Data Type :
# Elements in lists are ordered, i.e., index based element position and lists are mutable.

students = ["Vishwa", "Shivani", "Amit", "Raj", "Sonu"]
print(students, type(students))

# Creating list using a constructor :

# list using another list :
list1 = list(students)
print(list1, type(list1))
list1.append("Monu")
print(list1)
print(students)

# list using a string :
list2 = list("abcdefghij")
print(list2)

# list using a tuple :
list3 = list((1, 2, "Amit", "Raj"))
print(list3)

# Accessing the elements of a list :
list4 = [4, 5, 8, 9, 1, 7, 3, 2]
print(list4[4])
print(list4[-5])

# Inserting elements to a list using in-built methods :

# append() method :
arr1 = [3, 5, 6, 8, 7]
arr1.append(23)
print(arr1, type(arr1))

# insert() method :
arr2 = [1, 3, 5, "Amit"]
arr2.insert(0, "Raj")
print(arr2, type(arr2))
arr2.insert(3, 43)
print(arr2, type(arr2))

# extend() method :
l1 = [1, 3]
l2 = ["Amit", "Raj"]
l1.extend(l2)
l2.extend(l1)
print(l1, type(l1))
print(l2, type(l2))

# Removing/deleting elements of a list using in-built functions :

# remove() method :
l3 = [4, 5, 7, 8, 1, 34, 56]
l3.remove(1)
print(l3, type(l3))

# If the list has two elements with the same value, then remove() will remove the first occurrence only :
l4 = [3, 4, 6, 1, 8, 1, 9, 1]
l4.remove(1)
print(l4, type(l4))

# pop() method :
l5 = [7, 8, 99, 45, 43]
poppedElement = l5.pop()
print(poppedElement)
print(l5, type(l5))

# removing an element at a specific index using pop() method :
l6 = [78, 12, 33, 45, 65, 85]
poppedElement1 = l6.pop(2)
print(poppedElement1)
print(l6, type(l6))

# Replacing an element at a specific index or range of indexes in a list :

arr3 = list("abcdefghi")
arr3[2] = 'j'
print(arr3, type(arr3))

# for a range of elements :
arr3[3:7] = "m", "n", "o", "p"
print(arr3, type(arr3))

arr3[1:3] = "A"
print(arr3, type(arr3))
arr3[1:4] = "Amit"
print(arr3, type(arr3))

# Some in-built methods/functions for lists :

# reverse() method :
arr4 = [1, 3, 5, 7, 9]
arr4.reverse()
print(arr4)

# copy() method (Creates a copy of a list but will be a different object) :
arr4_copy = arr4.copy()
print(arr4_copy, type(arr4_copy))
print(arr4_copy == arr4)
print(id(arr4_copy), id(arr4))

# sort() method :
arr5 = [7, 9, 5, 11, 3, 4, 10]
arr5.sort()
print(arr5)

# Sequence Data Types :

# string :
name = 'Amit'
city = "Hajipur"
message = '''Hello everyone, this is a message!'''

fullName = "Amit Raj"
print(len(fullName))
print(fullName[3])
print(fullName[-len(fullName)])
print(fullName[0:4])

# Some important in-built methods for strings :

# String concatenation :
first_name = "Amit"
last_name = "Raj"
complete_name = first_name + " " + last_name
print(complete_name)

# len() method :
print(len(complete_name))

# String Slicing :

str = "Amit Raj"
print(str[1:4])

print(str[0:])

print(str[:8])

print(str[0:])

print(str[:])

print(str[-6:-1])

print(str[-1:-12:-1])

print(str[-7:4:])

# upper() method :
str1 = "amit"
newString = str1.upper()
print(newString)

# lower() method :
newString1 = newString.lower()
print(newString1)

# capitalize() method :
newString2 = newString1.capitalize()
print(newString2)

# strip() method :
newString3 = "     Amit      "
newString4 = newString3.strip()
print(newString4)

# replace() method :
str2 = "I am imperfect but; I am very talented, I am very hardworking, and I am super smart."
str3 = str2.replace("I am", "We are")
print(str3, type(str3), len(str3))

str4 = str3.replace("We are", "I am", 2)
print(str4, type(str4), len(str4))
