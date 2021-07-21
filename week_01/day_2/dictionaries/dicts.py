# list
items = ("one", "two", "three")

# dictionaries
meals = {}  # creates an empty dict
#  empty_dict = dict()         # also creates an empty dict

meals = {"breakfast": "toast", "lunch": "wrap", "dinner": "curry"}

# print(meals)

silly = {1: "2", 2: "3", 3: "false"}
# print(silly)

# print("breakfast" in meals)

# print(meals.values())


meals["lunch"] = "pasta"
# print(meals)

meals["supper"] = "pancakes"
# # print(meals)

# remove from dict
del meals["breakfast"]
#   print(meals)

# nested dict
countries = {"uk": "london", "germany": "berlin"}

countries = {
    "uk": {"capital": "london", "pop": 100000},
    "germany": {"capital": "berlin", "pop": 20000},
}

# print(countries)

# print(countries["germany"]["capital"])


# =============================
# Make a dictionary called avengers. It should contain keys for Iron Man and Hulk.
# Each avenger is represented by another dictionary, and has a name (Tony Stark and Bruce Banner respectively) and another dictionary containing their attacks.
# Each attack should have an int value of the attack's power. Iron man can punch (10) and kick (100) and Hulk can smash (1000) and roll (500).
# Once you have created the dictionary, retrieve and print out the attack power of Hulks smash move.

avengers = {
    "iron_man": {
        "name": "tony stark", 
        "attack values": {
            "punch": 10, 
            "kick": 100
            }
        },
    "hulk": {
        "name": "bruce banner", 
        "attack values": {
            "smash": 1000, 
            "roll": 500
            }
        },
}

print(avengers["hulk"]["attack values"]["smash"])
