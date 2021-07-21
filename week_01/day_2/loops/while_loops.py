counter = 0
my_number = 5
random = 7

# while (counter < my_number) :
#     print (f"counter is {counter}")
#     counter += 1

while (True):
    line = input("type something (type q to quit) ")
    if (line.lower() == "q"):
        break
    print(f"you typed: {line}")


