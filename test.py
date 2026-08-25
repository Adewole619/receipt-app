
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


test_receipts = [
  {
    "store": "Lagos",
    "receipt_number": "RCP0000096",
    "created_at": "2026-08-23T09:00",
    "customer_id": "CUS000001",
    "customer_name": "Chinedu Okafor",
    "items": [
      {
        "product_id": "PRD000007",
        "name": "PowerBank",
        "price": 29000.0,
        "quantity": 2,
        "subtotal": 58000.0
      }
    ],
    "grand_total": 58000.0
  },
  {
    "store": "Abuja",
    "receipt_number": "RCP0000097",
    "created_at": "2026-08-23T09:05",
    "customer_id": "CUS000002",
    "customer_name": "Aisha Bello",
    "items": [
      {
        "product_id": "PRD000008",
        "name": "Router",
        "price": 57000.0,
        "quantity": 2,
        "subtotal": 114000.0
      }
    ],
    "grand_total": 114000.0
  },
  {
    "store": "Ibadan",
    "receipt_number": "RCP0000098",
    "created_at": "2026-08-23T09:10",
    "customer_id": "CUS000003",
    "customer_name": "Tunde Adeyemi",
    "items": [
      {
        "product_id": "PRD000009",
        "name": "SSD",
        "price": 92000.0,
        "quantity": 1,
        "subtotal": 92000.0
      }
    ],
    "grand_total": 92000.0
  },
  {
    "store": "Kano",
    "receipt_number": "RCP0000099",
    "created_at": "2026-08-23T09:15",
    "customer_id": "CUS000004",
    "customer_name": "Ngozi Eze",
    "items": [
      {
        "product_id": "PRD000010",
        "name": "HardDrive",
        "price": 73000.0,
        "quantity": 2,
        "subtotal": 146000.0
      }
    ],
    "grand_total": 146000.0
  },
  {
    "store": "PortHarcourt",
    "receipt_number": "RCP0000100",
    "created_at": "2026-08-23T09:20",
    "customer_id": "CUS000005",
    "customer_name": "Emeka Nwosu",
    "items": [
      {
        "product_id": "PRD000011",
        "name": "Laptop",
        "price": 270000.0,
        "quantity": 1,
        "subtotal": 270000.0
      },
      {
        "product_id": "PRD000013",
        "name": "Mouse",
        "price": 8000.0,
        "quantity": 2,
        "subtotal": 16000.0
      }
    ],
    "grand_total": 286000.0
  },
  {
    "store": "Hymers",
    "receipt_number": "RCP0000101",
    "created_at": "2026-08-23T09:25",
    "customer_id": "CUS000005",
    "customer_name": "Emeka Nwosu",
    "items": [
      {
        "product_id": "PRD000014",
        "name": "washing machine",
        "price": 206000.0,
        "quantity": 1,
        "subtotal": 206000.0
      },
      {
        "product_id": "PRD000015",
        "name": "Deep freezer",
        "price": 256000.0,
        "quantity": 2,
        "subtotal": 512000.0
      }
    ],
    "grand_total": 718000.0
  },
  {
    "store": "Shoprite Lagos",
    "receipt_number": "RCP0000102",
    "created_at": "2026-08-23T09:30",
    "customer_id": "CUS000005",
    "customer_name": "Emeka Nwosu",
    "items": [
      {
        "product_id": "PRD000001",
        "name": "Coca-Cola 50cl",
        "price": 500,
        "quantity": 4,
        "subtotal": 2000
      },
      {
        "product_id": "PRD000002",
        "name": "Pepsi 50cl",
        "price": 450,
        "quantity": 5,
        "subtotal": 2250
      }
    ],
    "grand_total": 4250
  },
  {
    "store": "Shoprite Lagos",
    "receipt_number": "RCP0000103",
    "created_at": "2026-08-23T09:35",
    "customer_id": "CUS000008",
    "customer_name": "Amaka Obi",
    "items": [
      {
        "product_id": "PRD000001",
        "name": "Coca-Cola 50cl",
        "price": 500,
        "quantity": 3,
        "subtotal": 1500
      },
      {
        "product_id": "PRD000002",
        "name": "Pepsi 50cl",
        "price": 450,
        "quantity": 5,
        "subtotal": 2250
      }
    ],
    "grand_total": 3750
  },
  {
    "store": "Shoprite Lagos",
    "receipt_number": "RCP0000104",
    "created_at": "2026-08-23T09:40",
    "customer_id": "CUS000009",
    "customer_name": "Yusuf Musa",
    "items": [
      {
        "product_id": "PRD000001",
        "name": "Coca-Cola 50cl",
        "price": 550,
        "quantity": 2,
        "subtotal": 1100
      }
    ],
    "grand_total": 1100
  },
  {
    "store": "Shoprite Lagos",
    "receipt_number": "RCP0000105",
    "created_at": "2026-08-23T09:45",
    "customer_id": "CUS000010",
    "customer_name": "Grace Ekanem",
    "items": [
      {
        "product_id": "PRD000012",
        "name": "Mr V permium water 75cl",
        "price": 150.0,
        "quantity": 4,
        "subtotal": 600.0
      }
    ],
    "grand_total": 600.0
  },
  {
    "store": "Shoprite Lagos",
    "receipt_number": "RCP0000106",
    "created_at": "2026-08-23T09:50",
    "customer_id": "CUS000006",
    "customer_name": "Fatima Ibrahim",
    "items": [
      {
        "product_id": "PRD000012",
        "name": "Mr V permium water 75cl",
        "price": 175.0,
        "quantity": 8,
        "subtotal": 1400.0
      }
    ],
    "grand_total": 1400.0
  },
  {
    "store": "Shoprite Lagos",
    "receipt_number": "RCP0000107",
    "created_at": "2026-08-23T09:55",
    "customer_id": "CUS000012",
    "customer_name": "Blessing Ojo",
    "items": [
      {
        "product_id": "PRD000002",
        "name": "Pepsi 50cl",
        "price": 475,
        "quantity": 3,
        "subtotal": 1425
      },
      {
        "product_id": "PRD000004",
        "name": "Maltina 33cl",
        "price": 600,
        "quantity": 5,
        "subtotal": 3000
      }
    ],
    "grand_total": 4425
  },
  {
    "store": "Shoprite Lagos",
    "receipt_number": "RCP0000108",
    "created_at": "2026-08-23T10:00",
    "customer_id": "CUS000013",
    "customer_name": "Michael Adebayo",
    "items": [
      {
        "product_id": "PRD000006",
        "name": "Golden Penny Spaghetti",
        "price": 1200,
        "quantity": 9,
        "subtotal": 10800
      },
      {
        "product_id": "PRD000004",
        "name": "Maltina 33cl",
        "price": 650,
        "quantity": 3,
        "subtotal": 1950
      }
    ],
    "grand_total": 12750
  }
]


print_price_change_analysis(price_change_analysis(price_history_per_product(test_receipts)))

# print_product_sales(best_selling_product(test_receipts))
# print_price_history(price_history_for_product(test_receipts, "prd000004"))
# print_product_sales_revenue(sales_revenue_per_product(test_receipts))