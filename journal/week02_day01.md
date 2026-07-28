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