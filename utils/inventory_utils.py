import json
import os

INVENTORY_HISTORY_FILE_JSON = "data/inventory_history.json"

def load_inventory_history():

    try:
        with open(INVENTORY_HISTORY_FILE_JSON, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_all_inventory_history(history):

    with open(INVENTORY_HISTORY_FILE_JSON, "w") as file:
        json.dump(history, file, indent=4)

def generate_inventory_movement_id():

    if not os.path.exists(INVENTORY_HISTORY_FILE_JSON):
        return "MOV000001"

    histories = load_inventory_history()

    if not histories:
        return "MOV000001"

    highest_number = 0

    for history in histories:

        movement_id = history.get("movement_id", "")

        if not movement_id.startswith("MOV"):
            continue

        try:

            number = int(
                movement_id.replace("MOV", "")
            )

            if number > highest_number:
                highest_number = number

        except ValueError:
            continue

    next_number = highest_number + 1

    # last_movement = history[-1]

    # last_movement_id = last_movement["movement_id"]

    # number = int(last_movement_id.replace("MOV", ""))

    # number += 1

    return f"MOV{next_number:06d}"

def record_inventory_movement(product_id, movement_type, quantity, previous_stock, new_stock, reason):

    history = load_inventory_history()

    movement_id = generate_inventory_movement_id()

    movement = {
        "movement_id": movement_id,
        "product_id": product_id,
        "type": movement_type,
        "quantity": quantity,
        "previous_stock": previous_stock,
        "new_stock": new_stock,
        "reason": reason
    }

    history.append(movement)

    save_all_inventory_history(history)

    return movement

def search_inventory_history_by_product(history, product_id):

    if not history:
        return []

    product_id = product_id.strip().upper()

    matching_movements = []

    for movement in history:

        if movement["product_id"].strip().upper() == product_id:
            matching_movements.append(movement)

    return matching_movements

def search_inventory_history_by_type(history, movement_type):

    if not history:
        return []

    movement_type = movement_type.strip().upper()

    matching_movements = []

    for movement in history:

        if movement["type"].strip().upper() == movement_type:
            matching_movements.append(movement)

    return matching_movements

def validate_inventory_history(history):

    if not history:
        print("No inventory history found.")
        return

    print("\n========== INVENTORY INTEGRITY CHECK ==========")

    valid_movements = 0
    invalid_movements = 0

    # Keep track of the latest known stock
    # for each product.
    expected_stock = {}

    for movement in history:

        movement_id = movement.get("movement_id")
        product_id = movement.get("product_id")
        movement_type = movement.get("type")
        quantity = movement.get("quantity")
        previous_stock = movement.get("previous_stock")
        new_stock = movement.get("new_stock")

        movement_is_valid = True

        # -----------------------------------------
        # 1. Check required movement type
        # -----------------------------------------

        if movement_type not in (
            "RESTOCK",
            "SALE",
            "CORRECTION"
        ):

            print(
                f"\nInvalid movement: {movement_id}"
            )

            print(
                f"Unknown movement type: "
                f"{movement_type}"
            )

            invalid_movements += 1
            continue

        # -----------------------------------------
        # 2. Check RESTOCK quantity
        # -----------------------------------------

        if movement_type == "RESTOCK" and quantity <= 0:

            print(
                f"\nInvalid movement: {movement_id}"
            )

            print(
                "RESTOCK quantity must be positive."
            )

            movement_is_valid = False

        # -----------------------------------------
        # 3. Check SALE quantity
        # -----------------------------------------

        if movement_type == "SALE" and quantity >= 0:

            print(
                f"\nInvalid movement: {movement_id}"
            )

            print(
                "SALE quantity must be negative."
            )

            movement_is_valid = False

        # -----------------------------------------
        # 4. Calculate actual stock change
        # -----------------------------------------

        actual_stock_change = (
            new_stock - previous_stock
        )

        # -----------------------------------------
        # 5. Check quantity against stock change
        # -----------------------------------------

        if movement_type == "RESTOCK":

            if actual_stock_change != quantity:

                print(
                    f"\nInvalid movement: {movement_id}"
                )

                print(
                    f"Expected stock change: "
                    f"+{quantity}"
                )

                print(
                    f"Actual stock change: "
                    f"{actual_stock_change:+}"
                )

                movement_is_valid = False

        elif movement_type == "SALE":

            if actual_stock_change != quantity:

                print(
                    f"\nInvalid movement: {movement_id}"
                )

                print(
                    f"Expected stock change: "
                    f"{quantity}"
                )

                print(
                    f"Actual stock change: "
                    f"{actual_stock_change:+}"
                )

                movement_is_valid = False

        elif movement_type == "CORRECTION":

            if actual_stock_change != quantity:

                print(
                    f"\nInvalid movement: {movement_id}"
                )

                print(
                    f"Expected stock change: "
                    f"{quantity:+}"
                )

                print(
                    f"Actual stock change: "
                    f"{actual_stock_change:+}"
                )

                movement_is_valid = False

        # -----------------------------------------
        # 6. Check previous stock against
        #    previous movement for this product
        # -----------------------------------------

        if product_id in expected_stock:

            if previous_stock != expected_stock[product_id]:

                print(
                    f"\nInvalid movement: {movement_id}"
                )

                print(
                    f"Product: {product_id}"
                )

                print(
                    f"Expected stock: "
                    f"{expected_stock[product_id]}"
                )

                print(
                    f"Recorded stock: "
                    f"{previous_stock}"
                )

                movement_is_valid = False

        # -----------------------------------------
        # 7. Update expected stock
        # -----------------------------------------

        expected_stock[product_id] = new_stock

        # -----------------------------------------
        # 8. Count result
        # -----------------------------------------

        if movement_is_valid:

            valid_movements += 1

        else:

            invalid_movements += 1

    # -----------------------------------------
    # Final report
    # -----------------------------------------

    print("\n--------------------------------------")

    print(
        f"Movements checked: {len(history)}"
    )

    print(
        f"Valid movements:   {valid_movements}"
    )

    print(
        f"Invalid movements: {invalid_movements}"
    )

    if invalid_movements == 0:

        print(
            "\nInventory history is valid."
        )

    else:

        print(
            "\nInventory history contains errors."
        )

def print_inventory_history(history):

    if not history:
        print("No inventory history found.")
        return

    print("\n========== INVENTORY HISTORY ==========")

    for movement in history:

        print(f"\nMovement ID:     {movement['movement_id']}")
        print(f"Product ID:      {movement['product_id']}")
        print(f"Type:            {movement['type']}")
        print(f"Quantity Change: {movement['quantity']:+}")
        print(f"Previous Stock:  {movement['previous_stock']}")
        print(f"New Stock:       {movement['new_stock']}")
        print(f"Reason:          {movement['reason']}")

        print("--------------------------------------")

def inventory_movement_report(history):

    if not history:
        print("No inventory history found.")
        return

    restock_count = 0
    restock_quantity = 0
    net_stock_change = 0

    sale_count = 0
    sale_quantity = 0

    correction_count = 0
    correction_increase = 0
    correction_decrease = 0

    for movement in history:

        movement_type = movement["type"]
        quantity = movement["quantity"]

        previous_stock = movement["previous_stock"]
        new_stock = movement["new_stock"]

        stock_change = new_stock - previous_stock

        net_stock_change += stock_change

        if movement_type == "RESTOCK":

            restock_count += 1
            restock_quantity += quantity

        elif movement_type == "SALE":

            sale_count += 1
            sale_quantity += abs(stock_change)

        elif movement_type == "CORRECTION":

            correction_count += 1

            if quantity > 0:
                correction_increase += quantity

            elif quantity < 0:
                correction_decrease += abs(quantity)

    print("\n========== INVENTORY MOVEMENT REPORT ==========")

    print("\nRESTOCKS")
    print(f"Movements:        {restock_count}")
    print(f"Stock added:      +{restock_quantity}")

    print("\nSALES")
    print(f"Movements:        {sale_count}")
    print(f"Stock sold:        {sale_quantity}")

    print("\nCORRECTIONS")
    print(f"Movements:        {correction_count}")
    print(f"Stock increased:  +{correction_increase}")
    print(f"Stock decreased:  -{correction_decrease}")

    print("\n--------------------------------------")

    print(
        f"Total movements:  "
        f"{len(history)}"
    )

    print(
        f"Net stock change: "
        f"{net_stock_change:+}"
    )


def product_movement_report(history, product_id):

    movements = search_inventory_history_by_product(
        history,
        product_id
    )

    if not movements:
        print(
            f"No inventory history found "
            f"for {product_id}."
        )
        return

    restock_quantity = 0
    sale_quantity = 0
    correction_increase = 0
    correction_decrease = 0

    net_stock_change = 0

    for movement in movements:

        movement_type = movement["type"]

        previous_stock = movement["previous_stock"]
        new_stock = movement["new_stock"]

        stock_change = new_stock - previous_stock

        net_stock_change += stock_change

        if movement_type == "RESTOCK":

            restock_quantity += stock_change

        elif movement_type == "SALE":

            sale_quantity += abs(stock_change)

        elif movement_type == "CORRECTION":

            if stock_change > 0:
                correction_increase += stock_change

            elif stock_change < 0:
                correction_decrease += abs(stock_change)

    correction_increase_display = (
        f"+{correction_increase}"
        if correction_increase > 0
        else "0"
    )

    correction_decrease_display = (
        f"-{correction_decrease}"
        if correction_decrease > 0
        else "0"
    )

    print("\n========== PRODUCT MOVEMENT REPORT ==========")

    print(
        f"\nProduct ID: {product_id.upper()}"
    )

    print("\nRESTOCKS")
    print(
        f"Stock added:      +{restock_quantity}"
    )

    print("\nSALES")
    print(
        f"Stock sold:        {sale_quantity}"
    )

    print("\nCORRECTIONS")
    print(
        f"Stock increased:  "
        f"{correction_increase_display}"
    )

    print(
        f"Stock decreased:  "
        f"{correction_decrease_display}"
    )

    print("\n--------------------------------------")

    print(
        f"Movements:        "
        f"{len(movements)}"
    )

    print(
        f"Net stock change: "
        f"{net_stock_change:+}"
    )















