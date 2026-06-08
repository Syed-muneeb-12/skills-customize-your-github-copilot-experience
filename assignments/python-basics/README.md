
# 📘 Assignment: Python Basics

## 🎯 Objective

Practice fundamental Python programming skills including user input, string formatting, arithmetic operations, and conditional statements by implementing small, focused functions.

## 📝 Tasks

### 🛠️	User Input and String Formatting

#### Description
Implement `welcome_message()` which prompts the user for basic details and returns a formatted welcome string.

#### Requirements
Completed program should:

- Implement a function `welcome_message()` that prompts the user for their name, age, and favorite color using `input()`.
- Return a string exactly matching the format: `Hello, [name]! You are [age] years old and your favorite color is [color].`
- Do not print inside the function — return the string so callers can print or test it.

Example usage:

```python
msg = welcome_message()
print(msg)
# Example output:
# Hello, Alice! You are 25 years old and your favorite color is blue.
```

### 🛠️	Basic Arithmetic

#### Description
Implement `add_two_numbers()` which prompts the user for two numeric values and returns their sum.

#### Requirements
Completed program should:

- Implement a function `add_two_numbers()` that uses `input()` to read two values.
- Convert inputs to numbers (accept integers or floats) and return their numeric sum.
- Do not print inside the function — return the numeric result.

Example usage:

```python
result = add_two_numbers()
print(result)
# If inputs are 3 and 7, output: 10
```

### 🛠️	Conditional Statements

#### Description
Implement `is_even(n)` that determines whether an integer is even.

#### Requirements
Completed program should:

- Implement `is_even(n: int) -> bool` which returns `True` when `n` is even, `False` otherwise.
- Do not print inside the function — return a boolean so callers can use or test it.

Example usage:

```python
print(is_even(4))  # True
print(is_even(5))  # False
```

