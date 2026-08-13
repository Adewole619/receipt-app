
#-------------------------RECEIPT STATISTIC METHOD--------------

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
    return f"Average Sales for all stores ₦{average:,.2f}"


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

#-----------------------STORAGE STATISTICS METHODS--------------------------

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

def sales_per_store(receipts):
    store_sales = {}
    for receipt in receipts:
        store = receipt["store"]
        store_sales[store] = store_sales.get(store, 0) + receipt.get("grand_total", 0)

    return store_sales

def highest_spending_store(receipts):
    store_sales = sales_per_store(receipts)

    if not store_sales:
        return None
    
    highest_store = max(store_sales, key=store_sales.get)

    return {highest_store: store_sales[highest_store]}

def lowest_spending_store(receipts):
    store_sales = sales_per_store(receipts)

    if not store_sales:
        return None
    
    lowest_store = min(store_sales, key=store_sales.get)

    return {lowest_store: store_sales[lowest_store]}

def average_sales_per_store(receipts):

    store_sales = sales_per_store(receipts)

    if not store_sales:
        return None
    
    receipts_count = receipts_per_store(receipts)

    average_sales = {}

    for store in store_sales:
        average_sales[store] = store_sales[store] / receipts_count[store]

    return average_sales

# -----------------------------DISPLAY FUNCTIONS---------------------

def print_a_receipt(receipt, title="Receipt"):
    print(f"{title}\n")
    print(f"Store:\n{receipt['store']}\n")
    print(f"Receipt:\n{receipt['receipt_number']}\n")
    print(f"Grand Total:\n₦{receipt['grand_total']:,.2f}")



def print_store_count(store_counts):
    for store, count in store_counts.items():
        label = "receipt" if count == 1 else "receipts"
        print(f"{store}: {count} {label}")

    # counts = receipts_per_store(receipts)
    # for store, count in counts.items():
    #     print(f"{store}: {count} receipt{'s' if count != 1 else ''}")



def print_store_sales(store_sales, title="Store sales"):
    print(f"{title}\n")
    for store, sales in store_sales.items():
        print(f"{store}: ₦{sales:,.2f}")

#----------------------------------END-----------------------------------------------------------------