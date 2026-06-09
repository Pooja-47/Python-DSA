""" 
*Till now, whatever we studied was the Primitive approach (creating variables, writing code, and executing it).
*Object-Oriented Programming approach (uses classes, objects, methods, etc.)
*There is another thing called the Functional approach (creating and using functions). Let's see how functions work.
"""

# What are Functions:
"""
* Function is a reusable block of code with a name. 
* Instead of writing the same logic 10 times, you write it once as a function and call it 10 times.
"""
# Example:
""" 
"Let's say I have a friend acting as a function named 'Water'. Whenever I call the function 'Water', it provides me water."
"The fun fact is that I can call a function as many times as I want."
This is how functions work.
You can create multiple functions in your program.
"""
# There are two types of functions in Python:
"""
1. Built-in functions(Implicit functions) : These are Pre-defined functions, whose block of code is already defined.

    for example:
        print()         # We use parentheses whenever we define or call a function.
        input()
        len()
        int(), float()..... etc

2. User-defined functions(Explicit functions) : These are user-defined functions, whose block of code is defined by the user.

# Syntax:

def function_name():
    block of code   # colon is for indentation

* Where:
    def is a keyword that means you want to define or create a new function.
    function_name is the name of the function. It can follow the same naming rules as variables.      
"""

def greet():
    print('"Hello", welcome to Python!')
    print("Thank you!\n")   
    
# The function is defined above.
# It will execute whenever it is called.

greet()  # call function

greet()
greet()
greet()
greet()
greet()    # we can call as many times we want