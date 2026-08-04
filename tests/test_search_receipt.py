from utils.receipt_utils import (
    search_by_receipt_number,
    search_by_store , 
    print_receipt_out,
)

print("===== TEST: Search by Receipt Number =====")
receipt = search_by_receipt_number("RCP0000001")

if receipt:
    print("✅ Receipt Found\n")
    print_receipt_out(receipt)
else:
    print("❌ Receipt Not Found")

print("===== TEST: Receipt Does Not Exist =====")
receipt = search_by_receipt_number("RCP9999999")

if receipt:
    print("Test Failed")
else:
    print("✅ Correct")
    print("Receipt was not found.")

print("===== TEST: Search by Store =====")
receipts = search_by_store("Shoprite")

if receipts:
    print(f"Found {len(receipts)} receipt(s).\n")

    for receipt in receipts:
        print_receipt_out(receipt)
else:
    print("No receipts found.")

print("===== TEST: Store Does Not Exist =====")
receipts = search_by_store("Amazon")

if receipts:
    print("Test Failed")
else:
    print("✅ Correct")
    print("No receipts found.")

print("===== TEST: Case Insensitive Search =====")
tests = [
    "shoprite",
    "SHOPRITE",
    "Shoprite",
    "sHoPrItE",
]

for store in tests:
    receipts = search_by_store(store)

    print(f"{store} -> {len(receipts)} receipt(s)")