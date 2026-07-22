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