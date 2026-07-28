# Week 1 – Day 1 Journal

**Date:** 21 July 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Introduction to Python Programming

---

# Objectives

Today I wanted to:

- Learn what Python is.
- Understand how Python programs run.
- Learn how to use the `print()` function.
- Learn how to write comments.
- Set up my Python project.
- Initialize Git and connect my project to GitHub.

---

# What I Learned

Today was my first day learning Python.

I learned that Python is a high-level programming language that allows humans to write instructions in a simple and readable way. Instead of writing machine code, I can write Python code, and the Python interpreter translates it into instructions the computer understands.

I learned that the `print()` function displays information on the screen. I also discovered that calling `print()` without any text prints a blank line, which helps make program output easier to read.

I learned that comments begin with the `#` symbol. Comments are written for people reading the code and are ignored by Python when the program runs. They help explain what the code is doing and make it easier to understand later.

---

# Practice Completed

Today I created programs that:

- Printed a welcome message.
- Printed my name.
- Printed my favorite food.
- Printed my dream job.
- Printed a simple Receipt App banner.
- Used comments to explain different sections of my code.

---

# Challenges I Faced

Today I faced a few Git challenges.

I received errors such as:

- `fatal: not a git repository`
- `fatal: No configured push destination`
- `fatal: 'origin' does not appear to be a git repository`

I also accidentally created a remote named `oringin` instead of `origin`.

---

# How I Solved Them

I learned how to:

- Initialize a Git repository using `git init`.
- Check the repository status using `git status`.
- Create commits using `git add` and `git commit`.
- Add a remote repository using `git remote add origin`.
- Check configured remotes using `git remote -v`.
- Identify and remove an incorrectly named remote.
- Understand the difference between a local Git repository and a GitHub repository.

Although I haven't completed the push yet, I now understand what caused the errors and how to fix them.

---

# Key Concepts I Remember

- Python is a programming language that is easy for humans to read.
- The Python interpreter executes Python code.
- `print()` displays information on the screen.
- `print()` with no arguments prints a blank line.
- Comments start with `#` and are ignored by Python.
- Git tracks changes in my project.
- GitHub stores my project online.
- A remote connects my local Git repository to GitHub.

---

# What I Enjoyed

I enjoyed writing my first Python program and seeing the output appear in the terminal.

It was also exciting to learn how Git and GitHub work together because I know these are important tools used by professional software developers.

---

# What I Found Difficult

The Git setup was more challenging than writing the Python code.

Understanding repositories, remotes, branches, and pushing code to GitHub was new to me, but I now have a much better understanding of how everything connects.

---

# Goals for Tomorrow

Tomorrow I want to learn:

- Variables
- Data types
- The `input()` function
- How Python stores information in memory
- How to begin making my Receipt Manager interactive

---

# Reflection

Today was a successful start to my Python journey.

I built my first Python programs, practiced using `print()` and comments, and began learning Git and GitHub.

Although I encountered a few Git errors, I learned how to troubleshoot them instead of giving up.

I feel more confident than when I started, and I'm excited to continue building my Receipt Manager application one step at a time.

---

# Commands I Learned Today

```bash
python3 filename.py
git init
git status
git add .
git commit -m "message"
git remote add origin <repository-url>
git remote -v
git branch
git push -u origin main
```

---

# Vocabulary

| Term | Meaning |
|------|---------|
| Python | A high-level programming language. |
| Interpreter | A program that reads and executes Python code. |
| `print()` | Displays information on the screen. |
| Comment | A note in the code ignored by Python. |
| Repository | A folder tracked by Git. |
| Commit | A saved snapshot of the project. |
| Remote | A connection between a local Git repository and GitHub. |
| GitHub | A platform for hosting Git repositories online. |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐☆☆ (3/5)

**Confidence:** ⭐⭐⭐⭐☆ (4/5)

---

**End of Week 1 – Day 1**

# Week 1 – Day 2 Journal

**Date:** 22 July 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Variables, Data Types, and User Input

---

# Objectives

Today I wanted to:

- Learn what variables are.
- Understand the basic Python data types.
- Learn how to get input from the user.
- Learn how to display stored information.
- Build a simple console receipt application.

---

# What I Learned

Today I learned that a variable is like a labeled box that stores information. Instead of writing the same value repeatedly, I can store it in a variable and use it whenever I need it.

I also learned that the `=` operator in Python is an assignment operator. It stores the value on the right-hand side into the variable on the left-hand side. It does not mean "is equal to" like it does in mathematics.

I learned that variables can change. If I assign a new value to a variable, the old value is replaced.

For example:

```python
store = "Shoprite"
store = "Spar"
store = "Game"
```

At the end, the variable `store` contains only `"Game"`.

---

# Data Types I Learned

Today I learned four basic Python data types:

| Data Type | Description | Example |
|-----------|-------------|---------|
| `str` | Stores text | `"Shoprite"` |
| `int` | Stores whole numbers | `10` |
| `float` | Stores decimal numbers | `2500.50` |
| `bool` | Stores `True` or `False` | `True` |

I also learned that I can use the `type()` function to check the data type of a variable.

Example:

```python
store = "Shoprite"
print(type(store))
```

Output:

```text
<class 'str'>
```

---

# User Input

Today I learned how to use the `input()` function.

Example:

```python
name = input("Enter your name: ")
```

This allows my program to ask the user for information instead of displaying only fixed text.

I also learned that `input()` always returns a string, even if the user types a number.

---

# Practice Completed

Today I completed the following exercises:

- Asked the user for their name.
- Asked for their favorite food.
- Asked for their dream job.
- Displayed the information entered by the user.
- Created variables using different data types.
- Used the `type()` function to identify data types.
- Built a simple receipt display that collected:
  - Store name
  - Receipt number
  - Item name
  - Quantity
  - Price

---

# Challenges I Faced

While working on today's exercises, I made a mistake by trying to check the data type of variables before creating them.

For example:

```python
print(type(store))
```

before writing:

```python
store = "Shoprite"
```

This caused a `NameError` because the variable did not exist yet.

---

# How I Solved It

I learned that a variable must be created before it can be used.

The correct order is:

```python
store = "Shoprite"
print(type(store))
```

I also learned the importance of writing code in the correct sequence.

---

# Key Concepts I Remember

- Variables store information.
- Variables can be updated with new values.
- `=` assigns a value to a variable.
- `input()` collects information from the user.
- `type()` checks the data type of a variable.
- `input()` always returns a string.
- Variables must be created before they are used.

---

# Mentor Feedback

Today's feedback helped me understand:

- Why variables should have meaningful names.
- Why Python developers prefer `snake_case` for variable names.
- Why the order of code matters.
- Why a variable must exist before I can use it.

---

# What I Enjoyed

I enjoyed making my program interactive by asking the user questions.

Instead of displaying fixed messages, my program now responds to the user's input, which makes it feel like a real application.

---

# What I Found Difficult

The biggest challenge today was understanding why I received a `NameError`.

After reviewing my code, I realized I was trying to use variables before creating them.

This taught me to carefully think about the order in which my code runs.

---

# Goals for Tomorrow

Tomorrow I want to learn:

- Arithmetic operators
- Assignment operators
- Comparison operators
- Type conversion using `int()` and `float()`
- How to calculate receipt totals

---

# Reflection

Today was an exciting lesson because my programs became interactive.

I learned how to store information using variables, collect input from the user, and display the information in a simple receipt format.

I also learned that programming is not just about writing code but also about understanding the order in which the computer executes instructions.

Every lesson is bringing me one step closer to building my own Receipt Manager application.

---

# Commands I Used Today

```bash
python3 lessons/day02.py
python3 practice/practice_day02.py
python3 challenges/challenge_day02.py

git add .
git commit -m "Week 1 Day 2: Learned variables, data types, and user input"
```

---

# Vocabulary

| Term | Meaning |
|------|---------|
| Variable | A named location that stores data. |
| Assignment | Storing a value in a variable using `=`. |
| String (`str`) | A sequence of characters or text. |
| Integer (`int`) | A whole number. |
| Float (`float`) | A decimal number. |
| Boolean (`bool`) | A value that is either `True` or `False`. |
| `input()` | Collects information from the user. |
| `type()` | Displays the data type of a value or variable. |
| `snake_case` | A naming style where words are lowercase and separated by underscores, e.g., `store_name`. |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐☆☆ (3/5)

**Confidence:** ⭐⭐⭐⭐☆ (4/5)

---

# End of Week 1 – Day 2

## Progress Summary

✅ Learned variables

✅ Learned data types

✅ Learned user input

✅ Learned how to use `type()`

✅ Built a simple console receipt application

✅ Improved my understanding of variable assignment and code execution order

# Week 1 – Day 3 Journal

**Date:** 23 July 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Operators, Type Conversion, and Calculations

---

# Objectives

Today I wanted to:

- Learn arithmetic operators.
- Learn assignment operators.
- Learn comparison operators.
- Understand why `input()` returns a string.
- Learn how to convert strings into numbers.
- Build my first receipt calculator.

---

# What I Learned

Today I learned how Python performs mathematical calculations using arithmetic operators.

I also learned that when a user enters information using the `input()` function, Python always stores the value as a string (`str`). If I want to perform calculations, I must first convert the string into a number using either `int()` or `float()`.

This was an important lesson because my receipt application needs to calculate totals instead of only displaying information.

---

# Arithmetic Operators

Today I learned these arithmetic operators:

| Operator | Meaning | Example | Result |
|----------|---------|---------|--------|
| `+` | Addition | `5 + 3` | `8` |
| `-` | Subtraction | `5 - 3` | `2` |
| `*` | Multiplication | `5 * 3` | `15` |
| `/` | Division | `10 / 2` | `5.0` |
| `//` | Floor Division | `10 // 3` | `3` |
| `%` | Modulus (Remainder) | `10 % 3` | `1` |
| `**` | Exponent (Power) | `2 ** 3` | `8` |

---

# Type Conversion

Today I learned that I can convert data into different types.

Example:

```python
price = float(input("Enter price: "))
quantity = int(input("Enter quantity: "))
```

This converts:

- `"1500.50"` into `1500.50`
- `"2"` into `2`

Now Python can perform calculations.

---

# Assignment Operators

I learned that instead of writing:

```python
total = total + price
```

I can write:

```python
total += price
```

Other assignment operators I learned:

| Operator | Example |
|----------|---------|
| `+=` | `x += 5` |
| `-=` | `x -= 5` |
| `*=` | `x *= 2` |
| `/=` | `x /= 2` |

These operators make my code shorter and easier to read.

---

# Comparison Operators

I also learned comparison operators.

These operators return either `True` or `False`.

Examples:

```python
5 > 3
5 < 3
5 == 5
5 != 5
```

Output:

```text
True
False
True
False
```

Although I have not used them much yet, I learned that they will be important when I start using `if` statements.

---

# Practice Completed

Today I completed the following:

- Practiced arithmetic operations.
- Practiced assignment operators.
- Practiced comparison operators.
- Converted user input into integers and floats.
- Calculated receipt subtotals.
- Displayed receipt information using f-strings.

---

# Receipt Calculator

Today I built my first receipt calculator.

The program asked the user for:

- Store name
- Item name
- Price
- Quantity

It then calculated:

```text
Subtotal = Price × Quantity
```

Finally, it displayed the receipt in a clean format.

---

# Challenges I Faced

At first, I was unsure why calculations could not be performed directly on values returned by `input()`.

I learned that `input()` always returns a string, so Python cannot multiply two strings together.

For example:

```python
price = input("Price: ")
quantity = input("Quantity: ")

subtotal = price * quantity
```

This produces a `TypeError`.

---

# How I Solved It

I solved the problem by converting the input values.

Example:

```python
price = float(input("Price: "))
quantity = int(input("Quantity: "))

subtotal = price * quantity
```

Now Python correctly performs the calculation.

---

# New Things I Discovered

Today I discovered that Python can multiply a string by an integer.

Example:

```python
print("Hi" * 3)
```

Output:

```text
HiHiHi
```

I also learned that Python cannot multiply two strings.

Example:

```python
"100" * "3"
```

This results in a `TypeError`.

---

# Mentor Challenges

Today I answered several programming questions without running the code.

Some of the concepts I understood were:

- Variables can store new values by replacing old ones.
- Multiplying a string by an integer repeats the string.
- Type conversion is necessary before performing calculations.
- Formatting numbers with `.2f` displays two decimal places.

These exercises helped me think like a programmer instead of relying only on running the code.

---

# Key Concepts I Remember

- `input()` always returns a string.
- `int()` converts text into whole numbers.
- `float()` converts text into decimal numbers.
- Arithmetic operators perform calculations.
- Assignment operators update variable values.
- Comparison operators return `True` or `False`.
- f-strings make output easier to read.
- `:.2f` formats numbers with two decimal places.

---

# What I Enjoyed

I enjoyed building my first receipt calculator because my program finally started doing real calculations instead of only displaying information.

It felt like I was building something useful.

---

# What I Found Difficult

The most challenging part was understanding why strings cannot be multiplied together.

After practicing type conversion, the concept became much clearer.

---

# Goals for Tomorrow

Tomorrow I want to learn:

- `if` statements
- `elif`
- `else`
- Boolean logic
- Input validation
- Making my receipt application smarter by checking user input

---

# Reflection

Today was one of my favorite lessons so far.

I learned how to perform calculations, convert data types, and build a simple receipt calculator.

I also practiced tracing code before running it, which helped me understand how Python executes programs step by step.

I can already see my programming skills improving each day, and I feel more confident writing Python code on my own.

---

# Commands I Used Today

```bash
python3 lessons/day03.py
python3 practice/practice_day03.py
python3 challenges/challenge_day03.py

git add .
git commit -m "Week 1 Day 3: Learned operators, type conversion, and calculations"
```

---

# Vocabulary

| Term | Meaning |
|------|---------|
| Arithmetic Operator | Performs mathematical calculations. |
| Assignment Operator | Updates the value of a variable. |
| Comparison Operator | Compares two values and returns `True` or `False`. |
| Type Conversion | Changing one data type into another. |
| `int()` | Converts a value into an integer. |
| `float()` | Converts a value into a floating-point number. |
| `subtotal` | The total amount before taxes or discounts. |
| f-string | A way to insert variables directly into a string. |
| `.2f` | Formats a floating-point number with two decimal places. |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐⭐☆ (4/5)

**Confidence:** ⭐⭐⭐⭐⭐ (5/5)

---

# Progress Summary

✅ Learned arithmetic operators

✅ Learned assignment operators

✅ Learned comparison operators

✅ Learned type conversion

✅ Built my first receipt calculator

✅ Practiced tracing Python code before running it

✅ Improved my understanding of calculations and formatted output

---

# End of Week 1 – Day 3

# Week 1 – Day 4 Journal

**Date:** 24 July 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Decision Making with `if`, `elif`, and `else`

---

# Objectives

Today I wanted to:

- Learn how Python makes decisions.
- Understand `if`, `elif`, and `else` statements.
- Learn Boolean expressions.
- Validate user input.
- Improve my receipt calculator by preventing invalid data.

---

# What I Learned

Today I learned that programs can make decisions using `if`, `elif`, and `else`.

Instead of always running every line of code, Python can decide what to do based on whether a condition is `True` or `False`.

This makes my programs smarter because they can respond differently depending on what the user enters.

---

# The `if` Statement

I learned that an `if` statement allows Python to execute code only when a condition is true.

Example:

```python
age = 18

if age >= 18:
    print("You are an adult.")
```

If the condition is true, Python runs the indented code.

---

# The `else` Statement

I learned that `else` runs when the `if` condition is false.

Example:

```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Only one block of code is executed.

---

# The `elif` Statement

I learned that `elif` lets me check another condition if the previous one is false.

Example:

```python
score = 75

if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
else:
    print("Keep Practicing")
```

This allows a program to make multiple decisions.

---

# Boolean Expressions

Today I learned that every condition evaluates to either:

- `True`
- `False`

Python uses these values to decide which block of code should run.

---

# Comparison Operators

Today I reviewed comparison operators.

| Operator | Meaning |
|----------|---------|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

These operators are used inside `if` statements to compare values.

---

# Receipt Validation

Today I improved my receipt application by validating user input.

My program checks:

- Store name is not empty.
- Item name is not empty.
- Price is valid.
- Quantity is valid.

If any of these checks fail, the program displays an error message.

Otherwise, it calculates the subtotal and prints the receipt.

---

# My Solution

One thing I am proud of today is that I wrote my own validation logic.

I used the `or` operator to check multiple conditions at once.

```python
if store_name == "" or item_name == "" or quantity <= 0 or price <= 0:
```

Then I displayed a specific error message for each invalid field.

This helped me understand how to combine conditions while still giving meaningful feedback to the user.

---

# Mentor Feedback

Today I received useful feedback about my solution.

### What I did well

- Used `if` statements correctly.
- Validated multiple inputs.
- Printed all validation errors instead of stopping after the first one.
- Created a clean receipt layout.
- Continued using f-strings.

### Improvements I made

I learned that my original code used:

```python
quantity < 0
price < 0
```

This accidentally allowed the value `0`.

I corrected my validation to:

```python
quantity <= 0
price <= 0
```

Now my program correctly follows the requirement that both values must be greater than zero.

---

# Challenges I Faced

At first, I thought checking for values less than zero was enough.

After testing my program, I realized that entering `0` still printed a receipt with a subtotal of `₦0.00`.

This taught me an important lesson about carefully reading program requirements.

---

# How I Solved It

I changed my validation conditions from:

```python
quantity < 0
price < 0
```

to:

```python
quantity <= 0
price <= 0
```

Now invalid values are rejected before the receipt is displayed.

---

# Key Concepts I Remember

- `if` executes code when a condition is true.
- `else` executes when the condition is false.
- `elif` allows multiple conditions.
- Conditions return either `True` or `False`.
- Input validation prevents invalid data.
- Multiple conditions can be combined using `or`.
- Programs should validate data before performing calculations.

---

# What I Enjoyed

Today was my favorite lesson so far because my receipt application became smarter.

Instead of accepting every input, it now checks whether the data is valid before calculating the subtotal.

It feels more like a real application.

---

# What I Found Difficult

The biggest challenge was identifying a logic bug.

My program worked without crashing, but it still accepted a price of `0`.

This taught me that a program can run successfully while still producing incorrect results.

---

# Reflection

Today I learned that writing code is not only about making it run.

It is also about making sure it behaves correctly.

I learned how to use decision-making statements, validate user input, and think carefully about program logic.

I also learned to mentally trace my program before running it, which helps me find bugs more easily.

I feel more confident because my receipt application is becoming more realistic every day.

---

# Commands I Used Today

```bash
python3 lessons/day04.py
python3 practice/practice_day04.py
python3 challenges/challenge_day04.py

git add .
git commit -m "Week 1 Day 4: Learned if statements and input validation"
```

---

# Vocabulary

| Term | Meaning |
|------|---------|
| `if` | Executes code when a condition is true. |
| `elif` | Checks another condition if the previous one is false. |
| `else` | Executes when all previous conditions are false. |
| Boolean | A value that is either `True` or `False`. |
| Validation | Checking whether user input is correct before using it. |
| Logic Bug | A mistake where the program runs but produces the wrong result. |
| Condition | An expression that evaluates to `True` or `False`. |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐⭐☆ (4/5)

**Confidence:** ⭐⭐⭐⭐⭐ (5/5)

---

# Progress Summary

✅ Learned `if`, `elif`, and `else`

✅ Learned Boolean expressions

✅ Validated receipt input

✅ Fixed a logic bug by changing `< 0` to `<= 0`

✅ Improved my receipt application with input validation

✅ Practiced thinking through code before running it

---

# End of Week 1 – Day 4

Today was an important milestone. My receipt application no longer just accepts input—it now checks that the input is valid before processing it. This is a key step toward building a reliable and professional application.


# Week 1 – Day 5 Journal

**Date:** 26 July 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Functions – Organizing and Reusing Code

---

# Objectives

Today I wanted to:

- Learn what functions are.
- Understand how to create and call functions.
- Learn about parameters and arguments.
- Understand the `return` statement.
- Organize my receipt application using functions.

---

# What I Learned

Today I learned that a function is a reusable block of code that performs a specific task.

Instead of writing the same code repeatedly, I can write it once inside a function and call it whenever I need it.

Functions make programs:

- Easier to read
- Easier to maintain
- Easier to debug
- Easier to reuse

---

# Creating My First Function

I learned that a function is created using the `def` keyword.

Example:

```python
def greet():
    print("Hello!")
```

The function does nothing until it is called.

To execute it:

```python
greet()
```

---

# Parameters and Arguments

Today I learned the difference between parameters and arguments.

Example:

```python
def greet(name):
    print(f"Hello {name}")
```

When I call:

```python
greet("Ayoola")
```

- `name` is the **parameter**.
- `"Ayoola"` is the **argument**.

A parameter is like an empty box, while an argument is the value placed inside that box.

---

# Return Values

I learned that some functions calculate a value and send it back using the `return` statement.

Example:

```python
def add(a, b):
    return a + b
```

Calling:

```python
result = add(5, 3)
```

stores the returned value inside `result`.

I learned that `return` allows one function to produce a result that another part of the program can use.

---

# Building Functions for My Receipt App

Today I began organizing my receipt application into smaller functions.

I created:

```python
def calculate_subtotal(price, quantity):
    return price * quantity
```

This function has one responsibility:

- Calculate and return the subtotal.

---

I also created:

```python
def print_receipt(store_name, item_name, price, quantity, subtotal):
```

This function prints the receipt in a clean format.

Separating the printing logic into its own function made the rest of my program much easier to read.

---

# Building My Validation Function

I also created:

```python
def validate_input(store_name, item_name, price, quantity):
```

At first, I made a mistake by trying to calculate the subtotal and print the receipt inside this function.

After reviewing my code, I realized that the function had too many responsibilities.

I improved it so that it only checks whether the input is valid.

The final version returns:

```python
return False
```

when there is invalid input, and

```python
return True
```

when everything is valid.

This made the function much cleaner and more useful.

---

# Understanding Single Responsibility

One of the biggest lessons I learned today was that each function should have only one responsibility.

My application now has three separate functions:

```text
validate_input()
        ↓
Checks user input

calculate_subtotal()
        ↓
Calculates the subtotal

print_receipt()
        ↓
Displays the receipt
```

Each function has one clear job.

This makes the program easier to understand and easier to modify in the future.

---

# Mentor Feedback

Today I received valuable feedback about my functions.

### What I did well

- Created separate functions.
- Used parameters correctly.
- Used `return` correctly.
- Organized the receipt application.
- Improved the readability of my code.

### Mistakes I Fixed

At first, I mistakenly called:

```python
calculate_subtotal(store_name, item_name, price, quantity)
```

even though the function only expected:

```python
price
quantity
```

I corrected it to:

```python
calculate_subtotal(price, quantity)
```

I also learned that validation should not calculate totals or print receipts.

Instead, it should simply return `True` or `False`.

---

# Challenges I Faced

The biggest challenge today was understanding how functions should work together.

Initially, I thought every function should perform multiple tasks.

After reviewing my code, I learned that functions should focus on one responsibility.

This made my program much cleaner.

---

# How I Solved It

I reorganized my receipt application into three independent functions.

The main program now follows a simple flow:

1. Get user input.
2. Validate the input.
3. Calculate the subtotal.
4. Print the receipt.

This made the overall program easier to read and understand.

---

# Key Concepts I Remember

- Functions help organize code.
- Functions reduce code duplication.
- Parameters receive values.
- Arguments are the actual values passed into a function.
- `return` sends a value back to the caller.
- A function should have one responsibility.
- Breaking a program into smaller functions makes it easier to maintain.

---

# What I Enjoyed

Today was one of my favorite lessons because I learned how professional developers organize their programs.

Instead of writing one long program, I now understand how to split it into smaller, reusable pieces.

This made my receipt application look much more professional.

---

# What I Found Difficult

The most difficult part was deciding what each function should do.

It took some practice to understand that validation, calculation, and printing should each be handled by different functions.

Once I separated those responsibilities, the program became much easier to follow.

---

# Reflection

Today I learned that writing good software is not just about making it work.

It is also about organizing code so that it is easy to read, test, and improve.

Functions are one of the most important tools for achieving this.

I also learned that each function should have one clear purpose and communicate with the rest of the program using parameters and return values.

This lesson changed the way I think about writing programs.

---

# Commands I Used Today

```bash
python3 lessons/day05.py
python3 practice/practice_day05.py
python3 challenges/challenge_day05.py

git add .
git commit -m "Week 1 Day 5: Learned functions and code organization"
git push
```

---

# Vocabulary

| Term | Meaning |
|------|---------|
| Function | A reusable block of code that performs a specific task. |
| Parameter | A variable defined in a function that receives a value. |
| Argument | The value passed to a function when it is called. |
| Return | Sends a value back to the code that called the function. |
| Reusability | Writing code once and using it multiple times. |
| Code Organization | Structuring a program into smaller, manageable parts. |
| Single Responsibility | The principle that a function should have one clear job. |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐⭐☆ (4/5)

**Confidence:** ⭐⭐⭐⭐⭐ (5/5)

---

# Progress Summary

✅ Learned how to create functions

✅ Learned how to call functions

✅ Learned parameters and arguments

✅ Learned the `return` statement

✅ Organized my receipt application into reusable functions

✅ Improved code readability

✅ Learned the Single Responsibility Principle

---

# End of Week 1 – Day 5

Today was a major step forward in my Python learning journey. My receipt application is no longer one long block of code—it is now organized into reusable functions that each perform one specific task. This lesson taught me how professional developers structure their programs and prepared me for building larger, more maintainable applications in the future.


# Week 1 – Day 6 Journal

**Date:** 27 July 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Lists (`list`) and Loops (`for`)

---

# Objectives

Today I wanted to:

- Learn how to store multiple values using lists.
- Understand how `for` loops work.
- Build a receipt that supports multiple items.
- Learn how to calculate a running total.
- Learn how to reuse functions instead of copying code.

---

# What I Learned

Today I learned that a list allows me to store many values inside a single variable.

Instead of creating variables like:

```python
item1 = "Bread"
item2 = "Milk"
item3 = "Rice"
```

I can simply write:

```python
items = ["Bread", "Milk", "Rice"]
```

This makes my code cleaner and easier to manage.

---

# Understanding Lists

A list is a collection of values.

Example:

```python
items = ["Bread", "Milk", "Rice"]
```

Each item has an index.

| Index | Value |
|------:|-------|
| 0 | Bread |
| 1 | Milk |
| 2 | Rice |

I learned that Python starts counting from **0**.

---

# Understanding Loops

Today I learned that a `for` loop repeats the same block of code.

Example:

```python
for item in items:
    print(item)
```

Output:

```
Bread
Milk
Rice
```

Instead of writing multiple `print()` statements, the loop automatically prints every item in the list.

---

# Building My Receipt

Today I upgraded my receipt application.

Instead of supporting only one item, my program can now store multiple items.

My program asks for:

- Store name
- Number of items

Then for each item it asks for:

- Item name
- Price
- Quantity

It calculates the subtotal for each item and finally displays the grand total.

---

# My Solution

I created four lists:

```python
items = []
prices = []
quants = []
sub_totals = []
```

As the user entered each item, I stored the information inside the appropriate list.

For every item I calculated:

```python
sub_total = item_price * item_quantity
```

Then I added it to the grand total:

```python
grand_total += sub_total
```

Finally, I used another loop to print the receipt.

---

# What I Learned About Accumulators

Today I learned about the accumulator pattern.

An accumulator keeps adding values during a loop.

Example:

```python
total = 0

for number in numbers:
    total += number
```

I also used this idea in my receipt application:

```python
grand_total += sub_total
```

This allowed my application to calculate the total cost of all purchased items.

---

# Mentor Feedback

Today I received positive feedback on my receipt application.

### What I did well

- Used lists correctly.
- Used `for` loops correctly.
- Calculated subtotals correctly.
- Calculated the grand total correctly.
- Printed a professional-looking receipt.
- Successfully supported multiple receipt items.

### Improvements Suggested

I learned that I should format prices consistently:

```python
print(f"Price: ₦{price:.2f}")
```

instead of:

```python
print(f"Price: ₦{price}")
```

I also learned that using more descriptive variable names, such as `quantities` instead of `quants`, makes code easier to understand.

---

# Learning About Code Reuse

One of the most important lessons today was learning how professional developers reuse code.

I asked whether I should copy my Day 5 functions into my Day 6 program.

I learned that copying code is not the best practice.

Instead, reusable functions should be placed inside a shared module, for example:

```
utils/
    receipt_utils.py
```

Then other programs can import them:

```python
from utils.receipt_utils import calculate_subtotal
```

This allows one function to be used by many files without duplication.

---

# Challenges I Faced

At first, I thought copying functions into every new file was the normal way to reuse code.

After learning about modules and imports, I now understand why programmers organize reusable code into separate files.

---

# How I Solved It

I learned that instead of copying functions repeatedly, I should:

1. Create a reusable module.
2. Store common functions inside it.
3. Import those functions whenever I need them.

This makes programs easier to maintain and update.

---

# Key Concepts I Remember

- A list stores multiple values.
- Python lists start indexing at 0.
- `append()` adds new items to a list.
- A `for` loop repeats code for every item in a list.
- An accumulator keeps a running total.
- Functions can be reused by importing them from another module.
- Reusing code is better than copying code.

---

# What I Enjoyed

Today was exciting because my receipt application became much more realistic.

Instead of handling only one item, it now supports multiple products just like a real supermarket receipt.

I also enjoyed learning how reusable functions make programs cleaner and easier to maintain.

---

# What I Found Difficult

The biggest challenge today was understanding how to reuse functions across different files.

I originally thought I needed to copy the functions into every new program.

Now I understand that importing functions from a shared module is a better approach.

---

# Reflection

Today I learned that programming is not just about making a program work.

It is also about organizing code so that it is reusable and easy to maintain.

Using lists and loops helped me build a more realistic receipt application, and learning about modules introduced me to how larger Python projects are structured.

I feel more confident because my application is beginning to resemble a real-world program.

---

# Commands I Used Today

```bash
python3 lessons/day06.py
python3 practice/practice_day06.py
python3 challenges/challenge_day06.py

git add .
git commit -m "Week 1 Day 6: Learned lists, loops, and reusable functions"
git push
```

---

# Vocabulary

| Term | Meaning |
|------|---------|
| List | A collection of multiple values stored in one variable. |
| Loop | A way to repeat code automatically. |
| `for` Loop | Repeats code for each item in a collection. |
| `append()` | Adds a new item to a list. |
| Accumulator | A variable that keeps a running total. |
| Module | A Python file that contains reusable code. |
| Import | Bringing functions or classes from one Python file into another. |
| Reusability | Writing code once and using it in many places. |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐⭐☆ (4/5)

**Confidence:** ⭐⭐⭐⭐⭐ (5/5)

---

# Progress Summary

✅ Learned Python lists

✅ Learned `for` loops

✅ Built a receipt that supports multiple items

✅ Calculated subtotals and a grand total

✅ Learned the accumulator pattern

✅ Learned why importing functions is better than copying code

✅ Improved my understanding of professional project organization

---

# End of Week 1 – Day 6

Today was a major milestone in my Python journey. My receipt application now supports multiple items, calculates a grand total, and is moving toward a more professional structure through reusable modules and imports. I can see my application becoming more powerful and better organized with each new lesson.

# Week 1 – Day 7 Journal

**Date:** 28 July 2026

**Project:** Receipt Manager App with Python

**Study Duration:** 3–4 Hours

---

# Topic

Dictionaries (`dict`), Modules, and Code Reusability

---

# Objectives

Today I wanted to:

- Learn what dictionaries are.
- Store related data together using dictionaries.
- Replace multiple lists with a list of dictionaries.
- Reuse functions by importing them from another file.
- Continue improving my receipt application.

---

# What I Learned

Today I learned that a **dictionary** stores related pieces of information together using **key-value pairs**.

Instead of storing data in four separate lists:

```python
items = []
prices = []
quantities = []
sub_totals = []
```

I learned that I can store everything about one receipt item inside a single dictionary.

Example:

```python
item = {
    "name": "Bread",
    "price": 1500,
    "quantity": 2,
    "subtotal": 3000,
}
```

This makes the code cleaner and easier to understand.

---

# Understanding Dictionaries

A dictionary stores information using keys and values.

Example:

```python
item = {
    "name": "Milk",
    "price": 1200,
    "quantity": 1,
}
```

To access a value:

```python
print(item["name"])
```

Output:

```
Milk
```

I learned that:

- A **key** is the name used to identify a value.
- A **value** is the actual information stored.

---

# List of Dictionaries

Today I learned that I can store many dictionaries inside a list.

```python
receipt_items = []
```

For every item entered by the user, I created a dictionary:

```python
item = {
    "name": item_name,
    "price": item_price,
    "quantity": item_quantity,
    "subtotal": sub_total,
}
```

Then I added it to the list:

```python
receipt_items.append(item)
```

This structure is much better than keeping separate lists for names, prices, quantities, and subtotals.

---

# Reusing Functions

One of the biggest lessons today was learning how to reuse functions properly.

Instead of copying my Day 5 functions into the new file, I created a reusable module:

```python
from utils.receipt_utils import calculate_subtotal, validate_input
```

I learned that professional programmers avoid copying code because it creates unnecessary duplication.

By importing functions, I can write code once and use it in many files.

---

# Using Validation Correctly

At first, I called:

```python
validate_input(store_name, item_name, item_price, item_quantity)
```

but I ignored the result.

I learned that since `validate_input()` returns either `True` or `False`, I should use it like this:

```python
if validate_input(store_name, item_name, item_price, item_quantity):
```

This ensures that only valid items are added to the receipt.

Invalid items are rejected instead of being saved.

---

# Improving My Receipt Application

My receipt application now follows this process:

1. Ask for the store name.
2. Ask how many items the customer bought.
3. Get the details for each item.
4. Validate the input.
5. Calculate the subtotal.
6. Store the item inside a dictionary.
7. Add the dictionary to a list.
8. Calculate the grand total.
9. Print a formatted receipt.

This structure is much cleaner than my earlier versions.

---

# Learning `enumerate()`

Today I also learned about `enumerate()`.

Instead of manually counting items like this:

```python
i = 1

for item in receipt_items:
    print(i)
    i += 1
```

I learned I can write:

```python
for index, item in enumerate(receipt_items, start=1):
```

This automatically provides the item number while looping through the list.

It makes the code shorter and easier to read.

---

# Mentor Feedback

Today I received excellent feedback on my code.

### What I did well

- Imported reusable functions instead of copying them.
- Replaced four parallel lists with a list of dictionaries.
- Reused `calculate_subtotal()`.
- Used validation correctly with `if validate_input(...)`.
- Used `enumerate()` to number receipt items.
- Improved the overall organization of my program.

### Improvements Suggested

I learned that I can still improve my application by handling situations where every item entered is invalid.

In the future, I will learn how to keep asking the user for valid input instead of simply skipping invalid items.

---

# Challenges I Faced

The biggest challenge today was understanding how dictionaries work and how to organize receipt data more effectively.

I also had to understand how imported functions communicate with the main program by returning `True` or `False`.

---

# How I Solved It

I solved these challenges by:

- Replacing multiple lists with dictionaries.
- Importing reusable functions.
- Using the return value of `validate_input()`.
- Organizing my receipt data into a cleaner structure.

---

# Key Concepts I Remember

- A dictionary stores related data together.
- Dictionaries use key-value pairs.
- A list can contain multiple dictionaries.
- Functions can be reused through imports.
- Validation should control whether data is accepted.
- `enumerate()` automatically numbers items in a loop.
- Good code organization makes programs easier to maintain.

---

# What I Enjoyed

Today I enjoyed seeing my receipt application become more professional.

Using dictionaries made the data much easier to manage, and importing reusable functions helped me understand how larger Python projects are organized.

---

# What I Found Difficult

The most difficult part was understanding how imported functions return values and how those values should control the program's flow.

After updating my code to use:

```python
if validate_input(...):
```

everything made much more sense.

---

# Reflection

Today was an important milestone in my Python journey.

I learned that writing good software is not only about solving a problem—it is also about organizing data and writing reusable code.

Replacing multiple lists with dictionaries made my program cleaner, and importing functions instead of copying them introduced me to a professional way of structuring Python projects.

I also learned that validation should determine whether information is accepted into the program.

Every improvement I make is helping my receipt application become closer to a real-world software project.

---

# Commands I Used Today

```bash
python3 lessons/day07.py
python3 practice/practice_day07.py
python3 challenges/challenge_day07.py

git add .
git commit -m "Week 1 Day 7: Learned dictionaries and improved receipt data structure"
git push
```

---

# Vocabulary

| Term | Meaning |
|------|---------|
| Dictionary | A collection of key-value pairs used to store related data. |
| Key | The name used to identify a value in a dictionary. |
| Value | The information associated with a key. |
| Module | A Python file containing reusable code. |
| Import | Bringing code from one module into another. |
| Reusability | Writing code once and using it in many places. |
| `enumerate()` | A function that provides both the index and value while looping. |
| Key-Value Pair | The relationship between a dictionary key and its stored value. |

---

# Daily Rating

**Understanding:** ⭐⭐⭐⭐⭐ (5/5)

**Difficulty:** ⭐⭐⭐⭐☆ (4/5)

**Confidence:** ⭐⭐⭐⭐⭐ (5/5)

---

# Progress Summary

✅ Learned dictionaries

✅ Learned key-value pairs

✅ Replaced parallel lists with a list of dictionaries

✅ Imported reusable functions from a module

✅ Used validation correctly with `if`

✅ Learned `enumerate()`

✅ Improved the organization of my receipt application

---

# End of Week 1 – Day 7

Today was one of the most important days in my Python learning journey. I transformed my receipt application by organizing related data into dictionaries and by reusing functions through imports instead of copying code. These improvements made my application cleaner, easier to maintain, and closer to the structure used in professional Python software development.