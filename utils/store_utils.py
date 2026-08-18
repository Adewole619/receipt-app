import os
import json

from utils.validation import validate_string_input, validate_optional_string

STORE_FILE_JSON = "data/stores.json"

def generate_store_id():    

    if not os.path.exists(STORE_FILE_JSON):
        return "STO000001"

    try:
        with open(STORE_FILE_JSON, "r") as file:
            stores = json.load(file)

    except json.JSONDecodeError:
        return "STO000001"

    if not stores:
        return "STO000001"

    last_store = stores[-1]

    last_store_id = last_store["store_id"]

    number = int(
        last_store_id.replace("STO", "")
    )

    number += 1

    return f"STO{number:06d}"

def save_stores_json(store):

    try:
        with open(STORE_FILE_JSON, "r") as file:
            stores = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        stores = []

    stores.append(store)

    with open(STORE_FILE_JSON, "w") as file:
        json.dump(
            stores,
            file,
            indent=4
        )

def load_stores_json():

    try:
        with open(STORE_FILE_JSON, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("No stores have been saved yet.")
        return []

def search_store_by_name(stores, store_name):

    if not stores:
        return None

    store_name = store_name.strip().lower()

    for store in stores:
        if store["store_name"].strip().lower() == store_name:
            return store

    return None

def store_name_exists(stores, store_name):

    return search_store_by_name(
        stores,
        store_name
    ) is not None

def create_store():

    stores = load_stores_json()

    store_name = validate_string_input("Store name")
    address = validate_string_input("Store address")
    phone = validate_string_input("Store phone")
    manager = validate_string_input("Store manager")

    if store_name_exists(stores, store_name):
        print(
            f"\nStore '{store_name}' already exists."
        )
        return None

    store_id = generate_store_id()

    store = {
        "store_id": store_id,
        "store_name": store_name,
        "address": address,
        "phone": phone,
        "manager": manager
    }

    save_stores_json(store)

    print("\nStore successfully created.")

    return store

def search_store_by_id(stores, store_id):

    if not stores:
        return None

    store_id = store_id.strip().upper()

    for store in stores:
        if store["store_id"].strip().upper() == store_id:
            return store

    return None

def search_stores(stores, search_term):

    if not stores:
        return []

    search_term = search_term.strip().lower()

    matches = []

    for store in stores:

        store_id = store["store_id"].lower()
        store_name = store["store_name"].lower()
        address = store["address"].lower()

        if (
            search_term in store_id
            or search_term in store_name
            or search_term in address
        ):
            matches.append(store)

    return matches

def print_store(store):

    if store is None:
        print("Store not found.")
        return

    print("\n========== STORE ==========")
    print(f"Store ID:  {store['store_id']}")
    print(f"Name:      {store['store_name']}")
    print(f"Address:   {store['address']}")
    print(f"Phone:     {store['phone']}")
    print(f"Manager:   {store['manager']}")


def print_store_list(stores):

    if not stores:
        print("No stores found.")
        return

    print("\n========== STORES ==========")

    for i, store in enumerate(stores, start=1):

        print(f"\n[{i}]")
        print(f"Store ID:  {store['store_id']}")
        print(f"Name:      {store['store_name']}")
        print(f"Address:   {store['address']}")
        print(f"Phone:     {store['phone']}")
        print(f"Manager:   {store['manager']}")

def update_store(stores, store_id):

    store = search_store_by_id(stores, store_id)

    if store is None:
        print("Store not found.")
        return None

    print("\n========== UPDATE STORE ==========")

    print(f"Current name:    {store['store_name']}")
    print(f"Current address: {store['address']}")
    print(f"Current phone:   {store['phone']}")
    print(f"Current manager: {store['manager']}")

    new_name = validate_optional_string("New store name")
    new_address = validate_optional_string("New address")
    new_phone = validate_optional_string("New phone")
    new_manager = validate_optional_string("New manager")

    if new_name:

        existing_store = search_store_by_name(
            stores,
            new_name
        )

        if (
            existing_store is not None
            and existing_store["store_id"] != store["store_id"]
        ):
            print(
                f"\nStore name '{new_name}' "
                "already belongs to another store."
            )
            return None

        store["store_name"] = new_name

    if new_address:
        store["address"] = new_address

    if new_phone:
        store["phone"] = new_phone

    if new_manager:
        store["manager"] = new_manager

    save_all_stores(stores)

    print("\nStore successfully updated.")

    return store

def save_all_stores(stores):

    with open(STORE_FILE_JSON, "w") as file:
        json.dump(
            stores,
            file,
            indent=4
        )

def delete_store(stores, receipts, store_id):

    store = search_store_by_id(stores, store_id)

    if store is None:
        print("Store not found.")
        return False

    # Check whether the store has receipts
    store_receipts = []

    for receipt in receipts:
        if (
            receipt.get("store", "").strip().lower()
            == store["store_name"].strip().lower()
        ):
            store_receipts.append(receipt)

    if store_receipts:
        print(
            f"\nCannot delete store "
            f"{store['store_name']}."
        )

        print(
            "This store has receipts attached to it."
        )

        print(
            "Delete or move the store's receipts "
            "before deleting the store."
        )

        return False

    print_store(store)

    confirm = input(
        "\nPermanently delete this store?\n"
        "Type Yes to delete or No to cancel: "
    ).strip().lower()

    if confirm == "no":
        print("Deletion cancelled.")
        return False

    elif confirm == "yes":

        stores.remove(store)

        save_all_stores(stores)

        print("Store deleted successfully.")

        return True

    else:
        print(
            "Invalid option.\n"
            "Deletion cancelled."
        )

        return False