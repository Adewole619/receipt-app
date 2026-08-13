from utils.storage import load_receipts_json
from utils.menus import get_menu_choice
from utils.receipt_utils import print_a_receipt, validate_string_input
import os
import json

CUSTOMER_FILE_JSON = "data/customers.json"

receipts = load_receipts_json()


# customer = {
#     "customer_id": "CUS000001",
#     "name": "Ayoola",
#     "phone": "08000000000"
# }

# receipt = {
#     "store": store_name,
#     "receipt_number": receipt_number,
#     "customer_id": customer_id,
#     "items": receipt_items,
#     "grand_total": grand_total
# }



def save_customer(customer):

    try:
        with open(CUSTOMER_FILE_JSON, "r") as file:
            customers = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        customers = []

    customers.append(customer)

    with open(CUSTOMER_FILE_JSON, "w") as file:
        json.dump(customers, file, indent = 4)
    



def load_customers():
    try:
        with open(CUSTOMER_FILE_JSON, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"NO customer has been saved yet.")
        return []














receipts = [
    {
        "store": "Lagos",
        "receipt_number": "RCP0000001",
        "customer_id": "CUS000001",
        "items": [],
        "grand_total": 50000.0
    },
    {
        "store": "Abuja",
        "receipt_number": "RCP0000002",
        "customer_id": "CUS000002",
        "items": [],
        "grand_total": 30000.0
    },
    {
        "store": "Ibadan",
        "receipt_number": "RCP0000003",
        "customer_id": "CUS000001",
        "items": [],
        "grand_total": 75000.0
    }
]


# result = search_receipts_by_customer(receipts, "CUS000001")

# customer = search_customer_by_customer_id(customers, "CUS000001")

# history = customer_purchase_history(customers, receipts, "CUS000001")

# print_customer_purchase_history(history)










        
customers = [
    {
        "customer_id": "CUS000001",
        "name": "Ayoola",
        "phone": "08000000000"
    },
    {
        "customer_id": "CUS000002",
        "name": "John",
        "phone": "08111111111"
    }
]

customer = search_customer_by_phone(customers, "09099999999")

# if customer:
#     print("Customer already exists.")
#     print(customer)
# else:
#     print("Customer does not exist.")

customer3 = get_customer_for_receipt()
print(customer3)

# receipt = {
#     "store": store_name,
#     "receipt_number": receipt_number,
#     "customer_id": customer["customer_id"],
#     "items": receipt_items,
#     "grand_total": grand_total
# }