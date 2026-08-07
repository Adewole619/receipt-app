import sys
import json
import os

RECEIPT_FILE = "data/receipts.txt"
RECEIPT_FILE_JSON = "data/receipts.json"


def main_menu():
    while True:
        # MAIN MENU 
        print("====== Receipt Search and Receipt Deletion Menu ======")
        print("1. Search by Receipt Number\n2. Search by Store\n3. Delete a Receipt\n4. Exit")  
            
        choice = get_menu_choice("Choose an option: ")
        receipts = load_receipts_json()
        if choice == "1":
            search_by_receipt_menu(receipts)

        elif choice == "2":
            search_by_store_menu(receipts)

        elif choice == "3":
            delete_menu(receipts)

        elif choice == "4":
            print("receipt Search terminated")
            sys.exit()
        else:
            print("Invalid option")


def delete_menu(receipts):
    print("Searching for receipt")
    print("1. Search by Store")
    print("2. Search by Receipt Number")

    delete_type = get_menu_choice("Choose: ")

    if delete_type == "1":

        st_name = get_menu_choice("Enter store name: ")
        st_receipts = search_by_store(receipts, st_name)
        if not st_receipts:
            print("No receipts found.")
        else:
            print_receipt_list(st_receipts)
            receipt = choose_receipt(st_receipts)
            deleted = delete_receipt_object(receipts, receipt)
            if not deleted:
                print("Deletion canceled.")      

    elif delete_type == "2":
        delete_receipt_menu(receipts)

    else:
        print("Invalid option.")


def search_by_receipt_menu(receipts):
    rcp_number = get_receipt_number()
            
    receipt = search_by_receipt_number(receipts, rcp_number)
    
    if receipt is None:
        print("Receipt not found or no receipts have been saved.")
    else:
        print_receipt_out(receipt)

def search_by_store_menu(receipts):
    st_name =  get_menu_choice("Enter store name: ")

    st_receipts = search_by_store(receipts, st_name)

    if not st_receipts:
        print("No receipts found.")
    else:
        for st_receipt in st_receipts :
            print_receipt_out(st_receipt)


def delete_receipt_menu(receipts):
    receipt_number = get_receipt_number()
               
    deleted = delete_receipt(receipts, receipt_number)
    if not deleted:
        print("Deletion cancelled.")

def get_menu_choice(prompt):
    return input(prompt).strip()