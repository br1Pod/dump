# List Comprehension
# evens_squared = [expression for item in list if condition]


# #Part 1
# # Using single list comprehension, and the following list:
# ages = [5, 15, 64, 27, 84, 26]
# Return a list of only the odd ages.

ages = [5, 15, 64, 27, 84, 26]
odd_ages = [age for age in ages if age % 2 != 0]
print(odd_ages)

# Part 2
# Using single list comprehension, and the following list:
# chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
# Return a list with chickens whose name is more than 10 characters
# Return a list of chickens whose name starts with the letter H

chicken_names = ["Hen Solo", "Cluck Norris", "Hennifer Lopez", "ChewPekka", "Feather Locklear"]
ten_char_plus = [chicken for chicken in chicken_names if len(chicken) > 10]
print(ten_char_plus)

found_h = [name for name in chicken_names if name[0] == "H"]
print(found_h)

# Part 3
# Using a single list comprehension, and the following list:
# words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]
# Build a new list, with the first letter from each word
# Convert each letter to lower case
# Expected output: ["t", "q", "b", "f", "j", "o", "t", "l", "d"]
# Hint: Strings in Python work as if they were a tuple full of characters. 
# How would you get the first element from a tuple or list?

words = ["The", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

list_from_letters = [word[0].lower() for word in words]
print(list_from_letters)