# Receipt Manager — Day 15 Journal

**Date:** August 13, 2026

## 🎯 Objective

Today I continued expanding the Receipt Manager from a simple receipt CRUD application into a system that can also manage **customers and customer purchase history**.

The main goal was to connect customers to their receipts using a unique `customer_id`.

---

## 1. Customer Data Model

I created a customer structure:

```python
customer = {
    "customer_id": "CUS000001",
    "name": "Ayoola",
    "phone": "08000000000"
}
```

I learned that a customer should have a unique ID that can be used to connect the customer to their receipts.

---

## 2. Connecting Customers to Receipts

I added `customer_id` to the receipt structure:

```python
receipt = {
    "store": store_name,
    "receipt_number": receipt_number,
    "customer_id": customer_id,
    "items": receipt_items,
    "grand_total": grand_total
}
```

This creates a relationship between customers and receipts.

For example:

```text
CUS000001
    │
    ├── RCP0000001
    ├── RCP0000003
    └── RCP0000010
```

One customer can therefore have multiple receipts.

---

## 3. Customer ID Generation

I created `generate_customer_id()` to automatically generate customer IDs.

The idea is similar to my receipt number generator.

For example:

```text
CUS0000001
CUS0000002
CUS0000003
```

The function reads the existing customer JSON file, finds the most recent customer ID, increments the number, and creates the next ID.

---

## 4. Customer JSON Storage

I created functions for storing and loading customers:

```python
save_customer(customer)
load_customers()
```

The customer data is stored in:

```text
data/customers.json
```

This follows the same pattern I previously used for `receipts.json`.

---

## 5. Searching Receipts by Customer

I created:

```python
def search_receipts_by_customer(receipts, customer_id):
```

This function searches through all receipts and returns the receipts belonging to a specific customer.

For example:

```text
CUS000001
    ↓
Search receipts
    ↓
RCP0000001
RCP0000003
```

I tested this using multiple receipts belonging to the same customer.

The result correctly returned:

```text
Found 2 receipts
```

---

## 6. Searching for a Customer

I created:

```python
def search_customer(customers, customer_id):
```

This searches the customer list and returns the matching customer.

If the customer doesn't exist, it returns:

```python
None
```

I learned that returning `None` is useful because the calling function can determine whether the customer was found.

---

## 7. Customer Purchase History

I combined the customer search and receipt search into:

```python
def customer_purchase_history(customers, receipts, customer_id):
```

The function:

1. Searches for the customer.
2. Checks whether the customer exists.
3. Finds all receipts belonging to the customer.
4. Returns the customer and their receipts together.

The returned structure looks like:

```python
{
    "customer": customer,
    "receipts": customer_receipts
}
```

This became the foundation for a customer purchase-history feature.

---

## 8. Customer Analytics

I created several analytics functions:

```python
customer_total_spent()
customer_average_purchase()
customer_largest_purchase()
customer_lowest_purchase()
```

These allow the application to answer questions such as:

* How much has this customer spent?
* What is their average purchase?
* What was their largest purchase?
* What was their smallest purchase?

For example:

```text
Total Receipts:     2
Total Spent:        ₦125,000.00
Average Purchase:   ₦62,500.00
```

---

## 9. Customer Purchase History Display

I created:

```python
def print_customer_purchase_history(history):
```

The function now displays:

### Customer Profile

* Customer ID
* Name
* Phone

### Purchase History

* Receipt Number
* Store
* Receipt Total

### Customer Analytics

* Total Receipts
* Total Spent
* Average Purchase
* Largest Purchase
* Lowest Purchase

This gives me a much more complete view of a customer's activity.

---

## Important Programming Lesson

Today I learned more about **function reuse**.

Instead of calculating the same information repeatedly, I can reuse functions I have already created.

For example:

```python
total_spent = customer_total_spent(receipts)
```

can be used instead of writing the total calculation again.

This makes the code easier to maintain and reduces duplicated logic.

---

## Current Architecture

My project is now moving toward:

```text
Receipt Manager
│
├── Receipts
│   ├── Create
│   ├── Search
│   ├── Update
│   ├── Delete
│   └── Analytics
│
└── Customers
    ├── Customer ID
    ├── Customer Profile
    ├── Purchase History
    └── Customer Analytics
```

The relationship is:

```text
Customer
   │
   │ customer_id
   ↓
Receipts
   │
   ├── Receipt 1
   ├── Receipt 2
   └── Receipt 3
```

---

## Reflection

Today was an important step because the application is no longer only concerned with individual receipts.

I am beginning to think about **relationships between data**.

A receipt belongs to a customer, and multiple receipts can belong to the same customer.

This is the beginning of the CRM part of my larger goal of building an:

**AI-Powered Receipt Management, CRM & Business Analytics Platform.**

---

## Day 15 Completed

* [x] Create customer data model
* [x] Generate customer IDs
* [x] Save customers to JSON
* [x] Load customers from JSON
* [x] Search customer by ID
* [x] Search receipts by customer
* [x] Build customer purchase history
* [x] Calculate total customer spending
* [x] Calculate average purchase
* [x] Find largest purchase
* [x] Find smallest purchase
* [x] Display customer profile
* [x] Display customer purchase history
* [x] Display customer analytics

## Tomorrow — Day 16

I will begin **Customer CRUD**, starting with properly creating and saving customers instead of manually creating customer dictionaries.
