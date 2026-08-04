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
