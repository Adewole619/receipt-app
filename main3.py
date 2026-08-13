from utils.storage import load_receipts_json
from utils.receipt_utils import print_a_receipt
import os
import json

CUSTOMER_FILE_JSON = "data/customers.json"

receipts = load_receipts_json()


customer = {
    "customer_id": "CUS000001",
    "name": "Ayoola",
    "phone": "08000000000"
}

# receipt = {
#     "store": store_name,
#     "receipt_number": receipt_number,
#     "customer_id": customer_id,
#     "items": receipt_items,
#     "grand_total": grand_total
# }

def generate_customer_id():
    # path to the json file where customer-id are stored
    # file_name = "data/customer.json"

    #if the customer file does not exist, start with the first customer-id
    if not os.path.exists(CUSTOMER_FILE_JSON):
        return "CUS000001"

    try:
        # Open the customers file and load its contents into a list
        with open(CUSTOMER_FILE_JSON, "r") as file:
            customers = json.load(file)
    except json.JSONDecodeError:
        # File exists but is empty or contains invalid JSON
        return "CUS000001"

    # If the file exists but contains no customer, start with the first customer-id
    if len(customers) == 0:
        return "CUS000001"

    # Get the most recently added customer-id
    last_customer = customers[-1]

    # Extract the customer-id (e.g CUS0000007 )
    last_customer_id = last_customer["customer_id"]

    # Remove the "CUS"prefix and convert the remaining digits to an interger
    number = int(last_customer_id.replace("CUS", ""))

    # Increase the id number by 1
    number += 1

    # Return the new customer-id with the "CUS" prefix
    # pad the number with leading zeros to make it 6 digits long
    return f"CUS{number:06d}"

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


def search_receipts_by_customer(receipts, customer_id):

    if not receipts:
        return []

    customer_id = customer_id.strip().upper()

    customer_receipts = []

    for receipt in receipts:
        if receipt["customer_id"].strip().upper() == customer_id:
            customer_receipts.append(receipt)

    return customer_receipts

def search_customer(customers, customer_id):
    customer_id = customer_id.strip().upper()

    for customer in customers:
        if customer["customer_id"].strip().upper() == customer_id:
            return customer

    return None


def customer_purchase_history(customers, receipts, customer_id):
    customer= search_customer(customers, customer_id)
    if not customer:
        return None
    
    customer_receipts = search_receipts_by_customer(receipts, customer_id )
    if not customer_receipts:
        return {
            "customer": customer,
            "receipts": customer_receipts
        }

    return {
        "customer": customer,
        "receipts": customer_receipts
    }

def print_customer_purchase_history(history):
    if history is None:
        print("Customer not found.")
        return

    customer = history["customer"]
    receipts = history["receipts"]

    print("\n========== CUSTOMER PROFILE ==========")
    print(f"Customer ID: {customer['customer_id']}")
    print(f"Name:        {customer['name']}")
    print(f"Phone:       {customer['phone']}")

    print("\n========== PURCHASE HISTORY ==========")

    if not receipts:
        print("No purchases found.")
        return

    for receipt in receipts:
        print(f"\nReceipt No: {receipt['receipt_number']}")
        print(f"Store:      {receipt['store']}")
        print(f"Total:      ₦{receipt['grand_total']:,.2f}")

    total_spent = customer_total_spent(receipts)

    print("\n========== CUSTOMER ANALYTICS ==========")
    print(f"Total Receipts:     {len(receipts)}")
    print(f"Total Spent:        ₦{total_spent:,.2f}")
    average_purchase = customer_average_purchase(receipts)
    print(f"Average Purchase:   ₦{average_purchase:,.2f}\n")

    largest_purchase = customer_largest_purchase(receipts)
    print_a_receipt(largest_purchase, title="Largest Purchase:")

    lowest_purchase = customer_lowest_purchase(receipts)
    print_a_receipt(lowest_purchase, title="Lowest Purchase:")


# ---------------Customer Analytics--------------
def customer_total_spent(customer_receipts):
    if not customer_receipts:
        return 0
    
    total = 0

    for receipt in customer_receipts:
        total += receipt.get("grand_total", 0)

    return total

def customer_average_purchase(customer_receipts):
    if not customer_receipts:
        return 0

    total = customer_total_spent(customer_receipts)

    return total / len(customer_receipts)

def customer_largest_purchase(customer_receipts):

    if not customer_receipts:
        return None

    return max(customer_receipts, key=lambda receipt: receipt.get("grand_total", 0))

def customer_lowest_purchase(customer_receipts):

    if not customer_receipts:
        return None

    return min(customer_receipts, key=lambda receipt: receipt.get("grand_total", 0))

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

result = search_receipts_by_customer(receipts, "CUS000001")

customer = search_customer(customers, "CUS000001")

history = customer_purchase_history(customers, receipts, "CUS000001")

print_customer_purchase_history(history)