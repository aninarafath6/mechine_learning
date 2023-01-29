# about variables
a = 20
b = 21.2
print(a+b)
# Type casting
print(int(b))
print(float(a))


print("\n\n====> Strings <==== \n\n")
# Strings
string1 = "Hello World "
string2 = "this is string two"
multiLineString = """ This is 
Multi Line String"""

print(string1[1])
print(string1)
print(string2)
print(multiLineString)
print(string1+string2)
print(str(a) + string1)
# substrings
print(string1[1:3])
print(string1[1:])
print(string1[:10])
# reverse string
print(string1[::-1])

# String Functions
print("   Apple   ".strip())  # remove white spaces
print("   To Upper   ".upper())
print("   to LOWER   ".lower())
print("   Replace   ".replace("R", "x"))  # replace with
print("apple,orange,grapes".split(","))  # split

name = " Arafath"
age = 15

template = "My name is {} and my age is {}"
print(template.format(name, age))


# boolean
x = True
y = not True
