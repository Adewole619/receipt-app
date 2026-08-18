import sys

from utils.customer_utils import (
    create_customer,
    search_customer_by_customer_id,
    customer_purchase_history,
    print_customer_purchase_history,
    load_customers_json,
    update_customer,
    delete_customer,
    search_customers,
    print_customer,
    print_customers_list,
    choose_customer,
    find_customer_for_action,
    filter_customers_by_spending,
    filter_customers_by_purchase_count,
    customers_with_no_purchases,
    sort_customers_by_spending,
    print_customer_spending_list,
    customer_spending_report,
)

from utils.receipt_utils import load_receipts_json
from utils.validation import get_menu_choice, validate_num_input


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

    # customer_id = input("Enter Customer ID: ").strip().upper()
    customer = find_customer_for_action(customers)

    history = customer_purchase_history(
        customers,
        receipts,
        customer['customer_id']
    )

    print_customer_purchase_history(history)

def customer_sort_menu():

    customers = load_customers_json()
    receipts = load_receipts_json()

    if not customers:
        print("No customers have been saved yet.")
        return

    while True:

        print("""
========== CUSTOMER SORTING ==========

1. Highest spending
2. Lowest spending
3. Back
""")

        choice = get_menu_choice("Choose an option: ")

        if choice == "1":

            results = sort_customers_by_spending(
                customers,
                receipts,
                descending=True
            )

            print_customer_spending_list(results)

        elif choice == "2":

            results = sort_customers_by_spending(
                customers,
                receipts,
                descending=False
            )

            print_customer_spending_list(results)

        elif choice == "3":
            break

        else:
            print("Invalid option.")


def customer_menu():

    while True:

        print("""
========== CUSTOMER MENU ==========

1. Create Customer
2. Search Customers
3. Customer Purchase History
4. Update customer
5. Delete Customer
6. Customer Filter
7. Customer Sorting
8. Customer Report
9. Back
""")

        choice = get_menu_choice("Choose an option: ")

        if choice == "1":
            create_customer_menu()

        elif choice == "2":
            # customers = load_customers_json()

            # customer_id = input(
            #     "Enter Customer ID: "
            # ).strip().upper()

            # customer = search_customer_by_customer_id(
            #     customers,
            #     customer_id
            # )
            search_customer_menu()

            # if customer is None:
            #     print("Customer not found.")
            # else:
            #     print("\n========== CUSTOMER ==========")
            #     print(f"Customer ID: {customer['customer_id']}")
            #     print(f"Name:        {customer['name']}")
            #     print(f"Phone:       {customer['phone']}")

        elif choice == "3":
            customer_purchase_history_menu()

        elif choice == "4":
            update_customer_menu()

        elif choice == "5":
            delete_customer_menu()

        elif choice == "6":
            customer_filter_menu()

        elif choice == "7":
            customer_sort_menu()

        elif choice == "8":
            customer_spending_report()

        elif choice == "9":
            print("Returning to main menu...")
            break

        else:
            print("Invalid option. Try again.")

def update_customer_menu():

    print("\n========== UPDATE CUSTOMER ==========")

    customers = load_customers_json()

    if not customers:
        print("No customer have been saved yet.")
        return

    # customer_id = get_menu_choice("Enter customer ID: ").strip().upper()
    customer = find_customer_for_action(customers)

    updated_customer = update_customer(customers, customer['costomer_id'])
    if updated_customer is None:
        return

    print("\n========== UPDATED CUSTOMER ==========")
    print(f"Customer ID: {updated_customer['customer_id']}")
    print(f"Name:        {updated_customer['name']}")
    print(f"Phone:       {updated_customer['phone']}")

def delete_customer_menu():

    customers = load_customers_json()
    receipts = load_receipts_json()

    if not customers:
        print("No customers have been saved yet.")
        return
    # customer_id = get_menu_choice("Enter customer ID: ").strip().upper()
    customer = find_customer_for_action(customers)

    deleted = delete_customer(customers, receipts, customer['customer_id'])

    if not deleted:
        print("Customer was not deleted.")

def search_customer_menu():

    customers = load_customers_json()

    if not customers:
        print("No customers have been saved yet.")
        return
    search_term = get_menu_choice("search by customer ID, name, or phone: ")

    results = search_customers(customers, search_term)

    if not results:
        print("No customers found.")
        return

    print(f"\nFound {len(results)} customer(s).")

    print_customers_list(results)

    if len(results) == 1:
        return results[0]

    return choose_customer(results)

def customer_filter_menu():

    customers = load_customers_json()
    receipts = load_receipts_json()

    if not customers:
        print("No customers have been saved yet.")
        return

    while True:

        print("""
========== CUSTOMER FILTER ==========

1. Customers by minimum spending
2. Customers by minimum purchases
3. Customers with no purchases
4. Back
""")

        choice = get_menu_choice("Choose an option: ")

        if choice == "1":

            minimum = validate_num_input(
                "Minimum spending",
                float
            )

            results = filter_customers_by_spending(
                customers,
                receipts,
                minimum
            )

            print_customers_list(results)

        elif choice == "2":

            minimum = validate_num_input(
                "Minimum number of purchases",
                int
            )

            results = filter_customers_by_purchase_count(
                customers,
                receipts,
                minimum
            )

            print_customers_list(results)

        elif choice == "3":

            results = customers_with_no_purchases(
                customers,
                receipts
            )

            print_customers_list(results)

        elif choice == "4":
            break

        else:
            print("Invalid option.")

def customer_report_menu():

    customers = load_customers_json()
    receipts = load_receipts_json()

    if not customers:
        print("No customers have been saved yet.")
        return

    print("\n========== CUSTOMER REPORT ==========")

    search_term = input(
        "Search term (press Enter for all customers): "
    ).strip()

    minimum_spending = validate_num_input(
        "Minimum spending",
        float
    )

    results = customer_spending_report(
        customers,
        receipts,
        search_term=search_term if search_term else None,
        minimum_spending=minimum_spending
    )

    if not results:
        print("\nNo customers matched your criteria.")
        return

    print_customer_spending_list(results)