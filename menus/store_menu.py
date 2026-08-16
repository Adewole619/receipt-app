from utils.store_utils import (
    create_store,
    search_store_by_id,
    search_stores,
    print_store,
    print_store_list,
    update_store,
    delete_store,
    load_stores_json
)

from utils.receipt_utils import load_receipts_json

def store_menu():

    while True:

        print("\n========== STORE MENU ==========")

        print("1. Create Store")
        print("2. Search Store")
        print("3. List Stores")
        print("4. Update Store")
        print("5. Delete Store")
        print("6. Back")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            create_store_menu()

        elif choice == "2":
            search_store_menu()

        elif choice == "3":
            list_stores_menu()

        elif choice == "4":
            update_store_menu()

        elif choice == "5":
            delete_store_menu()

        elif choice == "6":
            print("Returning to main menu...")
            break

        else:
            print("Invalid option.")

def create_store_menu():

    store = create_store()

    if store:
        print("\nCreated store:")
        print_store(store)

def search_store_menu():

    stores = load_stores_json()

    print("\n========== SEARCH STORE ==========")

    print("1. Search by Store ID")
    print("2. Search by Name or Address")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":

        store_id = input(
            "Enter Store ID: "
        ).strip()

        store = search_store_by_id(
            stores,
            store_id
        )

        print_store(store)

    elif choice == "2":

        search_term = input(
            "Enter search term: "
        ).strip()

        results = search_stores(
            stores,
            search_term
        )

        print_store_list(results)

    else:
        print("Invalid option.")

def list_stores_menu():

    stores = load_stores_json()

    print_store_list(stores)

def update_store_menu():

    stores = load_stores_json()

    store_id = input(
        "Enter Store ID to update: "
    ).strip()

    updated_store = update_store(
        stores,
        store_id
    )

    if updated_store:
        print("\nUpdated store:")
        print_store(updated_store)

def delete_store_menu():

    stores = load_stores_json()
    receipts = load_receipts_json()

    store_id = input(
        "Enter Store ID to delete: "
    ).strip()

    delete_store(
        stores,
        receipts,
        store_id
    )