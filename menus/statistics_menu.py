from utils.receipt_utils import load_receipts_json
from utils.analytics import (
    total_receipts,
    total_sales,
    average_receipt,
    largest_receipt,
    smallest_receipt,
    receipts_per_store,
    sales_per_store,
    highest_spending_store,
    lowest_spending_store,
    average_sales_per_store,
    print_a_receipt,
    print_store_count,
    print_store_sales
)

from utils.validation import get_menu_choice
receipts = load_receipts_json()

def statistics_menu(receipts):

    while True:

        print("""
========== STATISTICS ==========

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

        choice = get_menu_choice("Choose an option: ")

        if choice == "1":

            total = total_receipts(receipts)

            print(f"\nTotal Receipts: {total}")

        elif choice == "2":

            total = total_sales(receipts)

            print(f"\nTotal Sales: ₦{total:,.2f}")

        elif choice == "3":

            if not receipts:
                print("\nNo receipts available.")
                continue

            average = average_receipt(receipts)

            print(f"\nAverage Receipt: ₦{average:,.2f}")

        elif choice == "4":

            largest = largest_receipt(receipts)

            if largest is None:
                print("\nNo receipts available.")
            else:
                print_a_receipt(
                    largest,
                    title="Largest Receipt"
                )

        elif choice == "5":

            smallest = smallest_receipt(receipts)

            if smallest is None:
                print("\nNo receipts available.")
            else:
                print_a_receipt(
                    smallest,
                    title="Smallest Receipt"
                )

        elif choice == "6":

            store_counts = receipts_per_store(receipts)

            if not store_counts:
                print("\nNo receipts available.")
            else:
                print_store_count(store_counts)

        elif choice == "7":

            store_sales = sales_per_store(receipts)

            if not store_sales:
                print("\nNo receipts available.")
            else:
                print_store_sales(
                    store_sales,
                    title="Sales Per Store"
                )

        elif choice == "8":

            highest = highest_spending_store(receipts)

            if highest is None:
                print("\nNo receipts available.")
            else:
                print_store_sales(
                    highest,
                    title="Highest Spending Store"
                )

        elif choice == "9":

            lowest = lowest_spending_store(receipts)

            if lowest is None:
                print("\nNo receipts available.")
            else:
                print_store_sales(
                    lowest,
                    title="Lowest Spending Store"
                )

        elif choice == "10":

            average_sales = average_sales_per_store(receipts)

            if not average_sales:
                print("\nNo receipts available.")
            else:
                print_store_sales(
                    average_sales,
                    title="Average Sales Per Store"
                )

        elif choice == "11":

            print("Returning to main menu...")
            break

        else:

            print("Invalid option. Try again.")