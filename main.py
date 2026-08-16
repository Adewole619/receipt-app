import sys

from menus.receipts_menu import receipts_menu
from menus.customer_menu import customer_menu
from menus.statistics_menu import statistics_menu
from menus.store_menu import store_menu

from utils.receipt_utils import load_receipts_json


def main_menu():

    while True:

        print("""
========================================
        RECEIPT MANAGEMENT SYSTEM
========================================

1. Receipt Management
2. Customer Management
3. Store Management
4. Business Statistics
5. Exit
""")

        choice = input("Choose an option: ").strip()

        if choice == "1":

            receipts_menu()

        elif choice == "2":

            customer_menu()

        elif choice == "3":

            store_menu()

        elif choice == "4":

            receipts = load_receipts_json()

            statistics_menu(receipts)

        elif choice == "5":

            print("Goodbye!")
            break

        else:

            print("Invalid option. Try again.")


if __name__ == "__main__":
    main_menu()