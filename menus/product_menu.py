from utils.product_utils import (
    load_products_json,
    create_product,
    search_product_by_id,
    search_products,
    search_products_by_store,
    print_product,
    print_product_list,
    update_product,
    delete_product
)

from utils.store_utils import load_stores_json, search_store_by_id
from utils.receipt_utils import load_receipts_json

def product_menu():

    while True:

        print("\n========== PRODUCT MENU ==========")

        print("1. Create Product")
        print("2. Search Product")
        print("3. List Products")
        print("4. Update Product")
        print("5. Delete Product")
        print("6. Products by Store")
        print("7. Back")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            create_product_menu()

        elif choice == "2":
            search_product_menu()

        elif choice == "3":
            list_products_menu()

        elif choice == "4":
            update_product_menu()

        elif choice == "5":
            delete_product_menu()

        elif choice == "6":
            products_by_store_menu()

        elif choice == "7":
            print("Returning to main menu...")
            break

        else:
            print("Invalid option.")

def create_product_menu():

    stores = load_stores_json()

    product = create_product(stores)

    if product:
        print_product(product)

def search_product_menu():

    products = load_products_json()

    print("\n========== SEARCH PRODUCT ==========")

    print("1. Search by Product ID")
    print("2. Search by Name or Category")

    choice = input("\nChoose an option: ").strip()

    if choice == "1":

        product_id = input(
            "Enter Product ID: "
        ).strip()

        product = search_product_by_id(
            products,
            product_id
        )

        print_product(product)

    elif choice == "2":

        search_term = input(
            "Enter search term: "
        ).strip()

        results = search_products(
            products,
            search_term
        )

        print_product_list(results)

    else:

        print("Invalid option.")

def list_products_menu():

    products = load_products_json()

    print_product_list(products)

def update_product_menu():

    products = load_products_json()

    product_id = input(
        "Enter Product ID to update: "
    ).strip()

    updated_product = update_product(
        products,
        product_id
    )

    if updated_product:
        print_product(updated_product)

def delete_product_menu():

    products = load_products_json()
    receipts = load_receipts_json()

    product_id = input(
        "Enter Product ID to delete: "
    ).strip()

    delete_product(
        products,
        receipts,
        product_id
    )

def products_by_store_menu():

    products = load_products_json()
    stores = load_stores_json()

    print("\n========== PRODUCTS BY STORE ==========")

    store_id = input(
        "Enter Store ID: "
    ).strip()

    store = search_store_by_id(
        stores,
        store_id
    )

    if store is None:
        print("Store not found.")
        return

    store_products = search_products_by_store(
        products,
        store_id
    )

    print(
        f"\nProducts for {store['store_name']}:"
    )

    print_product_list(store_products)

