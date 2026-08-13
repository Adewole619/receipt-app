import sys
import json
import os

RECEIPT_FILE = "data/receipts.txt"
RECEIPT_FILE_JSON = "data/receipts.json"







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