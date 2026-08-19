from utils.product_utils import (
    load_products_json,
    search_low_stock_products
)

products = load_products_json()

low_stock = search_low_stock_products(products)

for product in low_stock:
    print(
        product["name"],
        product["stock_quantity"],
        product["minimum_stock"]
    )