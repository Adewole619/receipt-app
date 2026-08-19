from utils.validation import get_menu_choice
from utils.receipt_utils import (
    create_receipt,
    load_receipts_json,
    get_receipt_number,
    delete_receipt,
    search_by_store,
    print_receipt_out,
    save_all_receipts,
    search_by_receipt_number,
    search_walk_in_receipts
    )

import sys


def print_receipt_list(receipts):

    """
    Display a list of receipts with a short
    selection number for each receipt.
    """
      
    for i, receipt in enumerate(receipts, start = 1):
                print(f"Selection [{i}]")
                print_receipt_out(receipt)

def choose_receipt(receipts):

    """
    Ask the user to select a receipt from a list.

    Returns:
        receipt dictionary if selected
        None if cancelled or invalid
    """

    
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

def search_by_receipt_menu(receipts):
    rcp_number = get_receipt_number()
            
    receipt = search_by_receipt_number(receipts, rcp_number)
    
    if receipt is None:
        print("Receipt not found or no receipts have been saved.")
    else:
        print_receipt_out(receipt)

def search_by_store_menu(receipts):

    """
    Search for all receipts belonging to a store.
    """

    store_name =  get_menu_choice("Enter store name: ")

    store_receipts = search_by_store(receipts, store_name)

    if not store_receipts:
        print("No receipts found.")
    else:
        for store_receipt in store_receipts :
            print_receipt_out(store_receipt)

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

def delete_menu(receipts):

    """
    Search for one receipt using its receipt number.
    """

    print("========== DELETE RECEIPT ==========")
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

    elif delete_type == "3":

        print("Deletion cancelled.")

    else:
        print("Invalid option.")

def delete_receipt_menu(receipts):

    """
    Delete a receipt using its receipt number.
    """

    receipt_number = get_receipt_number()
               
    deleted = delete_receipt(receipts, receipt_number)
    if not deleted:
        print("Deletion cancelled.")

def receipts_menu():

    """
    Main receipt search and deletion menu.
    """

    while True:
        # MAIN MENU 
        print("""
            ========== RECEIPT MANAGEMENT ==========

            1. Create Receipt
            2. Search by Receipt Number
            3. Search by Store
            4. Search Walk-in Receipts
            5. Delete a Receipt
            6. Back
            """)
            
        choice = get_menu_choice("Choose an option: ")
        
        receipts = load_receipts_json()
        if choice == "1":
            create_receipt_menu()

        elif choice == "2":
            search_by_receipt_menu(receipts)

        elif choice == "3":
            search_by_store_menu(receipts)

        elif choice == "4":
            search_walk_in_menu(receipts)
            
        elif choice == "5":
            delete_menu(receipts)

        elif choice == "6":
            break
        else:
            print("Invalid option. Try again")

def create_receipt_menu():

    receipt = create_receipt()

    if receipt is None:
        print("\nReceipt creation failed or cancelled.")
        return

    print("\nReceipt successfully created!")
    print_receipt_out(receipt)

def search_walk_in_menu(receipts):

    walk_in_receipts = search_walk_in_receipts(receipts)

    if not walk_in_receipts:
        print("No walk-in receipts found.")
        return

    print("\n========== WALK-IN RECEIPTS ==========")

    print_receipt_list(walk_in_receipts)


#----------------------END---------------------------------------









