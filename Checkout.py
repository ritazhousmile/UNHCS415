# Huan Zhou
# 13_Checkout Lab
# 03/05/2024


items = []
total = 0
words = ""
print("Welcome to 415-Mart!")
i = True
while i:
    print("Please enter an item to purchase.")
    grocery = input()
    if grocery == "Done":
        i = False
    else:
        print("Please enter the cost of this item.")
        price = float(input())
        grocery_item = (grocery, price)
        items.append(grocery_item)
        total += price

print("----------")
print("Receipt:")
for item, price in items:
    print(f"{item: <25} {price: ^10.2f}")
print(f"Total: ${total: ^8.2f}")
