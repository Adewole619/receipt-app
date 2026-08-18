import sys
import json
import os

from utils.validation import (
    get_menu_choice,
    validate_num_input,
    validate_string_input
)

from utils.store_utils import load_stores_json, search_store_by_id
from utils.product_utils import deduct_stock

from utils.product_utils import (
    load_products_json,
    search_product_by_id,
    save_all_products
)
from utils.customer_utils import get_customer_for_receipt

RECEIPT_FILE = "data/receipts.txt"
RECEIPT_FILE_JSON = "data/receipts.json"
CUSTOMER_FILE_JSON = "data/customers.json"

# ------------------STORAGE METHODS------------------------------
def save_all_receipts(receipts):
    with open(RECEIPT_FILE_JSON, "w") as file:
        json.dump(receipts, file, indent=4)


def load_receipts_json():
    try:
        with open(RECEIPT_FILE_JSON, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No receipts have been saved yet.")
        return []


def save_receipt_json(receipt):

    try:
        with open(RECEIPT_FILE_JSON, "r") as file:
            receipts = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        receipts = []

    receipts.append(receipt)

    try:
        with open(RECEIPT_FILE_JSON, "w") as file:
            json.dump(
                receipts,
                file,
                indent=4
            )

        return True

    except OSError:
        print("Could not save receipt.")
        return False
# ----------------------RECEIPT ID METHOD------------------------------

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

# ------------------------RECEIPT SEARCHING METHODS -----------------------

def search_by_receipt_number(rcp_number):
    
    saved_receipt_json = load_receipts_json()
    if not saved_receipt_json:
        return None

    rcp_number = rcp_number.strip().upper()

    for rcp in saved_receipt_json:
        if rcp["receipt_number"].strip().upper() == rcp_number :
            return rcp

    return None


def search_by_store(store_name):
    
    saved_receipt_json = load_receipts_json()
    if not saved_receipt_json:
        return []

    store_name = store_name.strip().lower()
    rcp_receipts = []
    for rcp in saved_receipt_json:
        if rcp["store"].strip().lower() == store_name:
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


def search_by_store(receipts, store_name):
    
    if not receipts:
        return []

    store_name = store_name.strip().lower()
    rcp_receipts = []
    for rcp in receipts:
        if rcp["store"].strip().lower() == store_name:
            rcp_receipts.append(rcp)

    return rcp_receipts
#--------------------------------CREATE RECEIPT--------------------

def create_receipt():
    # store_name = validate_string_input("Store name")
    stores = load_stores_json()
    products = load_products_json()

    store_id = input("Enter Store ID: ").strip().upper()

    store = search_store_by_id(stores, store_id)
    if store is None:
        print("Store not found.")
        return None

    store_name = store["store_name"]

    customer = get_customer_for_receipt()
    if customer is None:
        print("Customer selection failed.")
        return None
    customer_id = customer["customer_id"]

    receipt_number = generate_receipt_number()

    receipt_items = []

    while True:

        completed = receipt_cart_menu(
            receipt_items,
            products,
            store
        )

        if not completed:
            return None

        grand_total = 0

        for item in receipt_items:
            grand_total += item["subtotal"]

        receipt = {
            "store": store_name,
            "receipt_number": receipt_number,
            "customer_id": customer_id,
            "items": receipt_items,
            "grand_total": grand_total,
        }

        confirmation = confirm_receipt(receipt)

        if confirmation == "confirm":
            break

        elif confirmation == "edit":
            continue

        elif confirmation == "cancel":
            print("Receipt creation cancelled.")
            return None
    
    if not finalize_receipt(receipt, products):
        print("Receipt could not be completed.")
        return None

    print("Receipt successfully created.")
      
    return receipt

def receipt_cart_menu(
    receipt_items,
    products,
    store
):

    while True:

        print("\n========== RECEIPT ITEMS ==========")

        print("1. Add Product")
        print("2. Remove Product")
        print("3. Update Product Quantity")
        print("4. View Current Receipt")
        print("5. Finish Receipt")
        print("6. Cancel Receipt")

        choice = input(
            "\nChoose an option: "
        ).strip()

        if choice == "1":

            add_product_to_receipt(
                receipt_items,
                products,
                store
            )

        elif choice == "2":

            remove_product_from_receipt(
                receipt_items
            )
        elif choice == "3":
                
            update_product_quantity(
                receipt_items,
                products
            )
                
        elif choice == "4":

            print_receipt_cart(
                receipt_items
            )

        elif choice == "5":

            if not receipt_items:
                print(
                    "You must add at least "
                    "one product."
                )
                continue

            return True

        elif choice == "6":

            print("Receipt creation cancelled.")

            return False

        else:

            print("Invalid option.")

def remove_product_from_receipt(receipt_items):

    if not receipt_items:
        print("There are no products to remove.")
        return False

    product_id = input(
        "Enter Product ID to remove: "
    ).strip().upper()

    for item in receipt_items:

        if item["product_id"] == product_id:

            receipt_items.remove(item)

            print(
                f"{item['name']} removed "
                "from receipt."
            )

            return True

    print("Product is not on this receipt.")

    return False

def add_product_to_receipt(
    receipt_items,
    products,
    store
):
    product_id = input(
        "Enter Product ID: "
    ).strip().upper()

    product = search_product_by_id(
        products,
        product_id
    )

    if product is None:
        print("Product not found.")
        return False

    if product["store_id"] != store["store_id"]:
        print(
            "This product does not belong "
            "to the selected store."
        )
        return False

    # Prevent adding the same product twice
    for item in receipt_items:
        if item["product_id"] == product["product_id"]:
            print(
                f"{product['name']} is already "
                "on this receipt."
            )
            return False

    print(f"\nProduct: {product['name']}")
    print(f"Price: ₦{product['price']:,.2f}")
    print(
        f"Available stock: "
        f"{product['stock_quantity']}"
    )

    quantity = validate_num_input(
        f"Enter {product['name']} quantity",
        int
    )

    if quantity > product["stock_quantity"]:
        print(
            f"Insufficient stock. "
            f"Only {product['stock_quantity']} "
            "available."
        )
        return False

    subtotal = calculate_subtotal(
        product["price"],
        quantity
    )

    item = {
        "product_id": product["product_id"],
        "name": product["name"],
        "price": product["price"],
        "quantity": quantity,
        "subtotal": subtotal
    }

    receipt_items.append(item)

    print(
        f"{product['name']} added successfully."
    )

    return True

def print_receipt_cart(receipt_items):
    print("\n========== CURRENT RECEIPT ==========")

    if not receipt_items:
        print("No products have been added.")
        print("=====================================")
        return

    grand_total = 0

    for i, item in enumerate(receipt_items, start=1):
        print(f"\n[{i}] {item['name']}")
        print(f"    Product ID: {item['product_id']}")
        print(f"    Quantity:   {item['quantity']}")
        print(f"    Price:      ₦{item['price']:,.2f}")
        print(f"    Subtotal:   ₦{item['subtotal']:,.2f}")

        grand_total += item["subtotal"]

    print("\n-------------------------------------")
    print(f"Grand Total: ₦{grand_total:,.2f}")
    print("=====================================")

def finalize_receipt(receipt, products):

    receipt_items = receipt["items"]

    # Step 1: Validate stock
    for item in receipt_items:

        product = search_product_by_id(
            products,
            item["product_id"]
        )

        if product is None:
            print(
                f"Product {item['product_id']} "
                "no longer exists."
            )
            return False

        if item["quantity"] > product["stock_quantity"]:
            print(
                f"Not enough stock for "
                f"{product['name']}."
            )
            return False

    # Step 2: Save receipt
    if not save_receipt_json(receipt):
        print("Receipt could not be saved.")
        return False

    # Step 3: Deduct stock
    for item in receipt_items:

        product = search_product_by_id(
            products,
            item["product_id"]
        )

        product["stock_quantity"] -= item["quantity"]

    # Step 4: Save products
    save_all_products(products)

    return True

def confirm_receipt(receipt):
    while True:

        print("\n========== RECEIPT REVIEW ==========")

        print(f"Store: {receipt['store']}")
        print(f"Receipt Number: {receipt['receipt_number']}")
        print(f"Customer ID: {receipt['customer_id']}")

        print("\nItems:")

        for i, item in enumerate(receipt["items"], start=1):
            print(
                f"{i}. {item['name']} "
                f"x {item['quantity']} "
                f"= ₦{item['subtotal']:,.2f}"
            )

        print("\n-------------------------------------")
        print(
            f"Grand Total: "
            f"₦{receipt['grand_total']:,.2f}"
        )
        print("-------------------------------------")

        print("\n1. Confirm & Save")
        print("2. Go Back & Edit")
        print("3. Cancel")

        choice = input(
            "\nChoose an option: "
        ).strip()

        if choice == "1":
            return "confirm"

        elif choice == "2":
            return "edit"

        elif choice == "3":
            return "cancel"

        else:
            print("Invalid option.")

def update_product_quantity(receipt_items, products):

    if not receipt_items:
        print("There are no products on the receipt.")
        return False

    product_id = input(
        "Enter Product ID to update: "
    ).strip().upper()

    for item in receipt_items:

        if item["product_id"] == product_id:

            product = search_product_by_id(
                products,
                product_id
            )

            if product is None:
                print("Product no longer exists.")
                return False

            print(f"\nProduct: {item['name']}")
            print(f"Current quantity: {item['quantity']}")
            print(f"Available stock: {product['stock_quantity']}")

            new_quantity = validate_num_input(
                "Enter new quantity",
                int
            )

            if new_quantity > product["stock_quantity"]:
                print(
                    f"Insufficient stock. "
                    f"Only {product['stock_quantity']} available."
                )
                return False

            item["quantity"] = new_quantity

            item["subtotal"] = calculate_subtotal(
                item["price"],
                new_quantity
            )

            print(
                f"{item['name']} quantity updated "
                "successfully."
            )

            return True

    print("Product is not on this receipt.")

    return False


# -----------------------------RECEIPTS MODIFICATION METHODS----------------------------------

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


# ------------------------RECEIPT DISPLAY-----------------------

def print_receipt_out(receipt):
    store_name = receipt["store"]
    receipt_number = receipt["receipt_number"]
    receipt_items = receipt["items"]
    grand_total = receipt["grand_total"]
    print("==========RECEIPT==============")
    print(f"Store: {store_name}")
    print(f"Receipt No: {receipt_number}\n")

    for index, item in enumerate(receipt_items, start=1):
            
        print(f"{index}. {item['name']}")
        print(f"Price: ₦{item['price']:.2f}")
        print(f"Qty: {item['quantity']}")
        print(f"Subtotal: ₦{item['subtotal']:.2f}\n")

    print("------------------------")
    print(f"Grand Total: ₦{grand_total:.2f}")
        # print()

    print("Thank you for shopping!\n")

#------------------------------------------------END-----------------------------------------------------------------------
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


def get_receipt_number():
    return input("Enter receipt number: ").strip().upper()

def print_a_receipt(receipt, title="Receipt"):
    print(f"{title}")
    print(f"Store:         {receipt['store']}")
    print(f"Receipt:       {receipt['receipt_number']}")
    print(f"Grand Total:   ₦{receipt['grand_total']:,.2f}\n")