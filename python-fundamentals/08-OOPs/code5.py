# ============================================================
# ENCAPSULATION IN PYTHON
# ============================================================

"""
ENCAPSULATION
--------------

Encapsulation means wrapping data (attributes) and methods
(functions) together inside a class.

It also helps us control how the data can be accessed or changed.

Benefits of Encapsulation:
1. Keeps related data and methods together.
2. Protects data from accidental modification.
3. Provides controlled access to data.
4. Makes code cleaner and easier to maintain.
5. Helps implement data hiding.

Python mainly uses naming conventions for access control.
"""


# ============================================================
# ACCESS MODIFIERS IN PYTHON
# ============================================================

"""
Python does not have strict access modifiers like Java.

Python commonly uses three levels:

1. Public
2. Protected
3. Private
"""


# ============================================================
# 1. PUBLIC ATTRIBUTES AND METHODS
# ============================================================

"""
PUBLIC MEMBERS
--------------

Public attributes and methods can be accessed from:
- Inside the class
- Outside the class
- Child/inherited classes

In Python, attributes and methods without an underscore
are considered public.
"""


class PublicExample:

    # Public class attribute
    company = "Toyota"

    def __init__(self, car_type, tyre, color):

        # Public instance attributes
        self.car_type = car_type
        self.tyre = tyre
        self.color = color

    # Public method
    def show_details(self):
        print("Car Details:")
        print("Type:", self.car_type)
        print("Tyre:", self.tyre)
        print("Color:", self.color)


# Creating object
car1 = PublicExample("Sedan", "MRF", "White")

# Accessing public method
car1.show_details()

# Accessing public class attribute
print("Company:", car1.company)

# Modifying public attribute
car1.company = "Kia"

print("Updated Company:", car1.company)


# ============================================================
# 2. PROTECTED ATTRIBUTES AND METHODS
# ============================================================

"""
PROTECTED MEMBERS
-----------------

Protected members are created using a SINGLE underscore (_).

Example:
    _name
    _age
    _show_details()

The single underscore means:

"These members are intended for internal use or use by
the class and its child classes."

However, Python does NOT strictly prevent access from outside
the class.

So this is still possible:

    object._name

But it is considered bad practice when external code directly
accesses protected members.
"""


class ProtectedExample:

    # Protected class attributes
    _company = "Toyota"
    _old = 12

    def __init__(self, car_type, tyre, color):

        # Protected instance attributes
        self._car_type = car_type
        self._tyre = tyre
        self._color = color

    # Protected method
    def _show_details(self):

        print("Car Details:")
        print("Type:", self._car_type)
        print("Tyre:", self._tyre)
        print("Color:", self._color)


# Creating object
car2 = ProtectedExample("SUV", "MRF", "Black")

# Technically possible, but generally discouraged
car2._show_details()

# Protected class attribute
print("Company:", car2._company)

# Protected attribute can technically be accessed
print("Old value:", car2._old)


# ============================================================
# PROTECTED MEMBERS WITH INHERITANCE
# ============================================================

"""
Protected members are especially useful with inheritance.

A child class can access the protected members of its parent
class.
"""


class Parent:

    def __init__(self):
        self._value = 100

    def _show_value(self):
        print("Protected value:", self._value)


class Child(Parent):

    def display(self):
        # Child class can access protected member
        print("Accessing from child class:", self._value)

        # Child class can also call protected method
        self._show_value()


obj3 = Child()
obj3.display()


# ============================================================
# 3. PRIVATE ATTRIBUTES AND METHODS
# ============================================================

"""
PRIVATE MEMBERS
---------------

Private members are created using DOUBLE underscores (__).

Example:

    self.__salary
    self.__show_salary()

Python uses a mechanism called NAME MANGLING for private
members.

This means the name is internally changed so that it is not
normally accessed directly from outside the class.

Private members are mainly intended to be used inside the
class itself.
"""


class PrivateExample:

    def __init__(self):

        # Public attribute
        self.name = "Pooja"

        # Protected attribute
        self._age = 20

        # Private attribute
        self.__salary = 500000

    # Public method
    def show_details(self):

        print("\nInside the class:")
        print("Public:", self.name)
        print("Protected:", self._age)
        print("Private:", self.__salary)

    # Public method to access private data
    def get_salary(self):

        return self.__salary

    # Public method to modify private data
    def set_salary(self, new_salary):

        if new_salary > 0:
            self.__salary = new_salary
        else:
            print("Salary must be greater than 0.")


# Creating object
person = PrivateExample()


# ------------------------------------------------------------
# PUBLIC MEMBER
# ------------------------------------------------------------

print("\nPublic Attribute:")
print(person.name)

# Public attribute can be modified
person.name = "Demo Attribute"

print("Updated Name:", person.name)


# ------------------------------------------------------------
# PROTECTED MEMBER
# ------------------------------------------------------------

print("\nProtected Attribute:")
print(person._age)


# ------------------------------------------------------------
# PRIVATE MEMBER
# ------------------------------------------------------------

print("\nPrivate Attribute:")

# Correct way: use a public method
print("Salary:", person.get_salary())


# Direct access will NOT normally work:
#
# print(person.__salary)
#
# It will produce:
# AttributeError: 'PrivateExample' object has no attribute '__salary'


# ------------------------------------------------------------
# MODIFYING PRIVATE DATA USING A METHOD
# ------------------------------------------------------------

person.set_salary(600000)

print("Updated Salary:", person.get_salary())


# ============================================================
# SUMMARY
# ============================================================

"""
ACCESS LEVEL       SYNTAX          OUTSIDE ACCESS

Public             name            Yes
Protected          _name           Technically yes,
                                   but discouraged
Private            __name          Not directly; Python
                                   uses name mangling


Example:

class Student:

    def __init__(self):
        self.name = "Pooja"          # Public
        self._age = 20               # Protected
        self.__marks = 95            # Private
"""


# ============================================================
# FINAL EXAMPLE OF ENCAPSULATION
# ============================================================

"""
The following example shows why encapsulation is useful.

Instead of allowing anyone to directly change the balance,
we provide controlled methods such as deposit() and withdraw().
"""


class BankAccount:

    def __init__(self, owner, balance):

        self.owner = owner

        # Private attribute
        self.__balance = balance

    def deposit(self, amount):

        if amount > 0:
            self.__balance += amount
            print("Amount deposited:", amount)
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):

        if amount <= 0:
            print("Invalid withdrawal amount.")

        elif amount > self.__balance:
            print("Insufficient balance.")

        else:
            self.__balance -= amount
            print("Amount withdrawn:", amount)

    def get_balance(self):

        return self.__balance


# Creating bank account
account = BankAccount("Pooja", 10000)

print("\nBank Account Example")
print("Owner:", account.owner)
print("Initial Balance:", account.get_balance())

account.deposit(5000)

print("Balance after deposit:", account.get_balance())

account.withdraw(3000)

print("Balance after withdrawal:", account.get_balance())