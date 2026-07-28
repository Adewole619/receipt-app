from utils.receipt_utils import calculate_subtotal, validate_input, validate_string_input, validate_num_input, save_receipt, load_receipts

store_name = validate_string_input("Store name")

receipt_number = validate_string_input("Receipt number")

receipt_items = []

count = validate_num_input("Number of items", int)

grand_total = 0

for i in range(count):
    item_name = validate_string_input("Item name")
    
    item_price = validate_num_input("Item price", float)

    item_quantity = validate_num_input("Item quantity", int)

    sub_total = calculate_subtotal(item_price, item_quantity)

    item = {
         "name": item_name,
        "price": item_price,
        "quantity": item_quantity,
        "subtotal": sub_total,
    }
    receipt_items.append(item)

    grand_total += sub_total 


save_receipt(store_name, receipt_number, receipt_items, grand_total)

content = load_receipts()
print(content)