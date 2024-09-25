# This is a single line comment

# DocString or multi line comment :
'''
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Suspendisse nisl urna, bibendum vel arcu quis, ultrices interdum neque. 
Suspendisse ut fringilla mauris. Vivamus a aliquam ex, ut tempus erat. Nunc consectetur dui non orci tincidunt varius. 
Nam dignissim libero ut mi condimentum facilisis. Curabitur vestibulum enim augue, at porta urna pulvinar et. Suspendisse commodo 
ante id accumsan dapibus. Maecenas eu laoreet nunc, ut posuere tellus. Nulla id turpis a tortor faucibus auctor. Cras iaculis 
tellus arcu, vel consectetur nulla commodo id. Phasellus eu tempus eros, nec blandit purus.
'''

# In-built input() method :
name = input("Enter your fullname : ")
print(name)

# Output :
# In-built print() method that can take multiple comma(, ) separated arguments :
fullName = "Amit Raj"
age = 99
print("My name is", fullName, "and my age is", age, ".")

# Formatted string or f-string :
print(f"My name is {fullName} and my age is {age}.")

# printing with a separator attribute (sep="") :
x = 2
y = 6
z = 9
print(x, y, z, sep="-")

# printing with an (end="") attribute :
print("Hello", end = " ")
print("World", end = " ")
print("!")
