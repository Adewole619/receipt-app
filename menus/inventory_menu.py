from utils.validation import get_menu_choice
from utils.inventory_utils import (
    load_inventory_history,
    print_inventory_history,
    search_inventory_history_by_product,
    search_inventory_history_by_type,
    validate_inventory_history,
    inventory_movement_report,
    product_movement_report,
)


def inventory_history_menu():

    while True:

        print("""
========== INVENTORY HISTORY ==========

1. View All History
2. Search by Product
3. Search by Movement Type
4. Validate History
5. Movement Report
6. Product Movement Report
7. Back
""")

        choice = get_menu_choice("Choose an option: ")

        history = load_inventory_history()

        if choice == "1":

            print_inventory_history(history)

        elif choice == "2":

            product_id = get_menu_choice(
                "Enter Product ID: "
            )

            movements = search_inventory_history_by_product(
                history,
                product_id
            )

            if not movements:
                print("No inventory history found.")
            else:
                print_inventory_history(movements)

        elif choice == "3":

            movement_type = get_menu_choice(
                "Enter movement type "
                "(RESTOCK / SALE / CORRECTION): "
            )

            movements = search_inventory_history_by_type(
                history,
                movement_type
            )

            if not movements:
                print("No inventory history found.")
            else:
                print_inventory_history(movements)
        elif choice == "4":

            validate_inventory_history(history)

        elif choice == "5":

            inventory_movement_report(history)
        elif choice == "6":

            product_id = get_menu_choice(
                "Enter Product ID: "
            )

            product_movement_report(
                history,
                product_id
            )
        elif choice == "7":

            break

        else:

            print("Invalid option.")