my_number = 5
value = int(input("what number am I thinking of?"))

while (value != my_number) :
    if (value > 5):
        print("too high")
    else:
        print("too low")
    value = int(input("unlucky, try again..."))

print("well done")