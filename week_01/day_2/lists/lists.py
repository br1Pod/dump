fruits = ["apple", "banana", "grape", "orange"]
# print(fruits)

# print(fruits[3])

# print(fruits[-1])

# fruits[1] = "mango"

# number_of_fruits = len(fruits)
# print(number_of_fruits)

fruits.append("pear")

fruits.pop()  # removes end item
print(fruits)

fruits.pop(2)  # removes item in index 2
print(fruits)

# nested
nested_list = [1, 2, 3, [3.1, 3.2, 3.3], 4, 5]
print(nested_list)
print(nested_list[3][1])
