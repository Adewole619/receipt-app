from utils.storage import load_receipts_json
import sys
import json

RECEIPT_FILE = "data/receipts.txt"
RECEIPT_FILE_JSON = "data/receipts.json"

receipts = load_receipts_json()

















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

7. Sales Per Store

8. Highest Spending Store

9. Lowest Spending Store

10. Average Sales Per Store

11. Back
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
            sales = sales_per_store(receipts)
            print_store_sales(sales, "Sales Per Store")

        elif choice == "8":
            highest_sale = highest_spending_store(receipts)

            if highest_sale:
                print_store_sales(highest_sale, "Highest Spending Store")

        elif choice == "9":
            lowest_sale = lowest_spending_store(receipts)

            if lowest_sale:
                print_store_sales(lowest_sale, "Lowest Spending Store")

        elif choice == "10":
            average_sale = average_sales_per_store(receipts)

            if average_sale:
                print_store_sales(average_sale, "Average Sales Per Store")

        elif choice == "11":
            break

        else:
            print("Invalid option. Try again.")

statistics_menu(receipts)