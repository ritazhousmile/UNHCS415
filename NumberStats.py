# this is for the conditional lab
def number_stats(integer):
    print(f"+ Number entered: {integer}")
    even_boolean = bool(integer % 2 == 0)
    greater_than_fifty_boolean = bool(integer > 50)
    print(f"+ Number is even: {even_boolean}")
    print(f"+Number is greater than 50: {greater_than_fifty_boolean}")


print("Enter an integer:")
input_number = int(input())
number_stats(input_number)