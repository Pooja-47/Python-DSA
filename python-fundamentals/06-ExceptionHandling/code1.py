# ==========================
# Exception Handling in Python
# ==========================

# Errors
"""
Errors are problems in the code that prevent the program from running.

Common Errors:

1. SyntaxError
   - Occurs when Python syntax rules are violated.

   Example:
       print("Hello"

2. IndentationError
   - Occurs when indentation (spacing) is incorrect.

   Example:
       if True:
       print("Hello")

3. TabError
   - Occurs when tabs and spaces are mixed improperly.

   Example:
       if True:
           print("Hello")
       	print("World")
"""

# ==========================
# Exceptions
# ==========================

"""
Exceptions are runtime errors that occur while the program is executing.
Unlike syntax errors, exceptions can be handled using exception handling.

Common Exceptions:
"""

# 1. ZeroDivisionError
"""
Raised when a number is divided by zero.

Example:
    a = 20
    b = 0
    print(a / b)
"""

# 2. TypeError
"""
Raised when an operation is performed on incompatible data types.

Example:
    a = 20
    b = "9"

    print(a + b)
"""

# 3. ValueError
"""
Raised when a function receives a valid data type but an invalid value.

Example:
    num = int("hello")
"""

# 4. FileNotFoundError
"""
Raised when attempting to access a file that does not exist.

Example:
    file = open("data.txt")
"""

# ==========================
# Exception Handling Keywords
# ==========================

"""
Exception handling allows a program to continue running even when
an error occurs during execution.

# Program Flow Continues:

Exception handling prevents the program from crashing due to
handled exceptions, allowing the remaining code to execute.


Keywords used in exception handling:

1. try
   - Contains code that may raise an exception.

2. except
   - Used to handle errors that occur in the try block.

   - To handle a specific type of error, write the exception name.

       except ZeroDivisionError:
           print("Cannot divide by zero.")

   - To catch any exception and see its message, use:

       except Exception as err:
           print(err)

     Here, 'err' stores information about the exception that occurred.

3. else
   - Executes only if no exception occurs.

4. finally
   - Always executes, whether an exception occurs or not.
   - Commonly used for cleanup operations.

5. raise
   - Used to manually raise an exception.
"""


# try and except : try and except both are used together

try:
    # Risky code that may raise an exception
    num = 10 / 0

except ZeroDivisionError:
    # Handles division by 0 errors
    print("Cannot divide by zero.")

# Output:
# Cannot divide by zero.

# Multiple Exceptions

try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ValueError:
    print("Please enter a valid number.")

except ZeroDivisionError:
    print("Cannot divide by zero.")

# else 

try:
    num = int(input("Enter a number: "))
    result = 10 / num

except ZeroDivisionError:
    print("Cannot divide by zero.")

else:
    # Runs only if no exception occurs
    print("Division successful:", result)

# finally  

try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found.")

finally:
    # Always executes, regardless of whether an exception occurs
    #commonly used for cleanup operations
    print("Execution completed.")


# Taking input from the user
a = int(input("Enter your 1st number: "))
b = int(input("Enter your 2nd number: "))

try:
    print(a / b)

except Exception as err:
    # Handles any exception raised in the try block
    print(f"Sorry, an error occurred: {err}")

else:
    print("Division performed successfully.")

finally:
    print("Program execution completed.")


# ==========================
# Raising Exceptions Manually
# ==========================

"""
The raise keyword is used to manually generate an exception.
"""

# raise

"""
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("You are not eligible.")

print("You are eligible.")
"""


# ==========================
# Program Flow Continues
# ==========================

"""
Exception handling prevents the program from crashing due to
handled exceptions, allowing the remaining code to execute.
"""





























