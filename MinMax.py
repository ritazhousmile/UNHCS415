# huan zhou
# quiz 2
# 02/29/2024


command = ""
# a command
number_list = []
while command is not "q":
    print("Enter a command.")
    command = input()

    # a command
    if command == "a":
        print("Enter the number to add.")
        number_add = int(input())
        number_list.append(number_add)

        # M command
    elif command == "M":
        print(number_list)
        if len(number_list) == 0:
            print("No elements in list")
        else:
            largest_number = max(number_list)
            print(f"The largest number is {largest_number}")
    elif command == "m":
        print(number_list)
        if len(number_list) == 0:
            print("No elements in list")
        else:
            smallest_number = min(number_list)
            print(f"The smallest number is {smallest_number}")
        # <
    elif command == "<":
        print("Enter the threshold for this search.")
        number_threshold = int(input())
        if len(number_list) == 0:
            print("The numbers below this threshold are []")
        else:
            new_list = []
            for n in number_list:
                if n < number_threshold:
                    new_list.append(n)
            print(f"The numbers below this threshold are {new_list}")

    # >
    elif command == ">":
        print("Enter the threshold for this search.")
        number_threshold = int(input())
        if len(number_list) == 0:
            print("The numbers below this threshold are []")
        else:
            new_list = []
            for n in number_list:
                if n > number_threshold:
                    new_list.append(n)
            print(f"The numbers below this threshold are {new_list}")

        # d
    elif command == "d":
        print("Enter the number to remove.")
        number_to_remove = int(input())
        if number_to_remove not in number_list:
            print(f"{number_to_remove} was not found in the list")
        else:
            number_list.remove(number_to_remove)
            print(f"{number_to_remove} was removed from the list")
            # q#
    elif command == "q":
        print("Goodbye")
        break
    # any other command
    else:
        print("Invalid command")
        continue
