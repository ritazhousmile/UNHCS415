thisTuple = ("apple", "banana", "cherry")
print(thisTuple)

#Tuples are ordered, unchangeable, and allow for duplicate values
#Tuple items have a defined order which will not change
#They are ordered by its index, the first item is at [0], second at [1], and so on
#Tuple items cannot be changed
#No adding / removing items

print(len(thisTuple))

#If you need a tuple with 1 item, you need to add a comma after the first item
#If there is no comma, Python will not make it a tuple

tuple_example = ("apple",)

print(type(tuple_example))


#divmod() takes two arguments and returns a tuple of two values, the quotient and remainder.
t = divmod(7,3)
print(t)