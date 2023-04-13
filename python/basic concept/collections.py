# list
# tuple
# set
# dictionary


# list - > normal like array....
fruits = ["apple", "orange", "grapes", 3, .22, ["sample,another"]]
print(fruits[1:5])
print(fruits[:5])
fruits.append("banana")
fruits.insert(2, "kiwi")
copy = fruits.copy()  # copy
copy = list(fruits)  # another method for copy
new_fruits = fruits + copy
fruits.remove("orange")
fruits.pop()
del fruits[5]
print(fruits)
print(copy)
print(new_fruits)
copy.extend(fruits)
print(copy)




# tuple -> constant we cannot change it .
bucket = ("brush", "paste")

print("brush" in bucket)
print(len(bucket))
print(print("HI"))


# dictionary
student = {
    "name ": "Arafath",
    "age": 18,
    "class": "+2"
}

print(student)
print(student.values())
print(student.keys())
