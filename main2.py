from utils.receipt_utils import load_receipts_json , print_receipt_out 
import sys

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

print("====== Receipt Search ======")
print("1. Search by Receipt Number\n2. Search by Store\n3. Exit")
while True:
    
    
    choice = input("Choose an option: ").strip()
    # except ValueError:
    #     print("Please enter a number.")
    #     continue
    receipts = load_receipts_json()
    if choice == "1":

        rcp_number = input("Receipt Number: ")
        
        receipt = search_by_receipt_number(receipts, rcp_number)

        if receipt is None:
            print("Receipt not found or no receipts have been saved.")
        else:
            print_receipt_out(receipt)

        break    

    elif choice == "2":

        st_name =  input("Enter store name: ")

        st_receipts = search_by_store(st_name)

        if not st_receipts:
            print("No receipts found.")
        else:
            for st_receipt in st_receipts :
                    print_receipt_out(st_receipt)

        break
    elif choice == "3":
            print("receipt Search terminated")
            sys.exit()
    else:

        print("Invalid option")
        break


def update_receipt(rcp_number):
    receipts = load_receipts_json()
    receipt = search_by_receipt_number(receipts, rcp_number)
    if receipt is None:
        print("Receipt not found.")
    else:
        new_rcp_store_name = input(f"Update Store name?\nCurren store name: {receipt['store']}\n New store name: ").strip()
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
            
        

def save_all_receipts(receipts):
    with open(RECEIPT_FILE_JSON, "w") as file:
        json.dump(receipts, file, indent=4)

1. the receipts number is the first object to search for first
2. from the search by receipt number, we get the receipt, then use receipt["items"]["name"]
access "Riceand change it to "beans" with our update_receipt function
3. we write the new updated list of dictionaries from memory to file, then save as json