import sys

from utils.customer_utils import (
    create_customer,
    search_customer,
    customer_purchase_history,
    print_customer_purchase_history,
    load_customers_json
)

from utils.receipt_utils import load_receipts_json
from utils.validation import get_menu_choice


def create_customer_menu():
    print("\n========== CREATE CUSTOMER ==========")

    customer = create_customer()

    print("\nCustomer successfully created!")
    print(f"Customer ID: {customer['customer_id']}")
    print(f"Name:        {customer['name']}")
    print(f"Phone:       {customer['phone']}")


def customer_purchase_history_menu():
    print("\n========== CUSTOMER PURCHASE HISTORY ==========")

    customers = load_customers_json()
    receipts = load_receipts_json()

    if not customers:
        print("No customers have been saved.")
        return

    customer_id = input("Enter Customer ID: ").strip().upper()

    history = customer_purchase_history(
        customers,
        receipts,
        customer_id
    )

    print_customer_purchase_history(history)


def customer_menu():
    while True:

        print("""
========== CUSTOMER MENU ==========

1. Create Customer
2. Search Customer
3. Customer Purchase History
4. Back
""")

        choice = get_menu_choice("Choose an option: ")

        if choice == "1":
            create_customer_menu()

        elif choice == "2":
            customers = load_customers_json()

            customer_id = input(
                "Enter Customer ID: "
            ).strip().upper()

            customer = search_customer(
                customers,
                customer_id
            )

            if customer is None:
                print("Customer not found.")
            else:
                print("\n========== CUSTOMER ==========")
                print(f"Customer ID: {customer['customer_id']}")
                print(f"Name:        {customer['name']}")
                print(f"Phone:       {customer['phone']}")

        elif choice == "3":
            customer_purchase_history_menu()

        elif choice == "4":
            print("Returning to main menu...")
            break

        else:
            print("Invalid option. Try again.")