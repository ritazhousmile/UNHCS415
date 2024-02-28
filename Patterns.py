# Huan Zhou
# 10_patterns Lab
# 02/27/2024


print("Enter Pattern:")
letter = input()

if letter == "H":
    print("Enter a positive integer between 1 and 10 inclusive: ")
    int_input = int(input())
    pattern = "*" * int_input
    print(pattern)
elif letter == "V":
    print("Enter a positive integer between 1 and 10 inclusive: ")
    int_input = int(input())
    pattern = "*\n"
    number_of_pattern = pattern * int_input
    print(number_of_pattern)
elif letter == "S":
    print("Enter a positive integer between 1 and 10 inclusive: ")
    int_input = int(input())
    pattern = "****"
    i: int = 0
    while i in range(int_input):
        pattern = "****"
        print(pattern)
        i += 1
elif letter == "T":
    print("Enter a positive integer between 1 and 10 inclusive: ")
    int_input = int(input())
    i: int = 0
    while i in range(int_input):
        pattern = "*" * (i+1)
        print(pattern)
        i += 1
elif letter == "D":
    print("Enter a positive integer between 1 and 10 inclusive: ")
    int_input = int(input())
    i: int = 0
    while i in range(int_input):
        pattern = (" "*i)+"*"
        print(pattern)
        i += 1

