



#--------------------CUSTOMER STORAGE METHODS-------------------
def save_customers_json(customer):
    try:
        with open(CUSTOMER_FILE_JSON, "r") as file:
            customers = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        customers = []

    customers.append(customer)

    with open(CUSTOMER_FILE_JSON, "w") as file:
        json.dump(customers, file, indent = 4)


def load_customers_json():
    try:
        with open(CUSTOMER_FILE_JSON, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No customers have been saved yet.")
        return []

#--------------------------CUSTOMER ID METHODS-----------------------------------------

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

#------------------------CUSTOMER CREATION METHODS ---------------------------------

def create_customer():
    customers = load_customers_json()

    customer_name = validate_string_input("Customer name")
    customer_phone = validate_string_input("Phone number")

    existing_customer = search_customer_by_phone(customers,customer_phone)
    if existing_customer:
        print("Customer already existed.")
        return existing_customer
    
    customer_id = generate_customer_id()

    customer_details = {
        "customer_id" : customer_id,
        "name": customer_name,
        "phone": customer_phone
    }

    save_customers_json(customer_details)

    return customer_details

#------------------------ CUSTOMER SEARCHING METHODS --------------------

def search_customer_by_customer_id(customers, customer_id):
    customer_id = customer_id.strip().upper()

    for customer in customers:
        if customer["customer_id"].strip().upper() == customer_id:
            return customer

    return None

def search_customer_by_phone(customers, phone):
    phone = phone.strip()

    for customer in customers:
        if customer["phone"].strip() == phone:
            return customer

    return None

# -----------------------------CUSTOMER / RECEIPT RELATIONSHIP METHODS ----------------------

def search_receipts_by_customer(receipts, customer_id):

    if not receipts:
        return []

    customer_id = customer_id.strip().upper()

    customer_receipts = []

    for receipt in receipts:
        if receipt["customer_id"].strip().upper() == customer_id:
            customer_receipts.append(receipt)

    return customer_receipts


def customer_purchase_history(customers, receipts, customer_id):
    customer= search_customer_by_customer_id(customers, customer_id)
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

def get_customer_for_receipt():
    customers = load_customers_json()

    while True:
        choice = get_menu_choice("Display:\n1. Existing customer\n2. New customer\nChoice: ")

        if choice == "1":
            phone_number = get_menu_choice("Enter phone number: ")

            customer = search_customer_by_phone(customers, phone_number)

            if customer:
                print("Customer found:")
                return customer

            print("Customer not found.")
            continue

        elif choice == "2":
            return create_customer()
        
        else:
            print("Invalid option. Try again.")


#--------------------------CUSTOMER ANALYTICS METHODS-------------------------

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


#-------------------CUSTOMER DISPLAY METHODS-------------------------------

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

#--------------------END----------------------------------------

