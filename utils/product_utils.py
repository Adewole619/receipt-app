import os
import json

from utils.store_utils import search_store_by_id
from utils.validation import (
    validate_string_input,
    validate_num_input,
    validate_optional_num,
    validate_optional_string,
)

PRODUCT_FILE_JSON = "data/products.json"

# product = {
#     "product_id": "PRD000001",
#     "store_id": "STO000001",
#     "name": "Coca-Cola 50cl",
#     "category": "Drinks",
#     "price": 500.0,
#     "stock_quantity": 50
# }

def generate_product_id():

    if not os.path.exists(PRODUCT_FILE_JSON):
        return "PRD000001"

    try:
        with open(PRODUCT_FILE_JSON, "r") as file:
            products = json.load(file)

    except json.JSONDecodeError:
        return "PRD000001"

    if not products:
        return "PRD000001"

    last_product = products[-1]

    last_product_id = last_product["product_id"]

    number = int(
        last_product_id.replace("PRD", "")
    )

    number += 1

    return f"PRD{number:06d}"

def load_products_json():

    try:
        with open(PRODUCT_FILE_JSON, "r") as file:
            return json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        print("No products have been saved yet.")
        return []


def save_product_json(product):

    try:
        with open(PRODUCT_FILE_JSON, "r") as file:
            products = json.load(file)

    except (FileNotFoundError, json.JSONDecodeError):
        products = []

    products.append(product)

    with open(PRODUCT_FILE_JSON, "w") as file:
        json.dump(
            products,
            file,
            indent=4
        )

def save_all_products(products):

    with open(PRODUCT_FILE_JSON, "w") as file:
        json.dump(
            products,
            file,
            indent=4
        )

def search_product_by_name(products, store_id, product_name):

    if not products:
        return None

    store_id = store_id.strip().upper()
    product_name = product_name.strip().lower()

    for product in products:

        if (
            product["store_id"].strip().upper() == store_id
            and
            product["name"].strip().lower() == product_name
        ):
            return product

    return None

def create_product(stores):

    products = load_products_json()

    print("\n========== CREATE PRODUCT ==========")

    store_id = input("Enter Store ID: ").strip().upper()

    store = search_store_by_id(stores, store_id)

    if store is None:
        print("Store not found.")
        return None

    print(f"Store: {store['store_name']}")

    product_name = validate_string_input("Product name")

    existing_product = search_product_by_name(
        products,
        store_id,
        product_name
    )

    if existing_product:
        print(
            f"\nProduct '{product_name}' "
            f"already exists in {store['store_name']}."
        )
        return existing_product

    category = validate_string_input("Product category")

    price = validate_num_input(
        "Product price",
        float
    )

    stock_quantity = validate_num_input(
        "Initial stock quantity",
        int
    )

    product_id = generate_product_id()

    product = {
        "product_id": product_id,
        "store_id": store_id,
        "name": product_name,
        "category": category,
        "price": price,
        "stock_quantity": stock_quantity
    }

    save_product_json(product)

    print("\nProduct successfully created.")

    return product

def search_product_by_id(products, product_id):

    if not products:
        return None

    product_id = product_id.strip().upper()

    for product in products:
        if product["product_id"].strip().upper() == product_id:
            return product

    return None

def search_products_by_store(products, store_id):

    if not products:
        return []

    store_id = store_id.strip().upper()

    matching_products = []

    for product in products:

        if product["store_id"].strip().upper() == store_id:
            matching_products.append(product)

    return matching_products

def search_products(products, search_term):

    if not products:
        return []

    search_term = search_term.strip().lower()

    matches = []

    for product in products:

        product_id = product["product_id"].lower()
        product_name = product["name"].lower()
        category = product["category"].lower()

        if (
            search_term in product_id
            or search_term in product_name
            or search_term in category
        ):
            matches.append(product)

    return matches

def print_product(product):

    if product is None:
        print("Product not found.")
        return

    print("\n========== PRODUCT ==========")
    print(f"Product ID:     {product['product_id']}")
    print(f"Store ID:       {product['store_id']}")
    print(f"Name:           {product['name']}")
    print(f"Category:       {product['category']}")
    print(f"Price:          ₦{product['price']:,.2f}")
    print(f"Stock Quantity: {product['stock_quantity']}")

def print_product_list(products):

    if not products:
        print("No products found.")
        return

    print("\n========== PRODUCTS ==========")

    for i, product in enumerate(products, start=1):

        print(f"\n[{i}]")
        print(f"Product ID:     {product['product_id']}")
        print(f"Store ID:       {product['store_id']}")
        print(f"Name:           {product['name']}")
        print(f"Category:       {product['category']}")
        print(f"Price:          ₦{product['price']:,.2f}")
        print(f"Stock Quantity: {product['stock_quantity']}")

def update_product(products, product_id):

    product = search_product_by_id(
        products,
        product_id
    )

    if product is None:
        print("Product not found.")
        return None

    print("\n========== UPDATE PRODUCT ==========")

    print(f"Current name:     {product['name']}")
    print(f"Current category: {product['category']}")
    print(f"Current price:    ₦{product['price']:,.2f}")
    print(f"Current stock:    {product['stock_quantity']}")

    new_name = validate_optional_string(
        "New product name"
    )

    new_category = validate_optional_string(
        "New category"
    )

    new_price = validate_optional_num(
        "New price",
        float
    )

    new_stock = validate_optional_num(
        "New stock quantity",
        int
    )

    # Check whether the new name belongs
    # to another product in the same store.
    if new_name:

        existing_product = search_product_by_name(
            products,
            product["store_id"],
            new_name
        )

        if (
            existing_product is not None
            and existing_product["product_id"]
            != product["product_id"]
        ):
            print(
                f"\nProduct '{new_name}' already exists "
                f"in this store."
            )
            return None

        product["name"] = new_name

    if new_category:
        product["category"] = new_category

    if new_price is not None:
        product["price"] = new_price

    if new_stock is not None:
        product["stock_quantity"] = new_stock

    save_all_products(products)

    print("\nProduct successfully updated.")

    return product

def delete_product(products, receipts, product_id):

    product = search_product_by_id(
        products,
        product_id
    )

    if product is None:
        print("Product not found.")
        return False

    # Check whether the product appears
    # in any receipt.
    for receipt in receipts:

        for item in receipt.get("items", []):

            if item.get("product_id") == product_id:

                print(
                    f"\nCannot delete product "
                    f"{product['name']}."
                )

                print(
                    "This product has already "
                    "been used in a receipt."
                )

                return False

    print_product(product)

    confirm = input(
        "\nPermanently delete this product?\n"
        "Type Yes to delete or No to cancel: "
    ).strip().lower()

    if confirm == "no":

        print("Deletion cancelled.")
        return False

    elif confirm == "yes":

        products.remove(product)

        save_all_products(products)

        print("Product deleted successfully.")

        return True

    else:

        print(
            "Invalid option.\n"
            "Deletion cancelled."
        )

        return False

