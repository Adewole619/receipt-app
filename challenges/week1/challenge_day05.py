def calculate_subtotal(price, quantity):
    return price * quantity

def print_receipt(store_name, item_name, price, quantity, subtotal):
    print("========================")
    print("        RECEIPT")
    print("========================")
    print()
    print(f"Store: {store_name}")
    print(f"Item: {item_name}")
    print(f"Price: #{price:.2f}")
    print(f"Quantity: {quantity}")
    print("")
    print(f"Subtotal: {subtotal:.2f}")
    print()
    print("Thank you for shopping!")

def validate_input(store_name, item_name, price, quantity):

    if store_name == "" or item_name=="" or quantity <= 0 or price <= 0:
        if store_name == "":
            print("Store name cannot be empty.")
        if item_name == "":
            print("Item name cannot be empty.")
        if quantity <= 0:
            print("Quantity must be greater than 0.")
        if price <= 0:
            print("Price must be greater than 0.")

        return False
    
    return True
