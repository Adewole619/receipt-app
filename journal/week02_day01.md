# Week 2 – Day 8 Journal

**Date:** 28 July 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Reading and Writing Files

---

# Objectives

Today I wanted to:

- Learn how to save receipt data to a file.
- Learn how to read data from a file.
- Organize my code by separating responsibilities into reusable functions.
- Improve my receipt application to behave more like a real program.

---

# What I Learned

Today I learned how Python can save data permanently using files.

Before today, every receipt disappeared whenever the program closed because everything was stored in memory.

By using file handling, my receipt application can now save receipts to a text file so they can be viewed again later.

---

# File Handling

I learned how to open files using the `with open()` statement.

### Writing to a file

```python
with open("data/receipts.txt", "a") as file:
    file.write("Hello")
```

I learned that:

- `"w"` creates or overwrites a file.
- `"a"` appends new information without deleting existing data.
- `"r"` reads data from a file.

---

# Reading a File

I also learned how to read data back from the file.

```python
with open("data/receipts.txt", "r") as file:
    content = file.read()

print(content)
```

This allowed me to immediately verify that my receipt had been saved correctly.

---

# Improving My Validation

Instead of using `input()` directly everywhere, I created reusable validation functions.

### String Validation

```python
def validate_string_input(field_name):
```

This function:

- Rejects empty input.
- Removes leading and trailing spaces using `strip()`.
- Allows the user to quit by entering `q`.
- Returns a valid string.

---

### Number Validation

```python
def validate_num_input(field_name, num_type):
```

This function:

- Validates both integers and floating-point numbers.
- Rejects invalid input.
- Prevents zero and negative values.
- Returns the correct numeric type.
- Allows the user to quit the program.

Instead of writing separate functions for integers and floats, I learned how to reuse one function by passing either `int` or `float` as an argument.

Example:

```python
validate_num_input("Item quantity", int)
```

```python
validate_num_input("Item price", float)
```

This was one of the biggest lessons of the day because it showed me how functions can become more flexible.

---

# Reusing Functions

My receipt application now uses several reusable functions:

```text
calculate_subtotal()
```

Calculates the subtotal.

---

```text
validate_string_input()
```

Validates text input.

---

```text
validate_num_input()
```

Validates numeric input.

---

```text
save_receipt()
```

Saves the receipt to a text file.

---

```text
print_receipt()
```

Reads the saved receipt file and displays its contents.

Each function now has one clear responsibility.

---

# Refactoring My Code

One of the biggest improvements I made today was moving file handling into reusable functions.

Instead of writing:

```python
with open(...):
```

inside my main program, I created:

```python
def save_receipt(...):
```

and

```python
def print_receipt(...):
```

Now my main program simply calls these functions.

This made my code much shorter, cleaner, and easier to understand.

---

# What I Learned About Code Organization

Today I learned that professional programmers organize programs into small reusable pieces.

Instead of writing one large program, I now have separate functions responsible for:

- Validation
- Calculations
- Saving data
- Displaying data

This makes my application easier to maintain and easier to expand.

---

# Mentor Feedback

Today I received several valuable suggestions.

### What I did well

- Imported reusable functions instead of copying code.
- Used dictionaries to store receipt items.
- Used `enumerate()` to number receipt items.
- Separated file handling into reusable functions.
- Used file append mode to preserve previous receipts.
- Read the saved receipt back from the file.

### Improvements Suggested

I learned that Python function parameters should normally use **snake_case** instead of capitalized names.

Example:

Instead of:

```python
File_name
```

I should write:

```python
file_name
```

I also learned that future improvements could include handling missing files using exception handling and returning data from functions instead of printing it directly.

---

# Challenges I Faced

The biggest challenge today was deciding how to organize my growing application.

As the project became larger, I realized that putting everything inside one file would make it difficult to manage.

Creating reusable functions helped solve this problem.

---

# How I Solved It

I created reusable utility functions and moved them into my `utils` package.

This allowed my main program to focus on controlling the application's workflow while the utility functions handled individual tasks.

---

# Key Concepts I Remember

- File handling allows data to be stored permanently.
- `"w"` overwrites files.
- `"a"` appends to files.
- `"r"` reads files.
- `with open()` automatically closes files.
- Functions should have one responsibility.
- Validation should be reusable.
- Dictionaries keep related information together.
- Refactoring improves readability and maintainability.

---

# What I Enjoyed

Today I enjoyed reorganizing my receipt application.

Seeing my code become shorter and more readable after moving repeated logic into reusable functions made me feel like I was building software the way professional developers do.

---

# What I Found Difficult

The most difficult part was deciding how to separate responsibilities between my main program and my utility functions.

After experimenting with different approaches, I learned that reusable functions make the application much cleaner.

---

# Reflection

Today was one of the most important days of my learning journey.

My receipt application no longer feels like a collection of programming exercises.

It is beginning to look like a real software project with reusable functions, better organization, input validation, and persistent file storage.

I also learned that good software is not only about producing the correct output—it is also about writing code that is easy to understand, reuse, and improve.

---

# Commands I Used Today

```bash
python3 lessons/day08.py
python3 practice/practice_day08.py
python3 challenges/challenge_day08.py

git add .
git commit -m "Week 2 Day 8: Added file handling and reusable utility functions"
git push
```

---

# Vocabulary

| Term | Meaning |
|------|---------|
| File Handling | Reading from and writing data to files. |
| Append Mode (`a`) | Adds new data to the end of a file without removing existing data. |
| Read Mode (`r`) | Opens a file for reading. |
| Write Mode (`w`) | Creates or overwrites a file. |
| Refactoring | Improving the structure of existing code without changing its behavior. |
| Reusability | Writing code once so it can be used in many places. |
| Dictionary | A collection of key-value pairs used to store related information. |
| `enumerate()` | Returns both the index and the value while looping through a collection. |
| `with open()` | Opens a file and automatically closes it when finished. |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐⭐☆ (4/5)

**Confidence:** ⭐⭐⭐⭐⭐ (5/5)

---

# Progress Summary

✅ Learned file handling

✅ Saved receipts to a text file

✅ Read receipts from a text file

✅ Built reusable validation functions

✅ Refactored file handling into reusable functions

✅ Improved project organization

✅ Continued building a more realistic receipt management application

---

# End of Week 2 – Day 8

Today my receipt application reached another important milestone. It now stores receipt data permanently, reads saved receipts, validates user input through reusable functions, and uses a cleaner project structure. I can see how each improvement builds toward creating a complete receipt management system.

# Week 2 – Day 9 Journal

**Date:** July 29, 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Working with JSON (JavaScript Object Notation)

---

# Objectives

Today I wanted to:

* Learn how to store receipt data using JSON.
* Automatically generate unique receipt numbers.
* Save multiple receipts in a structured format.
* Load receipts back into my program.
* Continue improving the architecture of my receipt manager.

---

# What I Learned

Today I learned that although text files are easy for people to read, they are not the best format for applications that need to search, update, or delete data.

JSON stores information in a structured way that Python can easily understand. It is very similar to Python dictionaries, making it an excellent choice before moving to SQLite.

---

# Understanding JSON

I learned about Python's built-in `json` module.

The four most important functions are:

* `json.dump()` – Writes Python objects directly to a JSON file.
* `json.dumps()` – Converts a Python object into a JSON string.
* `json.load()` – Reads JSON from a file and converts it into a Python object.
* `json.loads()` – Converts a JSON string into a Python object.

---

# Automatic Receipt Numbers

One of the biggest improvements I made today was removing manual receipt number entry.

Instead of asking the user to type a receipt number, my application now generates one automatically.

Example:

```text
RCP0000001
RCP0000002
RCP0000003
```

I created a reusable function:

```python
generate_receipt_number()
```

This function:

* Checks whether the JSON file exists.
* Starts from `RCP0000001` if no receipts have been saved.
* Reads the last saved receipt.
* Extracts the numeric part.
* Increments it by one.
* Formats it with leading zeros.

This makes the receipt numbers unique, consistent, and easier to manage.

---

# Saving Receipts as JSON

Instead of saving formatted text, I now save each receipt as a dictionary.

Each receipt contains:

* Store name
* Receipt number
* Receipt items
* Grand total

Each receipt is added to a list of receipts before being written back to `receipts.json`.

My save process became:

```text
Load Existing Receipts
        ↓
Append New Receipt
        ↓
Save Updated List
```

This was one of the most important concepts I learned today.

---

# Loading Receipts

I created:

```python
load_receipts_json()
```

This function:

* Opens the JSON file.
* Reads all saved receipts.
* Returns them as a Python list.

If the file does not exist, it safely returns an empty list instead of crashing.

---

# Error Handling

I learned that programs should expect things to go wrong.

My functions now handle situations where:

* The JSON file does not exist.
* The JSON file is empty.
* The JSON file contains invalid JSON.

Instead of crashing, the program recovers and continues running.

---

# Improving My Project Structure

My project is becoming more organized.

Current structure:

```text
receipt-app/
│
├── main.py
│
├── utils/
│   └── receipt_utils.py
│
├── data/
│   └── receipts.json
│
├── journal/
│
└── README.md
```

Most of my reusable logic now lives inside `receipt_utils.py`.

---

# Functions Added Today

Today I created:

* `generate_receipt_number()`
* `save_receipt_json()`
* `load_receipts_json()`

These functions made my application much cleaner and easier to maintain.

---

# Mentor Feedback

Today I received several suggestions for improving my code.

### What I did well

* Automatically generated receipt numbers.
* Used JSON instead of plain text.
* Stored multiple receipts in one file.
* Used reusable functions.
* Handled missing files.
* Handled invalid JSON.
* Continued separating responsibilities.

### Improvements Suggested

I learned that:

* The JSON key should be `"items"` instead of `"item"` because each receipt contains multiple items.
* I should consistently use my `RECEIPT_FILE_JSON` constant instead of hardcoding the file path.
* In the future, I can pass the entire receipt dictionary into `save_receipt_json()` instead of passing multiple parameters.

These suggestions will make my code even cleaner as the project grows.

---

# Challenges I Faced

The biggest challenge today was understanding how to store multiple receipts without overwriting previous data.

I learned that the correct process is:

1. Load existing receipts.
2. Append the new receipt.
3. Save the updated list back to the JSON file.

---

# How I Solved It

I used:

```python
json.load()
```

to read the existing receipts into a list.

Then I added the new receipt using:

```python
append()
```

Finally, I used:

```python
json.dump()
```

to save the updated list back into the file.

---

# Key Concepts I Remember

* JSON stores structured data.
* Python dictionaries map naturally to JSON objects.
* Lists of dictionaries are useful for storing multiple records.
* `json.dump()` writes to a file.
* `json.load()` reads from a file.
* Automatic receipt numbers improve consistency.
* Functions should each have one responsibility.
* Error handling makes applications more reliable.

---

# What I Enjoyed

I enjoyed implementing automatic receipt number generation.

Seeing receipt numbers increase automatically made my receipt manager feel much more like a real business application.

I also enjoyed seeing how JSON organizes data in a way that is much easier for programs to process.

---

# What I Found Difficult

The most challenging part was understanding how to update a JSON file without losing the previous receipts.

Once I understood the **Load → Append → Save** workflow, the process became much clearer.

---

# Reflection

Today was another important milestone in my Python journey.

My receipt manager has moved beyond storing plain text and now stores structured data using JSON.

I also learned how to generate unique receipt numbers automatically, making the application more realistic and reducing the chance of duplicate receipt numbers.

Each day my project becomes cleaner, more organized, and closer to the type of applications used in the real world.

---

# Commands I Used Today

```bash
python3 lessons/day09.py
python3 practice/practice_day09.py
python3 challenges/challenge_day09.py

git add .
git commit -m "Week 2 Day 9: Added JSON storage and automatic receipt number generation"
git push
```

---

# Vocabulary

| Term                  | Meaning                                                        |
| --------------------- | -------------------------------------------------------------- |
| JSON                  | A structured text format used to store and exchange data.      |
| `json.dump()`         | Writes a Python object to a JSON file.                         |
| `json.load()`         | Reads a JSON file into a Python object.                        |
| Dictionary            | A collection of key-value pairs.                               |
| List                  | An ordered collection of values.                               |
| Exception Handling    | Writing code to deal with errors without crashing the program. |
| Refactoring           | Improving code structure without changing its behavior.        |
| Sequential Identifier | A unique number that increases in order, such as `RCP0000001`. |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐⭐☆ (4/5)

**Confidence:** ⭐⭐⭐⭐⭐ (5/5)

---

# Progress Summary

* ✅ Learned JSON fundamentals
* ✅ Stored multiple receipts in a JSON file
* ✅ Automatically generated receipt numbers
* ✅ Loaded receipts from JSON
* ✅ Improved error handling
* ✅ Continued refactoring the project into reusable functions
* ✅ Prepared the project for searching, updating, deleting, and future SQLite integration

---

# End of Week 2 – Day 9

Today my receipt manager became much more like a real application. Instead of storing plain text, it now stores structured JSON data, generates receipt numbers automatically, and safely manages multiple receipts. This lays a strong foundation for implementing search, update, delete, reporting, and eventually migrating the application to SQLite.

# Week 2 – Day 10 Journal

**Date:** July 30, 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Searching Receipts (Read Operation - CRUD)

---

# Objectives

Today I wanted to:

* Learn how to search receipts stored in a JSON file.
* Search receipts by receipt number.
* Search receipts by store name.
* Separate user interface code from business logic.
* Write reusable search functions.

---

# What I Learned

Today I learned that saving data is only one part of an application. A useful application must also allow users to find previously saved information quickly.

I implemented the **Read (R)** operation of CRUD by adding search functionality to my receipt manager.

---

# Search by Receipt Number

I created a reusable function:

```python
def search_by_receipt_number(rcp_number):
```

This function:

* Loads all receipts from `receipts.json`.
* Accepts a receipt number as a parameter.
* Searches every receipt.
* Returns the matching receipt if found.
* Returns `None` if no receipt exists.

I also learned that receipt numbers are unique, so once a match is found, the function can immediately return the receipt.

---

# Search by Store Name

I also created:

```python
def search_by_store(st_name):
```

Unlike receipt numbers, a store can have many receipts.

For this reason, I created an empty list:

```python
rcp_receipts = []
```

Every matching receipt is added to the list using:

```python
rcp_receipts.append(rcp)
```

The function finally returns the complete list of matching receipts.

---

# Understanding Return Values

One of the biggest lessons today was understanding that different functions may return different kinds of data.

### `search_by_receipt_number()`

Returns:

* One receipt dictionary
* Or `None`

### `search_by_store()`

Returns:

* A list of receipt dictionaries
* Or an empty list (`[]`) when nothing is found

This made me understand when to return a single object and when to return a collection.

---

# Separating Responsibilities

Earlier, my search functions asked the user for input and printed results.

Today I refactored them so they only perform the search.

Now the menu:

* Gets user input.
* Calls the search function.
* Displays the result.

The search functions simply return data.

This follows the **Single Responsibility Principle**, making the code easier to reuse and maintain.

---

# Improving My Menu

I created a simple search menu that allows users to:

```text
1. Search by Receipt Number
2. Search by Store
3. Exit
```

The menu now calls the appropriate search function and displays the results.

---

# Testing My Functions

I learned that functions can be tested without rewriting the entire application.

I tested:

* Searching for an existing receipt number.
* Searching for a receipt number that does not exist.
* Searching for an existing store.
* Searching for a store with multiple receipts.
* Searching using uppercase, lowercase, and mixed-case letters.
* Exiting the search menu.

---

# Mentor Feedback

Today I received useful feedback that improved my code.

### Improvements I Made

* Removed `input()` from my search functions.
* Removed printing from the search functions.
* Passed parameters into the functions instead.
* Returned search results instead of displaying them immediately.
* Used a list to collect multiple store receipts.

These changes made my code much more reusable.

---

# Challenges I Faced

At first, I made `search_by_store()` return only the first matching receipt.

After reviewing the logic, I realized that one store can have many receipts.

I fixed the problem by storing every matching receipt in a list and returning that list.

---

# How I Solved It

I used:

```python
rcp_receipts = []
```

Then:

```python
rcp_receipts.append(rcp)
```

Finally:

```python
return rcp_receipts
```

This allowed the function to return all matching receipts instead of just one.

---

# Key Concepts I Remember

* CRUD stands for Create, Read, Update, and Delete.
* Searching by receipt number returns one receipt.
* Searching by store returns many receipts.
* Functions should accept parameters instead of calling `input()`.
* Functions should return data instead of printing whenever possible.
* Lists are useful for collecting multiple results.
* Separating business logic from user interface makes code cleaner and easier to reuse.

---

# What I Enjoyed

I enjoyed refactoring my code into reusable functions.

It made the program easier to read and gave me a better understanding of how larger software projects are organized.

---

# What I Found Difficult

The most difficult part was understanding why `search_by_store()` should return a list while `search_by_receipt_number()` returns only one receipt.

After working through examples, I now understand the difference.

---

# Reflection

Today was an important step in my programming journey.

I moved beyond simply writing code that works and started writing code that is reusable and well organized.

I now understand why functions should have a single responsibility and how separating user interaction from business logic makes an application easier to maintain.

---

# Commands I Used Today

```bash
python3 practice/practice_day10.py

git add .
git commit -m "Week 2 Day 10: Added receipt search functionality"
git push
```

---

# Vocabulary

| Term                            | Meaning                                      |
| ------------------------------- | -------------------------------------------- |
| CRUD                            | Create, Read, Update, Delete                 |
| Search                          | Finding information based on a condition     |
| Return Value                    | The data a function sends back to its caller |
| Parameter                       | A value passed into a function               |
| List                            | A collection that can store multiple values  |
| Dictionary                      | A collection of key-value pairs              |
| Refactoring                     | Improving code without changing its behavior |
| Single Responsibility Principle | A function should perform one task well      |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐⭐☆ (4/5)

**Confidence:** ⭐⭐⭐⭐⭐ (5/5)

---

# Progress Summary

* ✅ Completed the **Read (Search)** operation of CRUD.
* ✅ Added search by receipt number.
* ✅ Added search by store.
* ✅ Returned data from functions instead of printing.
* ✅ Separated business logic from user interaction.
* ✅ Improved code organization and reusability.

---

# End of Week 2 – Day 10

Today I transformed my receipt manager into a more complete application by implementing search functionality. I learned how to design reusable functions, return meaningful results, and organize my code more professionally. My application can now create and read receipts, providing a strong foundation for implementing Update and Delete in the coming days.


# Week 2 – Day 11 Journal

**Date:** August 4, 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Update Receipts (Update - CRUD)

---

# Objectives

Today I wanted to:

* Learn how to update an existing receipt.
* Understand the update workflow.
* Reuse previously written functions.
* Save updated data back to the JSON file.
* Improve my understanding of mutable objects in Python.

---

# What I Learned

Today I implemented the **Update (U)** operation of CRUD.

Instead of creating a new receipt every time, my application can now locate an existing receipt using its unique receipt number and update its store name.

I also learned that updating data follows a simple workflow:

```text
Load Receipts
      │
      ▼
Search Receipt
      │
      ▼
Modify Data
      │
      ▼
Save Updated List
```

This pattern is common in many applications that work with files or databases.

---

# Reusing Existing Functions

One of the biggest lessons today was learning to reuse code instead of rewriting it.

I reused:

* `load_receipts_json()`
* `search_by_receipt_number()`

Instead of writing another search loop inside `update_receipt()`.

This made my code shorter, cleaner, and easier to maintain.

---

# Loading Data Only Once

Originally, my code loaded the JSON file twice:

```text
update_receipt()

↓

load_receipts_json()

↓

search_by_receipt_number()

↓

load_receipts_json()
```

I learned this was unnecessary.

I improved my design by passing the loaded receipts into my search function.

```python
receipt = search_by_receipt_number(receipts, rcp_number)
```

Now the JSON file is loaded only once.

---

# Mutable Objects

Today I learned an important Python concept.

Lists and dictionaries are **mutable objects**.

When I updated:

```python
receipt["store"] = new_rcp_store_name
```

I wasn't creating a new receipt.

I was modifying the existing dictionary that already existed inside the `receipts` list.

Because dictionaries are mutable, the change automatically appeared inside the list.

---

# Input Validation

I prevented users from saving an empty store name.

```python
if not new_rcp_store_name:
    print("Store name cannot be empty.")
    return
```

This ensures invalid data is not written to the JSON file.

---

# Creating `save_all_receipts()`

Previously, I wrote JSON-saving code directly inside my update function.

Today I created a reusable helper:

```python
def save_all_receipts(receipts):
```

Its only responsibility is to save the updated list back into `receipts.json`.

This follows the **Single Responsibility Principle**.

---

# Understanding Function Parameters

Today I asked whether I could use:

```python
def search_by_receipt_number(rcp_number, receipts=load_receipts_json()):
```

I learned that default parameter values are evaluated only once when Python defines the function, not every time the function is called.

Instead, I learned the better pattern:

```python
def search_by_receipt_number(rcp_number, receipts=None):
```

or passing the already-loaded receipts into the function.

This was one of my biggest lessons today.

---

# Challenges I Faced

At first, I tried to access receipts like this:

```python
receipts[rcp_number]
```

I learned this was incorrect because:

* `receipts` is a list.
* Lists use integer indexes.
* Receipt numbers are strings like `"RCP0000007"`.

The correct approach is to search the list until the matching receipt number is found.

---

# Mentor Feedback

Today I received helpful feedback about software design.

I learned that professional code should avoid:

* Loading the same file multiple times.
* Repeating the same code.
* Giving one function too many responsibilities.

Instead, functions should do one job well.

---

# Key Concepts I Remember

* CRUD = Create, Read, Update, Delete.
* Receipt numbers uniquely identify receipts.
* Lists contain multiple receipts.
* Each receipt is a dictionary.
* Dictionaries are mutable.
* Load data once whenever possible.
* Reuse existing functions.
* Validate user input before saving.
* Save the updated list after making changes.

---

# Reflection

Today helped me move beyond writing code that simply works.

I started thinking more about software design and efficiency.

I now understand why reusable functions, single responsibilities, and passing data between functions make programs cleaner and easier to maintain.

I also realized that understanding how lists and dictionaries work together is essential when working with JSON data.

---

# Commands Used Today

```bash
python3 practice/practice_day11.py

git add .
git git
git push
```

---

# Vocabulary

| Term                            | Meaning                                      |
| ------------------------------- | -------------------------------------------- |
| Update                          | Modifying existing data                      |
| Mutable                         | An object whose contents can be changed      |
| Dictionary                      | A collection of key-value pairs              |
| List                            | An ordered collection of items               |
| Parameter                       | A value passed into a function               |
| JSON                            | A text format used to store structured data  |
| Single Responsibility Principle | A function should perform one task well      |
| Refactoring                     | Improving code without changing its behavior |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐⭐☆ (4/5)

**Confidence:** ⭐⭐⭐⭐⭐ (5/5)

---

# Progress Summary

* ✅ Completed the **Update (U)** operation of CRUD.
* ✅ Reused search functions instead of duplicating code.
* ✅ Loaded JSON data only once.
* ✅ Updated a receipt's store name.
* ✅ Added validation for empty store names.
* ✅ Created a reusable `save_all_receipts()` function.
* ✅ Improved my understanding of mutable objects and function design.

---

# End of Week 2 – Day 11

Today I successfully implemented the Update feature of my Receipt Manager application. More importantly, I learned how to design reusable functions, avoid unnecessary work, and organize my code into clear responsibilities. My application now supports Create, Read, and Update operations, and I am ready to implement Delete to complete the CRUD cycle.

# Receipt Manager Project – Day 12 Journal

**Date:** August 6, 2026

---

# Objective

Today's goal was to complete the **receipt deletion functionality** and improve the way users select receipts from search results.

I also focused on making the deletion process safer because deleting a receipt is a permanent operation.

---

# What I Built

Today I worked on:

* Deleting receipts by receipt number.
* Searching for receipts before deletion.
* Confirming deletion with the user.
* Saving the updated receipt list back to JSON.
* Creating a reusable receipt-selection system.
* Assigning temporary display numbers to search results.
* Separating menu logic from business logic.

---

# 1. Deleting a Receipt

I created a `delete_receipt()` function that searches for a receipt first.

The basic process is:

```text
Receipt Number
      ↓
Search for Receipt
      ↓
Receipt Found?
   ↙       ↘
 No         Yes
 ↓           ↓
Stop     Display Receipt
             ↓
       Confirm Deletion
          ↙       ↘
        No         Yes
        ↓           ↓
      Cancel     Remove
                    ↓
              Save JSON
```

This taught me that deletion should not happen immediately after receiving the receipt number.

The program should first make sure the receipt exists and then ask the user for confirmation.

---

# 2. Using `remove()`

I learned how Python's list `.remove()` method can remove an object from a list.

For example:

```python
receipts.remove(receipt)
```

The `receipt` dictionary returned from the search is removed from the `receipts` list.

I also learned why deletion needs to be handled carefully:

> Once the receipt is removed and the updated list is saved, it cannot easily be restored.

Because of this, confirmation is important.

---

# 3. Confirming Permanent Deletion

Before deleting a receipt, I display the receipt and ask the user:

```text
Permanently deleted receipts cannot be restored.
Type Yes to delete or No to cancel:
```

The receipt is only deleted when the user enters:

```text
Yes
```

If the user enters:

```text
No
```

the deletion is cancelled.

This is an example of adding a safety mechanism to a destructive operation.

---

# 4. Saving the Updated Receipt List

After deleting the receipt:

```python
receipts.remove(receipt)
```

the list in memory has changed.

Therefore, I save the entire updated list back to the JSON file.

The process is:

```text
JSON file
   ↓
load_receipts_json()
   ↓
List of dictionaries in memory
   ↓
Remove receipt
   ↓
Updated list
   ↓
save_all_receipts()
   ↓
JSON file
```

I learned that the JSON file needs to represent the current state of the list in memory.

---

# 5. Searching by Store and Selecting a Receipt

I improved the delete menu so that a user can search by store.

For example:

```text
Search by Store
      ↓
Shoprite
      ↓
Multiple receipts found
      ↓
Display numbered results
```

Instead of forcing the user to type a long receipt number, I created temporary display numbers.

For example:

```text
Selection [1]
Receipt: RCP0000001

Selection [2]
Receipt: RCP0000027

Selection [3]
Receipt: RCP0000145
```

The user can simply select:

```text
2
```

and the program knows that this corresponds to the second receipt in the search results.

---

# 6. Creating `print_receipt_list()`

I created a reusable function:

```python
def print_receipt_list(receipts):
    for i, receipt in enumerate(receipts, start=1):
        print(f"Selection [{i}]")
        print_receipt_out(receipt)
```

This separates the responsibility of displaying a list of receipts from the menu logic.

---

# 7. Creating `choose_receipt()`

I also created:

```python
def choose_receipt(receipts):
```

This function handles selecting a receipt from a list.

The user enters a display number and the function returns the corresponding receipt.

For example:

```text
Selection [1] → RCP0000001
Selection [2] → RCP0000008
Selection [3] → RCP0000015
```

If the user enters:

```text
2
```

the function returns:

```text
RCP0000008
```

The display number is only a temporary position in the search results. It does not replace the actual receipt number.

---

# Key Concept

One of the most important things I learned today is the difference between:

### Display number

```text
2
```

and:

### Receipt number

```text
RCP0000008
```

The display number is temporary and only exists to make selection easier.

The receipt number is the permanent unique identifier of the receipt.

---

# Code Organization

I continued separating my application into smaller functions.

Instead of putting everything inside one large menu, I now have separate responsibilities:

```text
main_menu()
    ↓
delete_menu()
    ↓
delete_by_receipt_number()
    ↓
delete_receipt()
```

I also have reusable functions such as:

```text
search_by_receipt_number()
search_by_store()
print_receipt_out()
print_receipt_list()
choose_receipt()
save_all_receipts()
```

This makes the application easier to understand and maintain.

---

# What I Learned

Today I reinforced:

* Python lists.
* `.remove()`.
* Searching lists of dictionaries.
* Returning objects from functions.
* Confirmation before destructive operations.
* Saving modified data back to JSON.
* Temporary display numbers.
* Function decomposition.
* Separating menu logic from application logic.
* Reusing functions.

---

# Reflection

Today I started thinking more about the **user experience** of the application.

Typing a long receipt number is not always convenient, especially when many receipts are stored.

The temporary display-number system provides a better experience:

```text
Search results
      ↓
1. Receipt A
2. Receipt B
3. Receipt C
      ↓
User selects 2
      ↓
Application identifies Receipt B
```

I also learned that deleting data requires more care than simply removing an item from a list. The program needs to confirm the user's intention and then persist the changed state.

---

# Project Progress

My Receipt Manager now supports:

* ✅ Create receipts
* ✅ Auto-generated receipt numbers
* ✅ JSON storage
* ✅ Load receipts
* ✅ Search by receipt number
* ✅ Search by store
* ✅ Update receipts
* ✅ Delete receipts
* ✅ Confirmation before deletion
* ✅ Reusable menus
* ✅ Receipt selection using display numbers

The project is becoming a proper CRUD application with the beginnings of a business analytics system.

---

# Tomorrow's Direction

The next stage is to build more useful **business statistics and analytics** from the receipt data.

I want the system to answer questions such as:

* How many receipts exist?
* How much have we sold?
* What is the average receipt value?
* Which receipt is the largest?
* Which receipt is the smallest?
* How many receipts does each store have?
* Which store generates the most sales?

This will begin moving the project from a simple receipt manager toward a **business analytics platform**.


# Receipt Manager Project – Day 13 Journal

**Date:** August 7, 2026

---

# Objective

Today's goal was to transform my receipt manager from a CRUD application into a simple business reporting system by adding statistics and analytics.

Instead of only storing receipts, I learned how to analyze the stored data and present meaningful information to the user.

---

# What I Built

Today I implemented a Statistics module that can:

* Count the total number of receipts.
* Calculate total sales.
* Calculate the average receipt value.
* Find the largest receipt.
* Find the smallest receipt.
* Count how many receipts belong to each store.
* Display all statistics through a dedicated statistics menu.

---

# What I Learned

## 1. Counting Data

I used Python's `len()` function to determine how many receipts have been stored.

```python
def total_receipts(receipts):
    return len(receipts)
```

This taught me that counting records is one of the simplest forms of business analytics.

---

## 2. Calculating Total Sales

I looped through every receipt and added each receipt's `grand_total`.

```python
total_sales += receipt.get("grand_total", 0)
```

Using `.get()` makes the program safer because it provides a default value if the key is missing.

---

## 3. Reusing Existing Functions

Instead of recalculating everything inside `average_receipt()`, I reused my existing functions.

```python
average = total_sales(receipts) / total_receipts(receipts)
```

This reminded me that reusable functions make programs cleaner and easier to maintain.

---

## 4. Finding the Largest and Smallest Receipt

I learned how to compare dictionaries by their values.

I started with the first receipt and compared every other receipt against it.

```python
largest = receipts[0]
```

and

```python
smallest = receipts[0]
```

This helped me understand comparison algorithms without relying on Python's built-in `max()` or `min()` functions.

---

## 5. Counting Receipts Per Store

I created a dictionary that keeps track of how many receipts belong to each store.

```python
store_counts[store] = store_counts.get(store, 0) + 1
```

This introduced me to grouping and counting data, which is commonly used in reporting systems.

---

## 6. Building a Statistics Menu

I created a separate menu dedicated to business reports.

Each menu option calls its own function, making the code organized and easy to extend.

This reinforced the importance of separating responsibilities into small, focused functions.

---

# Challenges

One challenge I discovered is that some functions can fail if the receipt list is empty.

For example:

* Calculating an average when there are no receipts causes a division by zero.
* Accessing `receipts[0]` fails if the list is empty.

I learned that defensive programming and validating data before processing it are important for building reliable software.

---

# Key Takeaways

Today I learned that software is not only about storing information—it is also about extracting useful information from data.

I also reinforced several software engineering principles:

* Write small functions with one responsibility.
* Reuse existing functions whenever possible.
* Separate business logic from menu logic.
* Think about error handling before users encounter problems.
* Design code so that it can easily support future features.

---

# Reflection

Today's lesson made my receipt manager feel much more like a real business application. Instead of simply recording receipts, it can now provide useful insights such as total sales, average receipt value, and store summaries.

I also realized that analytics is the foundation for future dashboards and AI-powered reporting. The work I completed today is another step toward building a professional receipt management platform that can eventually support CRM, business intelligence, and AI features.

---

# Tomorrow's Goal

Tomorrow I will continue improving the application by adding more advanced reporting features, strengthening error handling, and making the code even more modular and reusable.

# Receipt Manager Project – Day 14 Journal

**Date:** August 8, 2026

---

# Objective

Today's goal was to expand the statistics functionality of my Receipt Manager.

Yesterday, I calculated general receipt statistics such as total receipts, total sales, average receipt, largest receipt, smallest receipt, and receipts per store.

Today, I focused on **store-level sales analytics**.

---

# What I Built

Today I implemented functions to:

* Calculate total sales per store.
* Find the highest-spending store.
* Find the lowest-spending store.
* Calculate the average sales per receipt for each store.
* Reuse existing statistics functions instead of duplicating logic.

---

# What I Learned

## 1. Calculating Sales Per Store

I created:

```python
def sales_per_store(receipts):
```

This function groups receipts by store and adds the `grand_total` of each receipt.

For example:

```python
{
    "Shoprite": 30000,
    "Spar": 20000
}
```

This means Shoprite generated ₦30,000 and Spar generated ₦20,000 from the stored receipts.

I reused the dictionary `.get()` pattern:

```python
store_sales[store] = store_sales.get(store, 0) + receipt.get("grand_total", 0)
```

This allowed me to create the store automatically when it does not already exist.

---

# 2. Finding the Highest-Spending Store

I created:

```python
def highest_spending_store(receipts):
```

First, I calculated the sales for every store.

Then I used:

```python
max(store_sales, key=store_sales.get)
```

This allowed Python to find the store with the highest sales value.

---

# 3. Finding the Lowest-Spending Store

I created:

```python
def lowest_spending_store(receipts):
```

This uses:

```python
min(store_sales, key=store_sales.get)
```

to find the store with the lowest total sales.

This helped me understand how `max()` and `min()` can work with dictionaries.

---

# 4. Average Sales Per Store

I created:

```python
def average_sales_per_store(receipts):
```

The calculation is:

```text
Store's Total Sales
-------------------
Number of Store Receipts
```

For example, if Shoprite has:

```text
Total sales: ₦30,000
Receipts: 3
```

then:

```text
₦30,000 ÷ 3 = ₦10,000
```

So the average sale per receipt for Shoprite is ₦10,000.

---

# 5. Reusing Existing Functions

One of the most important things I learned today was that I don't need to repeat calculations.

My `average_sales_per_store()` function reuses:

```python
sales_per_store(receipts)
```

and:

```python
receipts_per_store(receipts)
```

This gives me:

```text
Sales per store
+
Number of receipts per store
        ↓
Average sales per store
```

This makes my code easier to maintain.

---

# 6. Handling Empty Data

I added a check:

```python
if not store_sales:
    return None
```

This prevents the program from trying to calculate statistics when there are no receipts.

I also learned that functions using `max()`, `min()`, or `receipts[0]` need to consider the possibility of an empty list or dictionary.

---

# Key Takeaways

Today I learned about:

* Data aggregation.
* Grouping data by store.
* Dictionary `.get()`.
* `max()` with a dictionary.
* `min()` with a dictionary.
* Average calculations.
* Reusing existing functions.
* Handling empty datasets.
* Building business-level statistics from receipt data.

---

# Business Analytics

Today's work is starting to make the Receipt Manager more useful as a business analytics system.

The application can now answer questions such as:

```text
How many receipts do we have?

How much money was generated?

How much did each store generate?

Which store generated the most money?

Which store generated the least?

What is the average sale per receipt for each store?
```

These are examples of information that can eventually be displayed in a business dashboard.

---

# Reflection

Today's lesson helped me understand that the value of a receipt management system is not only in storing receipts.

The stored receipts can be transformed into useful business information.

I also noticed that my functions are becoming more reusable. Instead of creating each statistic from scratch, I can build new statistics using functions I already created.

This is making the project more modular and closer to the architecture of a real application.

---

# Tomorrow's Goal

Tomorrow I will continue improving the analytics functionality and begin thinking about how customers and businesses can be represented in the system.

I also want to start considering how the current JSON-based structure could eventually evolve into a proper database structure for the larger Receipt Management, CRM, and Business Analytics platform.


# Receipt Manager Project – Day 14 Journal

**Date:** August 8, 2026

---

# Objective

Today's goal was to expand the statistics functionality of my Receipt Manager.

Yesterday, I calculated general receipt statistics such as total receipts, total sales, average receipt, largest receipt, smallest receipt, and receipts per store.

Today, I focused on **store-level sales analytics**.

---

# What I Built

Today I implemented functions to:

* Calculate total sales per store.
* Find the highest-spending store.
* Find the lowest-spending store.
* Calculate the average sales per receipt for each store.
* Reuse existing statistics functions instead of duplicating logic.

---

# What I Learned

## 1. Calculating Sales Per Store

I created:

```python
def sales_per_store(receipts):
```

This function groups receipts by store and adds the `grand_total` of each receipt.

For example:

```python
{
    "Shoprite": 30000,
    "Spar": 20000
}
```

This means Shoprite generated ₦30,000 and Spar generated ₦20,000 from the stored receipts.

I reused the dictionary `.get()` pattern:

```python
store_sales[store] = store_sales.get(store, 0) + receipt.get("grand_total", 0)
```

This allowed me to create the store automatically when it does not already exist.

---

# 2. Finding the Highest-Spending Store

I created:

```python
def highest_spending_store(receipts):
```

First, I calculated the sales for every store.

Then I used:

```python
max(store_sales, key=store_sales.get)
```

This allowed Python to find the store with the highest sales value.

---

# 3. Finding the Lowest-Spending Store

I created:

```python
def lowest_spending_store(receipts):
```

This uses:

```python
min(store_sales, key=store_sales.get)
```

to find the store with the lowest total sales.

This helped me understand how `max()` and `min()` can work with dictionaries.

---

# 4. Average Sales Per Store

I created:

```python
def average_sales_per_store(receipts):
```

The calculation is:

```text
Store's Total Sales
-------------------
Number of Store Receipts
```

For example, if Shoprite has:

```text
Total sales: ₦30,000
Receipts: 3
```

then:

```text
₦30,000 ÷ 3 = ₦10,000
```

So the average sale per receipt for Shoprite is ₦10,000.

---

# 5. Reusing Existing Functions

One of the most important things I learned today was that I don't need to repeat calculations.

My `average_sales_per_store()` function reuses:

```python
sales_per_store(receipts)
```

and:

```python
receipts_per_store(receipts)
```

This gives me:

```text
Sales per store
+
Number of receipts per store
        ↓
Average sales per store
```

This makes my code easier to maintain.

---

# 6. Handling Empty Data

I added a check:

```python
if not store_sales:
    return None
```

This prevents the program from trying to calculate statistics when there are no receipts.

I also learned that functions using `max()`, `min()`, or `receipts[0]` need to consider the possibility of an empty list or dictionary.

---

# Key Takeaways

Today I learned about:

* Data aggregation.
* Grouping data by store.
* Dictionary `.get()`.
* `max()` with a dictionary.
* `min()` with a dictionary.
* Average calculations.
* Reusing existing functions.
* Handling empty datasets.
* Building business-level statistics from receipt data.

---

# Business Analytics

Today's work is starting to make the Receipt Manager more useful as a business analytics system.

The application can now answer questions such as:

```text
How many receipts do we have?

How much money was generated?

How much did each store generate?

Which store generated the most money?

Which store generated the least?

What is the average sale per receipt for each store?
```

These are examples of information that can eventually be displayed in a business dashboard.

---

# Reflection

Today's lesson helped me understand that the value of a receipt management system is not only in storing receipts.

The stored receipts can be transformed into useful business information.

I also noticed that my functions are becoming more reusable. Instead of creating each statistic from scratch, I can build new statistics using functions I already created.

This is making the project more modular and closer to the architecture of a real application.

---

# Tomorrow's Goal

Tomorrow I will continue improving the analytics functionality and begin thinking about how customers and businesses can be represented in the system.

I also want to start considering how the current JSON-based structure could eventually evolve into a proper database structure for the larger Receipt Management, CRM, and Business Analytics platform.


