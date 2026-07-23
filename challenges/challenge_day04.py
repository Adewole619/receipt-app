store_Name = input("Enter your store name: ")
item_Name = input("Enter an item: ")
price = float(input("Item price: "))
quantity = int(input("How many item: "))


print()
print()

if store_Name == "" or item_Name=="" or quantity <= 0 or price <= 0:
    if store_Name == "":
        print("Store name cannot be empty.")
    if item_Name == "":
        print("Item name cannot be empty.")
    if quantity <= 0:
        print("Quantity must be greater than 0.")
    if price <= 0:
        print("Price must be greater than 0.")
else:
    sub_Total = price * quantity
    print("========================")
    print("        RECEIPT")
    print("========================")
    print()
    print(f"Store: {store_Name}")
    print(f"Item: {item_Name}")
    print(f"Price: #{price}")
    print(f"Quantity: {quantity}")
    print("")
    print(f"Subtotal: {sub_Total:.2f}")
    print()
    print("Thank you for shopping!")
