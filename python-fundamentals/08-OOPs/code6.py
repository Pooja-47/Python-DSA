# ============================================================
# ABSTRACTION IN PYTHON
# ============================================================

"""
ABSTRACTION
-----------

Abstraction is an Object-Oriented Programming (OOP) concept
used to hide unnecessary implementation details and show only
the essential features to the user.

For example:

When we start a bike, we simply call:

    bike.start()

We do not need to know all the internal steps involved in
starting the engine.

Abstraction helps us focus on WHAT an object does rather than
HOW it does it.
"""


# ============================================================
# ABSTRACT CLASSES AND ABSTRACT METHODS
# ============================================================

"""
ABSTRACT CLASS
--------------

An abstract class is a class that is intended to be used as
a blueprint for other classes.

It can contain:
    - Normal methods
    - Abstract methods
    - Attributes

An abstract class cannot normally be instantiated directly.


ABSTRACT METHOD
---------------

An abstract method is a method that is declared in the
abstract class but does not contain its actual implementation.

The subclasses are responsible for providing the implementation
of the abstract method.
"""


# ============================================================
# abc MODULE
# ============================================================

"""
Python provides the 'abc' module for implementing abstraction.

ABC
---
ABC stands for Abstract Base Class.

abstractmethod
--------------
It is a decorator used to declare a method as abstract.
"""

from abc import ABC, abstractmethod


# ============================================================
# CREATING AN ABSTRACT CLASS
# ============================================================

class Vehicle(ABC):

    @abstractmethod
    def engine_start(self):
        """
        Abstract method.

        Every concrete subclass of Vehicle must provide its
        own implementation of engine_start().
        """
        pass


# ============================================================
# SUBCLASS 1: BIKE
# ============================================================

class Bike(Vehicle):

    def engine_start(self):
        print("Bike engine starts with a self-start button.")


# ============================================================
# SUBCLASS 2: CAR
# ============================================================

class Car(Vehicle):

    def engine_start(self):
        print("Car engine starts with a key or push button.")


# ============================================================
# CREATING OBJECTS OF SUBCLASSES
# ============================================================

bike = Bike()
car = Car()

bike.engine_start()
car.engine_start()


# ============================================================
# ABSTRACT CLASS CANNOT BE INSTANTIATED DIRECTLY
# ============================================================

"""
The following code will produce an error:

vehicle = Vehicle()

Why?

Because Vehicle contains an abstract method
engine_start() that has no implementation.

Therefore, Python does not allow us to create an object
directly from Vehicle.
"""

# vehicle = Vehicle()
# TypeError:
# Can't instantiate abstract class Vehicle with abstract method
# engine_start


# ============================================================
# INCOMPLETE SUBCLASS
# ============================================================

"""
A subclass that inherits an abstract class must implement all
its abstract methods before we can create its object.

For example, suppose Car does not implement engine_start():

    class Car(Vehicle):
        pass

Then:

    car = Car()

will produce a TypeError.

This happens because Car is still an abstract class.
"""


# ============================================================
# CORRECT EXAMPLE OF INCOMPLETE SUBCLASS
# ============================================================

class IncompleteVehicle(Vehicle):
    pass


# The following will give an error because
# IncompleteVehicle has not implemented engine_start().

# obj = IncompleteVehicle()


# ============================================================
# ABSTRACTION WITH MULTIPLE ABSTRACT METHODS
# ============================================================

"""
An abstract class can contain more than one abstract method.

Every concrete subclass must implement all of them.
"""


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Dog(Animal):

    def sound(self):
        print("Dog makes: Bark")

    def move(self):
        print("Dog moves by walking/running")


class Bird(Animal):

    def sound(self):
        print("Bird makes: Chirp")

    def move(self):
        print("Bird moves by flying")


dog = Dog()
bird = Bird()

print("\nDog:")
dog.sound()
dog.move()

print("\nBird:")
bird.sound()
bird.move()


# ============================================================
# ABSTRACTION + POLYMORPHISM
# ============================================================

"""
Abstraction and polymorphism can work together.

The same method name can behave differently for different
objects.

Here both Dog and Bird have:

    sound()
    move()

But each class provides its own implementation.
"""


animals = [Dog(), Bird()]

print("\nUsing Polymorphism:")

for animal in animals:
    animal.sound()
    animal.move()


# ============================================================
# REAL-LIFE EXAMPLE: PAYMENT SYSTEM
# ============================================================

"""
A good real-world example of abstraction is a payment system.

The user only needs to know:

    make_payment()

They do not need to know the internal implementation of
UPI, Credit Card, or PayPal payment processing.
"""


class Payment(ABC):

    @abstractmethod
    def make_payment(self, amount):
        pass


class UPI(Payment):

    def make_payment(self, amount):
        print(f"Payment of ₹{amount} made using UPI.")


class CreditCard(Payment):

    def make_payment(self, amount):
        print(f"Payment of ₹{amount} made using Credit Card.")


class PayPal(Payment):

    def make_payment(self, amount):
        print(f"Payment of ₹{amount} made using PayPal.")


# Creating objects
upi = UPI()
card = CreditCard()
paypal = PayPal()

print("\nPayment Examples:")

upi.make_payment(1000)
card.make_payment(2000)
paypal.make_payment(1500)