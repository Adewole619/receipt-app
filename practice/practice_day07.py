# Ask the user for:

item_name = input("Enter Item name: ")
item_price = float(input("Enter item price: "))
item_quantity = int(input("Enter item quantity: "))

# Store them in a dictionary and print the dictionary.

item = {
    "name": item_name,
    "price": item_price,
    "quantity": item_quantity,
}

print(item)