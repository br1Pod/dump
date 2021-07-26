numbers = range(1, 11)      # will hold numbers 1 - 10

# evens_squared = []

# for number in numbers:
#     if number % 2 == 0:
#         evens_squared.append(number ** 2)       #  ** = to power of


# evens_squared = [expression for item in list if condition]

evens_squared = [number ** 2 for number in numbers if number % 2 == 0]

print(evens_squared)