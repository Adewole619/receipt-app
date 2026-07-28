from utils.receipt_utils import calculate_subtotal, validate_input

store_name = input("Enter Store name: ")

receipt_items = []

# items = []
# prices = []
# quantities = []
# sub_totals = []


count = int(input("How many items? "))

grand_total = 0

for i in range(count):
    item_name = input(f"enter item {i+1} name: ")
    item_price = float(input("enter item price: "))
    item_quantity = int(input("How many(Quantity): "))

    if validate_input(store_name, item_name, item_price,item_quantity ):

        sub_total = calculate_subtotal(item_price, item_quantity)

        # items.append(item_name)
        # prices.append(item_price)
        # quantities.append(item_quantity)
        
        # sub_totals.append(sub_total)

        item = {
            "name": item_name,
            "price": item_price,
            "quantity": item_quantity,
            "subtotal": sub_total,
        }
        receipt_items.append(item)

        grand_total += sub_total 

print()
print("========================")
print("        RECEIPT")
print("========================")
print()

print(f"Store: {store_name}")
print()

# for i in range(count):
#     print(f"{i+1}. {items[i]}")
#     print(f"Price: ₦{prices[i]:.2f}")
#     print(f"Qty: {quantities[i]}")
#     print(f"Subtotal: ₦{sub_totals[i]:.2f}")
#     print()

for index, item in enumerate(receipt_items, start=1):
    
    print(f"{index}. {item['name']}")
    print(f"Price: ₦{item['price']:.2f}")
    print(f"Qty: {item['quantity']}")
    print(f"Subtotal: ₦{item['subtotal']:.2f}")

print("------------------------")
print(f"Grand Total: ₦{grand_total:.2f}")
print()

print("Thank you for shopping!")