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
