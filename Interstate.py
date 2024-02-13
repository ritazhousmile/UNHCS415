# Name: Huan Zhou
# Conditional lab assignment
# interstate highways follow a sepcific number system


def road_direction(integer):
    if integer % 2 == 0:
        print("primary east-west")
    else:
        print("primary north-south")


def belt_or_spur(integer):
    digit_output = []
    string = str(integer)

    for digit_char in string:
        digit_output.append(int(digit_char))

    leftmost_digit_str = digit_output[0]
    leftmost_digit_int = int(leftmost_digit_str)
    rest_digit_str = digit_output[-2:]
    c_str = ""
    for number in rest_digit_str:
        c_str += str(number)
    if leftmost_digit_int % 2 == 0:
        print(f"beltway for I-{c_str}")
    else:
        print(f"spur for I-{c_str}")


print("Enter an interstate highway integer:")
input_integer = int(input())
input_str = str(input_integer)
output = []
for char in input_str:
    output.append(int(char))


output_length = len(output)

if input_integer >= 999 or input_integer <= 1:
    print("invalid")
elif output_length == 2:
    road_direction(input_integer)
elif output_length == 3:
    belt_or_spur(input_integer)




