from utils.customer_utils import load_customers_json, update_customer
customers = load_customers_json()

updated_customer = update_customer(
    customers,
    "CUS000005"
)

print(updated_customer)