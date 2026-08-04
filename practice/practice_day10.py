from utils.receipt_utils import load_receipts_json , print_receipt_out 
import sys

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


print("====== Receipt Search ======")
print("1. Search by Receipt Number\n2. Search by Store\n3. Exit")
while True:
    
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a number.")
        continue
    
    if choice == 3:
        sys.exit()
    elif choice == 1:

        rcp_number = input("Receipt Number: ")
        
        receipt = search_by_receipt_number(rcp_number)

        if receipt is None:
            print("Receipt not found or no receipts have been saved.")
        else:
            print_receipt_out(receipt)

    elif choice == 2:

        st_name =  input("Enter store name: ")

        st_receipts = search_by_store(st_name)

        if not st_receipts:
            print("No receipts found.")
        else:
            for st_receipt in st_receipts :
                print_receipt_out(st_receipt)

    else:

        print("Invalid option")
        continue

