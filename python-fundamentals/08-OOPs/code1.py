"""
INTRODUCTION TO PROGRAMMING PARADIGMS
-------------------------------------

There are three main programming approaches:

1. Imperative Programming
2. Functional Programming
3. Object-Oriented Programming (OOP)
"""

# -----------------------------------------------------
# 1. IMPERATIVE PROGRAMMING
# -----------------------------------------------------
"""
In imperative programming, we write step-by-step instructions
for the computer to follow.

If we need to repeat a task, we often end up rewriting the same code.
"""

# Example: Adding two numbers
a = 20
b = 30
print("Imperative Output:", a + b)


# -----------------------------------------------------
# 2. FUNCTIONAL PROGRAMMING
# -----------------------------------------------------
"""
In functional programming, we wrap logic inside functions.

Whenever we need the same task, we simply call the function.
"""

# Example: Addition function
def addition(a, b):
    return a + b

print("Functional Output:", addition(3, 5))
print("Functional Output:", addition(834, 3424))


# -----------------------------------------------------
# 3. OBJECT-ORIENTED PROGRAMMING (OOP)
# -----------------------------------------------------
"""
In OOP, we organize code using classes and objects.

It is useful for building large and reusable programs.
It helps reduce code repetition and improves structure, scalability, and security.
"""

# Class = Blueprint
# Object = Instance of that blueprint

"""
Example:
A Vehicle Factory is like a class.

It defines:
- body type
- engine type
- tyres

Based on this blueprint, different vehicles are created:
bike, car, truck → these are objects
"""


# -----------------------------------------------------
# FOUR PILLARS OF OOP
# -----------------------------------------------------
"""
1. Encapsulation
-----------------
Wrapping data and methods together and restricting direct access.

Example:
A school classroom is accessible only to students who are allowed.
"""

"""
2. Inheritance
---------------
One class can inherit properties of another class.

Example:
Child inherits features from parents.
"""

"""
3. Polymorphism
----------------
One thing can take many forms.

Example:
A smartphone can act as a camera, calculator, music player, etc.
"""

"""
4. Abstraction
---------------
Hiding internal details and showing only essential features.

Example:
When you use a phone, you don't see internal circuits.
You just use features like calling or apps.
"""
