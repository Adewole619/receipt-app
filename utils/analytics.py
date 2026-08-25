
#-------------------------RECEIPT STATISTIC METHOD--------------

def total_receipts(receipts):
    total = len(receipts)
    return total

def total_sales(receipts):
    total_sales = 0
    for receipt in receipts:
        total_sales += receipt.get("grand_total", 0)

    return total_sales

def average_receipt(receipts):
    if not receipts:
        return 0
    average = total_sales(receipts) / total_receipts(receipts)
    return average


def smallest_receipt(receipts):
    # return min(receipt["grand_total"] for receipt in receipts)
    if not receipts:
        return None
    smallest = receipts[0]

    for receipt in receipts:
        if receipt["grand_total"] < smallest["grand_total"]:
            smallest = receipt

    return smallest

def largest_receipt(receipts):
    # return max(receipt["grand_total"] for receipt in receipts)
    if not receipts:
        return None
    
    largest = receipts[0]

    for receipt in receipts:
        if receipt["grand_total"] > largest["grand_total"]:
            largest = receipt

    return largest

#-----------------------STORAGE STATISTICS METHODS--------------------------

def receipts_per_store(receipts):
    store_counts = {}

    for receipt in receipts:
        store = receipt["store"]

        # if store in store_count:
        #     store_counts[store] +=1
        # else:
        #     store_counts[store] = 1
        store_counts[store]= store_counts.get(store, 0) + 1

    return store_counts

def sales_per_store(receipts):
    store_sales = {}
    for receipt in receipts:
        store = receipt["store"]
        store_sales[store] = store_sales.get(store, 0) + receipt.get("grand_total", 0)

    return store_sales

def highest_spending_store(receipts):
    store_sales = sales_per_store(receipts)

    if not store_sales:
        return None
    
    highest_store = max(store_sales, key=store_sales.get)

    return {highest_store: store_sales[highest_store]}

def lowest_spending_store(receipts):
    store_sales = sales_per_store(receipts)

    if not store_sales:
        return None
    
    lowest_store = min(store_sales, key=store_sales.get)

    return {lowest_store: store_sales[lowest_store]}

def average_sales_per_store(receipts):

    store_sales = sales_per_store(receipts)

    if not store_sales:
        return None
    
    receipts_count = receipts_per_store(receipts)

    average_sales = {}

    for store in store_sales:
        average_sales[store] = store_sales[store] / receipts_count[store]

    return average_sales

# -----------------------------DISPLAY FUNCTIONS---------------------

def print_a_receipt(receipt, title="Receipt"):
    print(f"{title}\n")
    print(f"Store:\n{receipt['store']}\n")
    print(f"Receipt:\n{receipt['receipt_number']}\n")
    print(f"Grand Total:\n₦{receipt['grand_total']:,.2f}")



def print_store_count(store_counts):
    for store, count in store_counts.items():
        label = "receipt" if count == 1 else "receipts"
        print(f"{store}: {count} {label}")

    # counts = receipts_per_store(receipts)
    # for store, count in counts.items():
    #     print(f"{store}: {count} receipt{'s' if count != 1 else ''}")



def print_store_sales(store_sales, title="Store sales"):
    print(f"{title}\n")
    for store, sales in store_sales.items():
        print(f"{store}: ₦{sales:,.2f}")


#-------------------------PRODUCT SALES STATISTICS--------------------------

def units_sold_per_product(receipts):

    product_sales = {}

    for receipt in receipts:

        for item in receipt["items"]:

            product_id = item["product_id"]
            product_name = item["name"]
            product_quantity = item["quantity"]

            if product_id not in product_sales:

                product_sales[product_id] = {
                    "product_name": product_name,
                    "product_quantity": product_quantity
                }

            else:

                product_sales[product_id]["product_quantity"] += product_quantity

    return product_sales

def print_product_sales(product_sales):

    print("\n========== UNITS SOLD BY PRODUCT ==========")

    for product_id, product in product_sales.items():

        product_name = product["product_name"]
        product_quantity = product["product_quantity"]

        label = "unit" if product_quantity == 1 else "units"

        print(
            f"Product ID:       {product_id}"
        )
        print(
            f"Product Name:     {product_name}"
        )
        print(
            f"Units Sold:       {product_quantity} {label}"
        )
        print("--------------------------------------")


def sales_revenue_per_product(receipts):

    product_sales = {}

    for receipt in receipts:

        for item in receipt["items"]:
            product_id = item["product_id"]
            product_name = item["name"]
            product_subtotal = item["subtotal"]

            if product_id not in product_sales:
                product_sales[product_id] = {
                    "product_name": product_name,
                    "sales_revenue": product_subtotal
                }

            else:
                product_sales[product_id]["sales_revenue"] += product_subtotal

    return product_sales

def print_product_sales_revenue(product_sales):

    print("\n========== SALES REVENUE BY PRODUCT ==========")

    for product_id, product in product_sales.items():

        print(
            f"Product ID:       {product_id}"
        )

        print(
            f"Product Name:     {product['product_name']}"
        )

        print(
            f"Sales Revenue:    "
            f"₦{product['sales_revenue']:,.2f}"
        )

        print("--------------------------------------")

def best_selling_product(receipts):
    best_selling = {}
    product_sales= units_sold_per_product(receipts)
    if not product_sales:
        return None

    best_selling_product_id = max(product_sales, key= lambda product_id: product_sales[product_id]["product_quantity"])

    best_selling[best_selling_product_id] = {
        "product_name": product_sales[best_selling_product_id]["product_name"],
        "product_quantity": product_sales[best_selling_product_id]["product_quantity"]
    }

    return best_selling


def lowest_selling_product(receipts):

    lowest_selling = {}

    product_sales = units_sold_per_product(receipts)

    if not product_sales:
        return None

    lowest_selling_product_id = min(
        product_sales,
        key=lambda product_id:
            product_sales[product_id]["product_quantity"]
    )

    lowest_selling[lowest_selling_product_id] = {
        "product_name":
            product_sales[lowest_selling_product_id]["product_name"],

        "product_quantity":
            product_sales[lowest_selling_product_id]["product_quantity"]
    }

    return lowest_selling

def print_lowest_selling_product(product):

    if not product:
        print("No product sales found.")
        return

    print("\n========== LOWEST-SELLING PRODUCT ==========")

    for product_id, details in product.items():

        print(f"Product ID:       {product_id}")
        print(f"Product Name:     {details['product_name']}")
        print(f"Units Sold:       {details['product_quantity']}")

def print_selling_product(product, selling_type="Highest/Lowest"):

    if not product:
        print("No product sales found.")
        return
    
    print(f"\n========== {selling_type.upper()}-SELLING PRODUCT ==========")

    for product_id, details in product.items():

        print(f"Product ID:       {product_id}")
        print(f"Product Name:     {details['product_name']}")
        print(f"Units Sold:       {details['product_quantity']}")

def revenue_per_product(receipts):

    product_revenue = {}

    for receipt in receipts:

        for item in receipt.get("items", []):

            product_id = item.get("product_id")

            if not product_id:
                continue

            product_name = item.get("name", "Unknown")
            subtotal = item.get("subtotal", 0)

            if product_id not in product_revenue:

                product_revenue[product_id] = {
                    "product_name": product_name,
                    "revenue": 0
                }

            product_revenue[product_id]["revenue"] += subtotal

    return product_revenue

def highest_revenue_product(receipts):

    product_revenue = revenue_per_product(receipts)

    if not product_revenue:
        return None

    highest_product_id = max(
        product_revenue,
        key=lambda product_id:
            product_revenue[product_id]["revenue"]
    )

    return {
        highest_product_id: {
            "product_name":
                product_revenue[highest_product_id]["product_name"],

            "revenue":
                product_revenue[highest_product_id]["revenue"]
        }
    }

def lowest_revenue_product(receipts):

    product_revenue = revenue_per_product(receipts)

    if not product_revenue:
        return None

    lowest_product_id = min(
        product_revenue,
        key=lambda product_id:
            product_revenue[product_id]["revenue"]
    )

    return {
        lowest_product_id: {
            "product_name":
                product_revenue[lowest_product_id]["product_name"],

            "revenue":
                product_revenue[lowest_product_id]["revenue"]
        }
    }

def print_revenue_product(product, title="Highest"):

    if not product:
        print("No product revenue found.")
        return

    print(
        f"\n========== "
        f"{title.upper()}-REVENUE PRODUCT "
        f"=========="
    )

    for product_id, details in product.items():

        print(f"Product ID:       {product_id}")
        print(f"Product Name:     {details['product_name']}")
        print(f"Revenue:          ₦{details['revenue']:,.2f}")

def average_price_per_product(receipts):

    product_sales = units_sold_per_product(receipts)
    product_revenue = revenue_per_product(receipts)

    if not product_sales:
        return {}

    average_prices = {}

    for product_id in product_sales:

        quantity = product_sales[product_id]["product_quantity"]
        revenue = product_revenue[product_id]["revenue"]

        if quantity == 0:
            continue

        average_prices[product_id] = {
            "product_name":
                product_sales[product_id]["product_name"],

            "average_price":
                revenue / quantity
        }

    return average_prices

def print_average_product_price(products):

    if not products:
        print("No product sales found.")
        return

    print("\n========== AVERAGE PRODUCT PRICE ==========")

    for product_id, details in products.items():

        print(f"Product ID:       {product_id}")
        print(f"Product Name:     {details['product_name']}")
        print(
            f"Average Price:    "
            f"₦{details['average_price']:,.2f}"
        )

def product_revenue_percentage(receipts):

    product_revenue = revenue_per_product(receipts)

    if not product_revenue:
        return {}

    total_revenue = sum(
        details["revenue"]
        for details in product_revenue.values()
    )

    if total_revenue == 0:
        return {}

    revenue_percentage = {}

    for product_id, details in product_revenue.items():

        percentage = (
            details["revenue"] / total_revenue
        ) * 100

        revenue_percentage[product_id] = {
            "product_name": details["product_name"],
            "revenue": details["revenue"],
            "percentage": percentage
        }

    return revenue_percentage

def print_product_revenue_percentage(products):

    if not products:
        print("No product revenue found.")
        return

    print(
        "\n========== PRODUCT REVENUE CONTRIBUTION =========="
    )

    for product_id, details in products.items():

        print(f"Product ID:       {product_id}")
        print(f"Product Name:     {details['product_name']}")
        print(
            f"Revenue:          "
            f"₦{details['revenue']:,.2f}"
        )
        print(
            f"Revenue Share:    "
            f"{details['percentage']:.2f}%"
        )

def product_performance_summary(receipts):

    product_sales = units_sold_per_product(receipts)
    product_revenue = revenue_per_product(receipts)

    if not product_sales:
        return {}

    product_summary = {}

    for product_id, sales_details in product_sales.items():

        product_name = sales_details["product_name"]
        quantity = sales_details["product_quantity"]

        revenue = product_revenue[product_id]["revenue"]

        if quantity > 0:
            average_price = revenue / quantity
        else:
            average_price = 0

        product_summary[product_id] = {
            "product_name": product_name,
            "units_sold": quantity,
            "revenue": revenue,
            "average_price": average_price
        }

    return product_summary

def print_product_performance(summary):

    if not summary:
        print("No product performance data found.")
        return

    print(
        "\n========== PRODUCT PERFORMANCE =========="
    )

    for product_id, details in summary.items():

        print(f"\nProduct ID:       {product_id}")
        print(f"Product Name:     {details['product_name']}")
        print(f"Units Sold:       {details['units_sold']}")
        print(f"Revenue:          ₦{details['revenue']:,.2f}")
        print(
            f"Average Price:    "
            f"₦{details['average_price']:,.2f}"
        )

        print("--------------------------------------")

def price_history_per_product(receipts):

    price_history = {}

    for receipt in receipts:

        created_at = receipt.get("created_at")

        if not created_at:
            continue

        for item in receipt.get("items", []):

            product_id = item.get("product_id")
            if not product_id:
                continue

            product_name = item.get("name")
            price = item.get("price")

            if price is None:
                continue

            if product_id not in price_history:

                price_history[product_id] = {
                    "product_name": product_name,
                    "prices_history": []
                }

            prices = price_history[product_id]["prices_history"]

            # first recorded price
            if not prices:
                prices.append({
                    "created_at": created_at,
                    "price": price
                })

            # only record if the price changed
            elif prices[-1]["price"] != price:
                prices.append({
                    "created_at": created_at,
                    "price": price
                })

    return price_history


def print_price_history(price_history):

    if not price_history:
        print("No price history found.")
        return

    print("\n========== PRODUCT PRICE HISTORY ==========")

    for product_id, details in price_history.items():

        print(f"\nProduct ID:   {product_id}")
        print(f"Product Name: {details['product_name']}")

        print("\nDate and Time              Price")
        print("--------------------------------------")

        for record in details["prices_history"]:

            date_time = record["created_at"].replace("T", " ")
            price = record["price"]

            print(
                f"{date_time:<25} "
                f"₦{price:,.2f}"
            )

        print("--------------------------------------")

def price_history_for_product(receipts, product_id):

    price_history = price_history_per_product(receipts)

    product_id = product_id.strip().upper()

    if product_id not in price_history:
        return None

    return {
        product_id: price_history[product_id]
    }


def price_change_analysis(price_history):

    if not price_history:
        return None

    analysis = {}

    for product_id, details in price_history.items():

        prices = details["prices_history"]

        if not prices:
            continue

        first_price = prices[0]["price"]
        current_price = prices[-1]["price"]

        highest_price = max(
            record["price"]
            for record in prices
        )

        lowest_price = min(
            record["price"]
            for record in prices
        )

        price_changes = len(prices) - 1

        price_difference = current_price - first_price

        if first_price != 0:
            percentage_change = (
                price_difference / first_price
            ) * 100
        else:
            percentage_change = 0

        analysis[product_id] = {
            "product_name": details["product_name"],
            "first_price": first_price,
            "current_price": current_price,
            "highest_price": highest_price,
            "lowest_price": lowest_price,
            "price_changes": price_changes,
            "price_difference": price_difference,
            "percentage_change": percentage_change
        }

    return analysis

def print_price_change_analysis(analysis):

    if not analysis:
        print("No price change analysis found.")
        return

    print("\n========== PRICE CHANGE ANALYSIS ==========")

    for product_id, details in analysis.items():

        print(f"\nProduct ID:       {product_id}")
        print(f"Product Name:     {details['product_name']}")

        print(
            f"First Price:      "
            f"₦{details['first_price']:,.2f}"
        )

        print(
            f"Current Price:    "
            f"₦{details['current_price']:,.2f}"
        )

        print(
            f"Highest Price:    "
            f"₦{details['highest_price']:,.2f}"
        )

        print(
            f"Lowest Price:     "
            f"₦{details['lowest_price']:,.2f}"
        )

        print(
            f"Price Changes:    "
            f"{details['price_changes']}"
        )

        print(
            f"Price Difference: "
            f"₦{details['price_difference']:+,.2f}"
        )

        print(
            f"Percentage Change:"
            f" {details['percentage_change']:+.2f}%"
        )

        print("--------------------------------------")


def products_with_price_increases(analysis):

    if not analysis:
        return {}

    increased = {}

    for product_id, details in analysis.items():

        if details["price_difference"] > 0:
            increased[product_id] = {
                "product_name": details["product_name"],
                "first_price": details["first_price"],
                "current_price": details["current_price"],
                "price_difference": details["price_difference"],
                "percentage_change": details["percentage_change"]
            }

    return increased

def products_with_price_decreases(analysis):

    if not analysis:
        return {}

    decreased = {}

    for product_id, details in analysis.items():

        if details["price_difference"] < 0:
            decreased[product_id] = {
                "product_name": details["product_name"],
                "first_price": details["first_price"],
                "current_price": details["current_price"],
                "price_difference": details["price_difference"],
                "percentage_change": details["percentage_change"]
            }

    return decreased

def print_price_changes(products, title):

    if not products:
        print(f"\nNo products found for {title.lower()}.")
        return

    print(f"\n========== {title.upper()} ==========")

    for product_id, details in products.items():

        print(f"\nProduct ID:       {product_id}")
        print(f"Product Name:     {details['product_name']}")

        print(
            f"First Price:      "
            f"₦{details['first_price']:,.2f}"
        )

        print(
            f"Current Price:    "
            f"₦{details['current_price']:,.2f}"
        )

        print(
            f"Price Difference: "
            f"₦{details['price_difference']:+,.2f}"
        )

        print(
            f"Percentage Change:"
            f" {details['percentage_change']:+.2f}%"
        )

        print("--------------------------------------")


def largest_price_increase(analysis):

    if not analysis:
        return None

    increases = {
        product_id: details
        for product_id, details in analysis.items()
        if details["price_difference"] > 0
    }

    if not increases:
        return None

    product_id = max(
        increases,
        key=lambda product_id:
            increases[product_id]["price_difference"]
    )

    return {
        product_id: increases[product_id]
    }


def largest_price_decrease(analysis):

    if not analysis:
        return None

    decreases = {
        product_id: details
        for product_id, details in analysis.items()
        if details["price_difference"] < 0
    }

    if not decreases:
        return None

    product_id = min(
        decreases,
        key=lambda product_id:
            decreases[product_id]["price_difference"]
    )

    return {
        product_id: decreases[product_id]
    }

def print_largest_price_change(product, title):

    if not product:
        print(f"\nNo {title.lower()} found.")
        return

    print(f"\n========== {title.upper()} ==========")

    for product_id, details in product.items():

        print(f"\nProduct ID:       {product_id}")
        print(f"Product Name:     {details['product_name']}")

        print(
            f"First Price:      "
            f"₦{details['first_price']:,.2f}"
        )

        print(
            f"Current Price:    "
            f"₦{details['current_price']:,.2f}"
        )

        print(
            f"Price Difference: "
            f"₦{details['price_difference']:+,.2f}"
        )

        print(
            f"Percentage Change:"
            f" {details['percentage_change']:+.2f}%"
        )

        print("--------------------------------------")



def largest_percentage_increase(analysis):

    if not analysis:
        return None

    increases = {
        product_id: details
        for product_id, details in analysis.items()
        if details["percentage_change"] > 0
    }

    if not increases:
        return None

    product_id = max(
        increases,
        key=lambda product_id:
            increases[product_id]["percentage_change"]
    )

    return {
        product_id: increases[product_id]
    }


def largest_percentage_decrease(analysis):

    if not analysis:
        return None

    decreases = {
        product_id: details
        for product_id, details in analysis.items()
        if details["percentage_change"] < 0
    }

    if not decreases:
        return None

    product_id = min(
        decreases,
        key=lambda product_id:
            decreases[product_id]["percentage_change"]
    )

    return {
        product_id: decreases[product_id]
    }


def products_sorted_by_units_sold(product_sales):

    if not product_sales:
        return {}

    sorted_products = dict(
        sorted(
            product_sales.items(),
            key=lambda item: item[1]["product_quantity"],
            reverse=True
        )
    )

    return sorted_products

def top_selling_products(product_sales, limit=5):

    if not product_sales:
        return {}

    sorted_products = products_sorted_by_units_sold(product_sales)

    top_products = dict(
        list(sorted_products.items())[:limit]
    )

    return top_products

def print_top_selling_products(product_sales):

    if not product_sales:
        print("No product sales found.")
        return

    print("\n========== TOP-SELLING PRODUCTS ==========")

    for position, (product_id, product) in enumerate(
        product_sales.items(),
        start=1
    ):

        product_name = product["product_name"]
        product_quantity = product["product_quantity"]

        label = "unit" if product_quantity == 1 else "units"

        print(f"\n{position}. {product_name}")
        print(f"   Product ID: {product_id}")
        print(f"   Units Sold: {product_quantity} {label}")

        print("--------------------------------------")

def products_sorted_by_units_sold_ascending(product_sales):

    if not product_sales:
        return {}

    sorted_products = dict(
        sorted(
            product_sales.items(),
            key=lambda item: item[1]["product_quantity"]
        )
    )

    return sorted_products

def lowest_selling_products(product_sales, limit=5):

    if not product_sales:
        return {}

    sorted_products = products_sorted_by_units_sold_ascending(
        product_sales
    )

    lowest_products = dict(
        list(sorted_products.items())[:limit]
    )

    return lowest_products

def print_lowest_selling_products(product_sales):

    if not product_sales:
        print("No product sales found.")
        return

    print("\n========== LOWEST-SELLING PRODUCTS ==========")

    for position, (product_id, product) in enumerate(
        product_sales.items(),
        start=1
    ):

        product_name = product["product_name"]
        product_quantity = product["product_quantity"]

        label = "unit" if product_quantity == 1 else "units"

        print(f"\n{position}. {product_name}")
        print(f"   Product ID: {product_id}")
        print(f"   Units Sold: {product_quantity} {label}")

        print("--------------------------------------")

def revenue_per_product(receipts):

    product_revenue = {}

    for receipt in receipts:

        for item in receipt.get("items", []):

            product_id = item.get("product_id")

            # Ignore old receipt items without product_id
            if not product_id:
                continue

            product_name = item.get("name")
            quantity = item.get("quantity", 0)
            price = item.get("price", 0)

            revenue = price * quantity

            if product_id not in product_revenue:

                product_revenue[product_id] = {
                    "product_name": product_name,
                    "revenue": 0
                }

            product_revenue[product_id]["revenue"] += revenue

    return product_revenue

def print_revenue_per_product(product_revenue):

    if not product_revenue:
        print("No product revenue found.")
        return

    print("\n========== REVENUE PER PRODUCT ==========")

    for product_id, details in product_revenue.items():

        product_name = details["product_name"]
        revenue = details["revenue"]

        print(f"\nProduct ID:     {product_id}")
        print(f"Product Name:   {product_name}")
        print(f"Revenue:        ₦{revenue:,.2f}")

        print("--------------------------------------")

def products_sorted_by_revenue(product_revenue):

    if not product_revenue:
        return {}

    sorted_products = dict(
        sorted(
            product_revenue.items(),
            key=lambda item: item[1]["revenue"],
            reverse=True
        )
    )

    return sorted_products

def highest_revenue_products(product_revenue, limit=5):

    if not product_revenue:
        return {}

    sorted_products = products_sorted_by_revenue(
        product_revenue
    )

    highest_products = dict(
        list(sorted_products.items())[:limit]
    )

    return highest_products

def print_highest_revenue_products(product_revenue):

    if not product_revenue:
        print("No product revenue found.")
        return

    print("\n========== HIGHEST-REVENUE PRODUCTS ==========")

    for position, (product_id, product) in enumerate(
        product_revenue.items(),
        start=1
    ):

        product_name = product["product_name"]
        revenue = product["revenue"]

        print(f"\n{position}. {product_name}")
        print(f"   Product ID: {product_id}")
        print(f"   Revenue:    ₦{revenue:,.2f}")

        print("--------------------------------------")

def products_sorted_by_revenue_ascending(product_revenue):

    if not product_revenue:
        return {}

    sorted_products = dict(
        sorted(
            product_revenue.items(),
            key=lambda item: item[1]["revenue"]
        )
    )

    return sorted_products

def lowest_revenue_products(product_revenue, limit=5):

    if not product_revenue:
        return {}

    sorted_products = products_sorted_by_revenue_ascending(
        product_revenue
    )

    lowest_products = dict(
        list(sorted_products.items())[:limit]
    )

    return lowest_products

def print_lowest_revenue_products(product_revenue):

    if not product_revenue:
        print("No product revenue found.")
        return

    print("\n========== LOWEST-REVENUE PRODUCTS ==========")

    for position, (product_id, product) in enumerate(
        product_revenue.items(),
        start=1
    ):

        product_name = product["product_name"]
        revenue = product["revenue"]

        print(f"\n{position}. {product_name}")
        print(f"   Product ID: {product_id}")
        print(f"   Revenue:    ₦{revenue:,.2f}")

        print("--------------------------------------")

def average_price_per_product(receipts):

    product_data = {}

    for receipt in receipts:

        for item in receipt.get("items", []):

            product_id = item.get("product_id")

            # Skip old receipt items without product_id
            if not product_id:
                continue

            product_name = item.get("name")
            quantity = item.get("quantity", 0)
            price = item.get("price", 0)

            revenue = price * quantity

            if product_id not in product_data:

                product_data[product_id] = {
                    "product_name": product_name,
                    "total_units": 0,
                    "total_revenue": 0
                }

            product_data[product_id]["total_units"] += quantity
            product_data[product_id]["total_revenue"] += revenue

    average_prices = {}

    for product_id, details in product_data.items():

        if details["total_units"] == 0:
            continue

        average_prices[product_id] = {
            "product_name": details["product_name"],
            "average_price":
                details["total_revenue"] /
                details["total_units"]
        }

    return average_prices

def print_average_price_per_product(average_prices):

    if not average_prices:
        print("No average price data found.")
        return

    print("\n========== AVERAGE SELLING PRICE PER PRODUCT ==========")

    for product_id, details in average_prices.items():

        product_name = details["product_name"]
        average_price = details["average_price"]

        print(f"\nProduct ID:       {product_id}")
        print(f"Product Name:     {product_name}")
        print(f"Average Price:    ₦{average_price:,.2f}")

        print("--------------------------------------")

def price_changes_per_product(price_history):

    if not price_history:
        return {}

    price_changes = {}

    for product_id, details in price_history.items():

        prices = details["prices_history"]

        if len(prices) < 2:
            continue

        product_changes = []

        for i in range(1, len(prices)):

            previous = prices[i - 1]
            current = prices[i]

            previous_price = previous["price"]
            current_price = current["price"]

            change = current_price - previous_price

            if previous_price == 0:
                percentage_change = 0
            else:
                percentage_change = (
                    change / previous_price
                ) * 100

            product_changes.append({
                "from_date": previous["created_at"],
                "to_date": current["created_at"],
                "old_price": previous_price,
                "new_price": current_price,
                "change": change,
                "percentage_change": percentage_change
            })

        price_changes[product_id] = {
            "product_name": details["product_name"],
            "changes": product_changes
        }

    return price_changes

def print_price_changes(price_changes):

    if not price_changes:
        print("No price changes found.")
        return

    print("\n========== PRODUCT PRICE CHANGES ==========")

    for product_id, details in price_changes.items():

        product_name = details["product_name"]
        changes = details["changes"]

        print(f"\nProduct ID:       {product_id}")
        print(f"Product Name:     {product_name}")

        print("\nPrice Changes:")
        print("--------------------------------------")

        for change in changes:

            from_date = change["from_date"].replace("T", " ")
            to_date = change["to_date"].replace("T", " ")

            old_price = change["old_price"]
            new_price = change["new_price"]
            amount_change = change["change"]
            percentage_change = change["percentage_change"]

            print(f"From:             {from_date}")
            print(f"To:               {to_date}")
            print(f"Old Price:        ₦{old_price:,.2f}")
            print(f"New Price:        ₦{new_price:,.2f}")
            print(f"Amount Changed:   ₦{amount_change:+,.2f}")
            print(f"Percentage:       {percentage_change:+.2f}%")
            print("--------------------------------------")

def largest_price_increase(price_changes):

    if not price_changes:
        return None

    largest = None

    for product_id, details in price_changes.items():

        for change in details["changes"]:

            if change["change"] <= 0:
                continue

            if largest is None or change["change"] > largest["change"]:

                largest = {
                    "product_id": product_id,
                    "product_name": details["product_name"],
                    "from_date": change["from_date"],
                    "to_date": change["to_date"],
                    "old_price": change["old_price"],
                    "new_price": change["new_price"],
                    "change": change["change"],
                    "percentage_change": change["percentage_change"]
                }

    return largest

def largest_price_decrease(price_changes):

    if not price_changes:
        return None

    largest = None

    for product_id, details in price_changes.items():

        for change in details["changes"]:

            if change["change"] >= 0:
                continue

            if largest is None or change["change"] < largest["change"]:

                largest = {
                    "product_id": product_id,
                    "product_name": details["product_name"],
                    "from_date": change["from_date"],
                    "to_date": change["to_date"],
                    "old_price": change["old_price"],
                    "new_price": change["new_price"],
                    "change": change["change"],
                    "percentage_change": change["percentage_change"]
                }

    return largest

def print_price_change_summary(change, title):

    if not change:
        print(f"\nNo {title.lower()} found.")
        return

    print(f"\n========== {title.upper()} ==========")

    print(f"Product ID:       {change['product_id']}")
    print(f"Product Name:     {change['product_name']}")

    print(f"\nFrom:             {change['from_date'].replace('T', ' ')}")
    print(f"To:               {change['to_date'].replace('T', ' ')}")

    print(f"\nOld Price:        ₦{change['old_price']:,.2f}")
    print(f"New Price:        ₦{change['new_price']:,.2f}")
    print(f"Amount Changed:   ₦{change['change']:+,.2f}")
    print(f"Percentage:       {change['percentage_change']:+.2f}%")

    print("--------------------------------------")

def sales_per_date(receipts):

    sales_by_date = {}

    for receipt in receipts:

        created_at = receipt.get("created_at")

        if not created_at:
            continue

        date = created_at.split("T")[0]

        sales_by_date[date] = (
            sales_by_date.get(date, 0)
            + receipt.get("grand_total", 0)
        )

    return sales_by_date

def print_sales_per_date(sales_by_date):

    if not sales_by_date:
        print("No sales data found.")
        return

    print("\n========== SALES PER DATE ==========")

    for date, sales in sorted(sales_by_date.items()):

        print(
            f"{date}: "
            f"₦{sales:,.2f}"
        )

    print("--------------------------------------")

def receipts_per_date(receipts):

    receipt_counts = {}

    for receipt in receipts:

        created_at = receipt.get("created_at")

        if not created_at:
            continue

        date = created_at.split("T")[0]

        receipt_counts[date] = (
            receipt_counts.get(date, 0) + 1
        )

    return receipt_counts

def print_receipts_per_date(receipt_counts):

    if not receipt_counts:
        print("No receipt data found.")
        return

    print("\n========== RECEIPTS PER DATE ==========")

    for date, count in sorted(receipt_counts.items()):

        label = "receipt" if count == 1 else "receipts"

        print(
            f"{date}: "
            f"{count} {label}"
        )

    print("--------------------------------------")

def daily_sales_report(receipts):

    sales = sales_per_date(receipts)
    receipt_counts = receipts_per_date(receipts)

    if not sales and not receipt_counts:
        return {}

    report = {}

    dates = set(sales) | set(receipt_counts)

    for date in sorted(dates):

        report[date] = {
            "receipts": receipt_counts.get(date, 0),
            "sales": sales.get(date, 0)
        }

    return report

def print_daily_sales_report(report):

    if not report:
        print("No daily sales data found.")
        return

    print("\n========== DAILY SALES REPORT ==========")

    print(
        f"{'Date':<15}"
        f"{'Receipts':<12}"
        f"{'Sales':>15}"
    )

    print("------------------------------------------")

    for date, details in report.items():

        receipts_count = details["receipts"]
        sales = details["sales"]

        print(
            f"{date:<15}"
            f"{receipts_count:<12}"
            f"₦{sales:>13,.2f}"
        )

    print("------------------------------------------")


#----------------------------------END-----------------------------------------------------------------