import sys

RECEIPT_FILE = "data/receipts.txt"

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

def validate_input(store_name,receipt_number, item_name, price, quantity):

    if store_name == "" or receipt_number == "" or item_name=="" or quantity <= 0 or price <= 0:
        if store_name == "":
            print("Store name cannot be empty.")
        if receipt_number == "":
            print("Store name cannot be empty.")
        if item_name == "":
            print("Receipt number cannot be empty.")
        if quantity <= 0:
            print("Quantity must be greater than 0.")
        if price <= 0:
            print("Price must be greater than 0.")

        return False
    
    return True

def validate_string_input(field_name):
    while True:
        string_input = input(f"Enter {field_name} (or q to quit): ").strip()

        if string_input.lower() == "q":
            print("Program terminated.")
            sys.exit()

        if not string_input:
            print(f"{field_name} can not be empty. Try again.")
            continue
    
        # print(f"{field_name} is stored successfully")
        return string_input

def validate_num_input(field_name, num_type):
    while True:
        int_input = input(f"Enter {field_name} (or q to quit): ").strip()

        if int_input.lower() == "q":
            print("Program terminated.")
            sys.exit()
        try:
            if num_type == int:
                val = int(int_input)
            elif num_type == float:
                val = float(int_input)
            else:
                raise ValueError("num_type must be int or float")

            if val <= 0:
                print(f"{field_name} must be greater than 0. Try again.")
                continue
    
            # print(f"{field_name} is stored successfully.")
            return val
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def save_receipt(store_name, receipt_number, receipt_items, grand_total):
    with open(RECEIPT_FILE , "a") as file:
        file.write("==========RECEIPT==============\n")
        file.write(f"Store: {store_name}\n")
        file.write(f"Receipt No: {receipt_number}\n\n")

        for index, item in enumerate(receipt_items, start=1):
            
            file.write(f"{index}. {item['name']}\n")
            file.write(f"Price: ₦{item['price']:.2f}\n")
            file.write(f"Qty: {item['quantity']}\n")
            file.write(f"Subtotal: ₦{item['subtotal']:.2f}\n\n")

        file.write("------------------------\n")
        file.write(f"Grand Total: ₦{grand_total:.2f}\n")
        # print()

        file.write("Thank you for shopping!\n\n")

def load_receipts():
    try:
        with open(RECEIPT_FILE, "r") as file:
            return file.read()
    except FileNotFoundError:
        print("No receipts have been saved yet.")