from utils.storage import load_receipts_json
import sys
import json

RECEIPT_FILE = "data/receipts.txt"
RECEIPT_FILE_JSON = "data/receipts.json"

receipts = load_receipts_json()



def total_receipts(receipts):
    total = len(receipts)
    return total


def total_sales(receipts):
    total_sales = 0
    for receipt in receipts:
        total_sales += receipt.get("grand_total", 0)

    return total_sales

def average_receipt(receipts):
    if not receipts:
        return 0
    average = total_sales(receipts) / total_receipts(receipts)
    return average

def smallest_receipt(receipts):
    # return min(receipt["grand_total"] for receipt in receipts)
    if not receipts:
        return None
    smallest = receipts[0]

    for receipt in receipts:
        if receipt["grand_total"] < smallest["grand_total"]:
            smallest = receipt

    return smallest

def largest_receipt(receipts):
    # return max(receipt["grand_total"] for receipt in receipts)
    if not receipts:
        return None
    
    largest = receipts[0]

    for receipt in receipts:
        if receipt["grand_total"] > largest["grand_total"]:
            largest = receipt

    return largest

def print_a_receipt(receipt, title="Receipt"):
    print(f"{title}\n")
    print(f"Store:\n{receipt['store']}\n")
    print(f"Receipt:\n{receipt['receipt_number']}\n")
    print(f"Grand Total:\n₦{receipt['grand_total']:,.2f}")

def receipts_per_store(receipts):
    store_counts = {}

    for receipt in receipts:
        store = receipt["store"]

        # if store in store_count:
        #     store_counts[store] +=1
        # else:
        #     store_counts[store] = 1
        store_counts[store]= store_counts.get(store, 0) + 1

    return store_counts

def print_store_count(store_counts):
    for store, count in store_counts.items():
        label = "receipt" if count == 1 else "receipts"
        print(f"{store}: {count} {label}")

    # counts = receipts_per_store(receipts)
    # for store, count in counts.items():
    #     print(f"{store}: {count} receipt{'s' if count != 1 else ''}")

def statistics_menu(receipts):
    while True:
        print("""
====== Statistics ======

1. Total Receipts

2. Total Sales

3. Average Receipt

4. Largest Receipt

5. Smallest Receipt

6. Receipts Per Store

7. Back
""")

        choice = input("Choose an option: ")

        if choice == "1":
            print(total_receipts(receipts))

        elif choice == "2":
            print(total_sales(receipts))

        elif choice == "3":
            print(average_receipt(receipts))

        elif choice == "4":
            largest = largest_receipt(receipts)
            print_a_receipt(largest, "Largest Receipt")

        elif choice == "5":
            smallest = smallest_receipt(receipts)
            print_a_receipt(smallest, "Smallest Receipt")

        elif choice == "6":
            stores = receipts_per_store(receipts)

            print_store_count(stores)

        elif choice == "7":
            break

        else:
            print("Invalid option. Try again.")

statistics_menu(receipts)