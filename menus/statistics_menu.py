from utils.receipt_utils import load_receipts_json
from utils.analytics import (
    total_receipts,
    total_sales,
    average_receipt,
    largest_receipt,
    smallest_receipt,
    receipts_per_store,
    sales_per_store,
    highest_spending_store,
    lowest_spending_store,
    average_sales_per_store,
    print_a_receipt,
    print_store_count,
    print_store_sales,

    price_history_per_product,
    price_history_for_product,
    print_price_history,
    price_change_analysis,
    print_price_change_analysis,

    products_with_price_decreases,
    products_with_price_increases,
    print_price_changes,

    largest_percentage_decrease,
    largest_percentage_increase,
    print_largest_price_change,
    largest_price_decrease,
    largest_price_increase,

    price_changes_per_product,
    print_price_change_summary,

    units_sold_per_product,
    print_product_sales,
    best_selling_product,
    lowest_selling_product,
    print_selling_product,
    revenue_per_product,
    print_revenue_per_product,
    highest_revenue_products,
    lowest_revenue_products,
    print_highest_revenue_products,
    print_lowest_revenue_products,
    average_price_per_product,
    print_average_price_per_product,

    daily_sales_report,
    print_daily_sales_report,
)

from utils.validation import get_menu_choice
receipts = load_receipts_json()

def statistics_menu(receipts):

    while True:

        print("""
========== STATISTICS ==========

RECEIPT STATISTICS

1. Total Receipts
2. Total Sales
3. Average Receipt
4. Largest Receipt
5. Smallest Receipt

STORE STATISTICS

6. Receipts Per Store
7. Sales Per Store
8. Highest Spending Store
9. Lowest Spending Store
10. Average Sales Per Store

PRODUCT SALES STATISTICS

11. Units Sold Per Product
12. Best-Selling Product
13. Lowest-Selling Product
14. Revenue Per Product
15. Highest-Revenue Products
16. Lowest-Revenue Products
17. Average Selling Price Per Product

PRICE ANALYTICS

18. Price History Per Product
19. Price History For Product
20. Price Changes
21. Largest Price Increase
22. Largest Price Decrease

DATE ANALYTICS

23. Daily Sales Report

24. Back
""")

        choice = get_menu_choice("Choose an option: ")

        if choice == "1":

            total = total_receipts(receipts)

            print(f"\nTotal Receipts: {total}")

        elif choice == "2":

            total = total_sales(receipts)

            print(f"\nTotal Sales: ₦{total:,.2f}")

        elif choice == "3":

            if not receipts:
                print("\nNo receipts available.")
                continue

            average = average_receipt(receipts)

            print(f"\nAverage Receipt: ₦{average:,.2f}")

        elif choice == "4":

            largest = largest_receipt(receipts)

            if largest is None:
                print("\nNo receipts available.")
            else:
                print_a_receipt(
                    largest,
                    title="Largest Receipt"
                )

        elif choice == "5":

            smallest = smallest_receipt(receipts)

            if smallest is None:
                print("\nNo receipts available.")
            else:
                print_a_receipt(
                    smallest,
                    title="Smallest Receipt"
                )

        elif choice == "6":

            store_counts = receipts_per_store(receipts)

            if not store_counts:
                print("\nNo receipts available.")
            else:
                print_store_count(store_counts)

        elif choice == "7":

            store_sales = sales_per_store(receipts)

            if not store_sales:
                print("\nNo receipts available.")
            else:
                print_store_sales(
                    store_sales,
                    title="Sales Per Store"
                )

        elif choice == "8":

            highest = highest_spending_store(receipts)

            if highest is None:
                print("\nNo receipts available.")
            else:
                print_store_sales(
                    highest,
                    title="Highest Spending Store"
                )

        elif choice == "9":

            lowest = lowest_spending_store(receipts)

            if lowest is None:
                print("\nNo receipts available.")
            else:
                print_store_sales(
                    lowest,
                    title="Lowest Spending Store"
                )

        elif choice == "10":

            average_sales = average_sales_per_store(receipts)

            if not average_sales:
                print("\nNo receipts available.")
            else:
                print_store_sales(
                    average_sales,
                    title="Average Sales Per Store"
                )
        elif choice == "11":
            product_sales = units_sold_per_product(receipts)

            if not product_sales:
                print("\nNo product sales found.")
            else:
                print_product_sales(product_sales)

        elif choice == "12":
            product_sales = units_sold_per_product(receipts)

            best = best_selling_product(product_sales)

            print_selling_product(
                best,
                title="Best"
            )

        elif choice == "13":
            product_sales = units_sold_per_product(receipts)

            lowest = lowest_selling_product(product_sales)

            print_selling_product(
                lowest,
                title="Lowest"
            )

        elif choice == "14":
            product_revenue = revenue_per_product(receipts)

            print_revenue_per_product(product_revenue)

        elif choice == "15":
            product_revenue = revenue_per_product(receipts)

            highest = highest_revenue_products(
                product_revenue
            )

            print_highest_revenue_products(highest)

        elif choice == "16":
            product_revenue = revenue_per_product(receipts)

            lowest = lowest_revenue_products(
                product_revenue
            )

            print_lowest_revenue_products(lowest)

        elif choice == "17":
            average_prices = average_price_per_product(
                receipts
            )

            print_average_price_per_product(
                average_prices
            )

        elif choice == "18":

            price_history = price_history_per_product(receipts)

            if not price_history:
                print("\nNo history available.")

            else:
                print_price_history(price_history)

        elif choice == "19":

            product_id = get_menu_choice("Enter product ID: ").strip().upper()

            price_history = price_history_for_product(receipts, product_id)

            if price_history is None:
                print(f"\nNo price history found for {product_id}.")
            else:
                print_price_history(price_history)


        elif choice == "20":

            price_change_reports_menu(receipts)

        elif choice == "21":
            price_history = price_history_per_product(receipts)

            price_changes = price_changes_per_product(
                price_history
            )

            largest = largest_price_increase(
                price_changes
            )

            print_price_change_summary(
                largest,
                "Largest Price Increase"
            )

        elif choice =="22":
            price_history = price_history_per_product(receipts)

            price_changes = price_changes_per_product(
                price_history
            )

            largest = largest_price_decrease(
                price_changes
            )

            print_price_change_summary(
                largest,
                "Largest Price Decrease"
            )

        elif choice == "23":
            report = daily_sales_report(receipts)

            if not report:
                print("\nNo daily sales data available.")
            else:
                print_daily_sales_report(report)
                
        elif choice == "24":

            print("Returning to main menu...")
            break

        else:

            print("Invalid option. Try again.")


def price_change_reports_menu(receipts):

    while True:

        print("""
========== PRICE CHANGE REPORTS ==========

1. All Price Changes
2. Price Increases
3. Price Decreases
4. Largest Price Increase
5. Largest Price Decrease
6. Largest Percentage Increase
7. Largest Percentage Decrease
8. Back
""")

        choice = get_menu_choice("Choose an option: ")

        if choice == "1":

            price_history = price_history_per_product(receipts)
            analysis = price_change_analysis(price_history)

            print_price_change_analysis(analysis)

        elif choice == "2":

            price_history = price_history_per_product(receipts)
            analysis = price_change_analysis(price_history)

            increases = products_with_price_increases(analysis)

            print_price_changes(
                increases,
                "Price Increases"
            )

        elif choice == "3":

            price_history = price_history_per_product(receipts)
            analysis = price_change_analysis(price_history)

            decreases = products_with_price_decreases(analysis)

            print_price_changes(
                decreases,
                "Price Decreases"
            )

        elif choice == "4":

            price_history = price_history_per_product(receipts)
            analysis = price_change_analysis(price_history)

            result = largest_price_increase(analysis)

            print_largest_price_change(
                result,
                "Largest Price Increase"
            )

        elif choice == "5":

            price_history = price_history_per_product(receipts)
            analysis = price_change_analysis(price_history)

            result = largest_price_decrease(analysis)

            print_largest_price_change(
                result,
                "Largest Price Decrease"
            )

        elif choice == "6":

            price_history = price_history_per_product(receipts)
            analysis = price_change_analysis(price_history)

            result = largest_percentage_increase(analysis)

            print_largest_price_change(
                result,
                "Largest Percentage Price Increase"
            )

        elif choice == "7":

            price_history = price_history_per_product(receipts)
            analysis = price_change_analysis(price_history)

            result = largest_percentage_decrease(analysis)

            print_largest_price_change(
                result,
                "Largest Percentage Price Decrease"
            )

        elif choice == "8":

            print("Returning to statistics menu...")
            break

        else:

            print("Invalid option. Try again.")