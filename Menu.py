# Huan Zhou
# 09_Menu Lab
# 2/22/2024

# x, y = int(input("Please Enter x and y: "))
user_input = ""
while user_input is not "Q":
    x, y = input("Please Enter x and y: ")
    user_input = input("Please enter a command: ")

    if user_input == "A":
        result = int(x) + int(y)
        print(f"{x} + {y} = {result}")
    elif user_input == "S":
        result = int(y) - int(x)
        print(f"{y} - {x} = {result}")
    elif user_input == "Q":
        print("Goodbye")
        break
    else:
        print("Invalid command")

