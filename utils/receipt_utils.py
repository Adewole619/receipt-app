import sys
import json
import os

RECEIPT_FILE = "data/receipts.txt"
RECEIPT_FILE_JSON = "data/receipts.json"

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


def generate_receipt_number():
    # # Path to the JSON file where receipts are stored
    # file_name = "data/receipts.json"

    # If the receipts file does not exist, start with the first receipt number
    if not os.path.exists(RECEIPT_FILE_JSON):
        return "RCP0000001"

    try:
        # Open the receipts file and load its contents into a list
        with open(RECEIPT_FILE_JSON, "r") as file:
            receipts = json.load(file)
    except json.JSONDecodeError:
         # File exists but is empty or contains invalid JSON
        return "RCP0000001"

    # If the file exists but contains no receipts, start with the first receipt number
    if len(receipts) == 0:
        return "RCP0000001"

    # Get the most recently added receipt
    last_receipt = receipts[-1]

    # Extract the receipt number (e.g., "RCP0000005")
    last_number = last_receipt["receipt_number"]

    # Remove the "RCP" prefix and convert the remaining digits to an integer
    number = int(last_number.replace("RCP", ""))

    # Increment the receipt number by 1
    number += 1

    # Return the new receipt number with the "RCP" prefix
    # and pad the number with leading zeros to make it 7 digits long
    return f"RCP{number:07d}"

def save_receipt_json(receipt):

    try:
        with open(RECEIPT_FILE_JSON, "r") as file:
            receipts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        receipts = []

    receipts.append(receipt)

    with open(RECEIPT_FILE_JSON, "w") as file:
        json.dump(receipts, file, indent=4)



def search_by_receipt_number(rcp_number):
    
    saved_receipt_json = load_receipts_json()
    if not saved_receipt_json:
        return None

    rcp_number = rcp_number.strip().upper()

    for rcp in saved_receipt_json:
        if rcp["receipt_number"].strip().upper() == rcp_number :
            return rcp

    return None


def search_by_store(st_name):
    
    saved_receipt_json = load_receipts_json()
    if not saved_receipt_json:
        return []

    st_name = st_name.strip().lower()
    rcp_receipts = []
    for rcp in saved_receipt_json:
        if rcp["store"].strip().lower() == st_name:
            rcp_receipts.append(rcp)

    return rcp_receipts


def search_by_receipt_number(receipts, rcp_number):
    
    if not receipts:
        return None

    rcp_number = rcp_number.strip().upper()

    for rcp in receipts:
        if rcp["receipt_number"].strip().upper() == rcp_number :
            return rcp

    return None


def search_by_store(receipts, st_name):
    
    if not receipts:
        return []

    st_name = st_name.strip().lower()
    rcp_receipts = []
    for rcp in receipts:
        if rcp["store"].strip().lower() == st_name:
            rcp_receipts.append(rcp)

    return rcp_receipts


def update_receipt(rcp_number):
    receipts = load_receipts_json()
    receipt = search_by_receipt_number(receipts, rcp_number)
    if receipt is None:
        print("Receipt not found.")
    else:
        new_rcp_store_name = get_menu_choice(f"Update Store name?\nCurren store name: {receipt['store']}\n New store name: ")
        if not new_rcp_store_name:
            print("Store name cannot be empty.")
            return
        
        receipt["store"] = new_rcp_store_name
        try:
            save_all_receipts(receipts)
            print("Store updated successfully.")
        except OSError:
            print("Failed to save receipt.")
            return

def delete_receipt(receipts, rcp_number):
    receipt = search_by_receipt_number(receipts, rcp_number)
    if receipt is None:
        print("Receipt not found.")
        return None
    else:
        print_receipt_out(receipt)
        confirm_delete = input(
            "Permanently deleted receipts cannot be restored.\n"
            "Type Yes to delete or No to cancel: "
        )

        if confirm_delete.strip().lower() == "yes":
            receipts.remove(receipt)
            save_all_receipts(receipts)
            print("Receipt deleted successfully")
            return True
        
        return False

def delete_receipt_object(receipts, receipt):
    if receipt is None:
        return False
    
    print_receipt_out(receipt)
    confirm_delete = input(
                "Permanently deleted receipts cannot be restored.\n"
                "Type Yes to delete or No to cancel: "
            )
    if confirm_delete.strip().lower() == "yes":
                receipts.remove(receipt)
                save_all_receipts(receipts)
                print("Receipt deleted successfully")
                return True
    
    return False

def choose_receipt(receipts):
    try:
        select_index = int(get_menu_choice("0. cancel selection\nPick selection-number: "))
        if select_index == 0:
            print("Cancelling...")
            return None
        elif 1 <= select_index <= len(receipts):
            return receipts[select_index - 1]
        else:
            print("Invalid display number.")
            return None
    except (ValueError, IndexError):
        print("Enter selection number")
        return None




def get_receipt_number():
    return input("Enter receipt number: ").strip().upper()