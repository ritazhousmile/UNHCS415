# rita Zhou
# CS415 Quiz #1 (programming)
# Feb 15, 2024


# write a function  mad_lib

def mad_lib(a, b, c, d):
    print(f"Roses are {a}")
    print(f"{b} are blue")
    print(f"{c} is {d}")
    print("And so are you!")


# get user input
adj1 = input("Enter an adjective: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
adj2 = input("Enter an adjective: ")

# calling mad_lib function
mad_lib(adj1, noun1, noun2, adj2)
