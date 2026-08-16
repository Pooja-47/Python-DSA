# ============================================================
# POLYMORPHISM
# ============================================================

"""
POLYMORPHISM
============

Polymorphism is one of the four pillars of Object-Oriented
Programming (OOP).

The word "Polymorphism" comes from two words:

    Poly  -> Many
    Morph -> Forms

Therefore, polymorphism means "many forms".

In programming, polymorphism allows the same method, function,
operator, or interface to behave differently depending on the
object or data it is working with.

In simple words:

    "Same interface, different behavior."

Python supports polymorphism mainly through:

    1. Method Overriding
    2. Duck Typing
    3. Operator Overloading

Python does NOT support traditional method overloading in the
same way as languages such as Java or C++.
"""


# ============================================================
# 1. SAME FUNCTION NAME DOES NOT MEAN POLYMORPHISM
# ============================================================

"""
Consider the following example:

If we define two functions with exactly the same name,
the second definition replaces the first definition.

Python does NOT keep both functions separately.
"""

def hello():
    print("Hello")

def hello():
    print("How are you?")

hello()

"""
Output:

How are you?

The second hello() definition replaced the first one.

This is called NAME REBINDING / REDEFINITION.

It should NOT be considered an example of polymorphism.

The same principle applies to methods inside a class:
Python does not support traditional method overloading simply
by defining multiple methods with the same name.
"""


# ============================================================
# 2. BASIC POLYMORPHISM
# ============================================================

"""
A simple way to understand polymorphism is:

    Same method name
    +
    Different objects
    =
    Different behavior

For example, both Animal and Human classes have a speak()
method, but the behavior of the method is different.
"""

class Animal:

    def speak(self):
        print("Animals make different sounds.")


class Human:

    def speak(self):
        print("Humans can communicate using language.")


animal = Animal()
human = Human()

animal.speak()
human.speak()

"""
Here:

    animal.speak()
        -> calls Animal's speak() method

    human.speak()
        -> calls Human's speak() method

The method name is the same:

    speak()

But the behavior is different depending on the object.

This is polymorphic behavior.

Notice that these classes do not need to inherit from each
other for this basic form of polymorphism.
"""


# ============================================================
# 3. POLYMORPHISM USING A COMMON FUNCTION
# ============================================================

"""
Polymorphism becomes more useful when the same function can
work with objects of different classes.

The function does not need to know the exact class of the object.

It only needs the object to provide the required method.
"""

class Dog:

    def speak(self):
        print("Dog says: Woof!")


class Cat:

    def speak(self):
        print("Cat says: Meow!")


def make_sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()

make_sound(dog)
make_sound(cat)

"""
The make_sound() function works with both Dog and Cat objects.

When we pass:

    dog -> Dog's speak() method is called

    cat -> Cat's speak() method is called

The function does not need separate versions such as:

    make_dog_sound()
    make_cat_sound()

It uses the same interface:

    speak()

This is one of the major benefits of polymorphism.
"""


# ============================================================
# 4. METHOD OVERRIDING
# ============================================================

"""
METHOD OVERRIDING
=================

Method overriding occurs when a child class provides its own
implementation of a method that is already defined in its
parent class.

Method overriding requires INHERITANCE.

The child class replaces the inherited behavior of the method
with its own implementation.

Syntax:

class Parent:

    def method(self):
        ...


class Child(Parent):

    def method(self):
        ...


Here, Child overrides the method inherited from Parent.
"""


class Animal:

    def __init__(self, name):
        self.name = name

    def details(self):
        print(f"Animal name: {self.name}")


class Dog(Animal):

    def details(self):
        print(f"Dog name: {self.name}")


animal = Animal("Cat")
dog = Dog("Bruno")

animal.details()
dog.details()

"""
Output:

Animal name: Cat
Dog name: Bruno

Both classes have a method called:

    details()

But the behavior is different.

Animal -> uses Animal.details()

Dog -> uses Dog.details()

The Dog class inherited from Animal, but it provided its own
implementation of details().

Therefore, Dog's details() overrides Animal's details().
"""


# ============================================================
# 5. WHY METHOD OVERRIDING IS POLYMORPHISM
# ============================================================

"""
Consider this function:

    def show_details(obj):
        obj.details()

The function does not need to know whether obj is an Animal
or a Dog.

Python determines at runtime which details() method should be
called based on the actual object.
"""

def show_details(obj):
    obj.details()


animal = Animal("Cat")
dog = Dog("Bruno")

show_details(animal)
show_details(dog)

"""
This is an example of RUNTIME POLYMORPHISM.

At runtime Python determines:

    Animal object -> Animal.details()

    Dog object -> Dog.details()

Therefore, the same function call:

    obj.details()

can produce different behavior depending on the object.
"""


# ============================================================
# 6. USING super() WITH METHOD OVERRIDING
# ============================================================

"""
Sometimes we do not want to completely replace the parent's
method.

Instead, we want to:

    1. Execute the parent's method.
    2. Add some additional behavior.

For this, we can use super().
"""

class Parent:

    def show(self):
        print("This is the Parent class method.")


class Child(Parent):

    def show(self):
        super().show()
        print("This is the Child class method.")


obj = Child()
obj.show()

"""
Output:

This is the Parent class method.
This is the Child class method.

Here:

    super().show()

calls the show() method of the parent class.

Then the child class adds its own behavior.

Therefore, super() is useful when overriding a method but still
wanting to reuse the parent's implementation.
"""


# ============================================================
# 7. METHOD OVERLOADING
# ============================================================

"""
METHOD OVERLOADING
==================

Method overloading means having multiple methods with the same
name but different parameters.

For example, in some programming languages we can write:

    add(int a, int b)
    add(int a, int b, int c)

and the programming language chooses the correct method based
on the number or type of arguments.

Python does NOT support traditional method overloading.

If we define the same method multiple times, the latest
definition replaces the previous definition.
"""

class Calculator:

    def add(self, a, b):
        return a + b

    # This replaces the previous add() method
    def add(self, a, b, c):
        return a + b + c


calculator = Calculator()

print(calculator.add(1, 2, 3))

"""
The first add() method is no longer available because the second
definition replaced it.

Therefore, this would cause an error:

    calculator.add(1, 2)

because the active add() method requires three arguments.

So Python does not provide traditional method overloading.
"""


# ============================================================
# 8. HOW PYTHON CAN ACHIEVE OVERLOADING-LIKE BEHAVIOR
# ============================================================

"""
Although Python does not support traditional method overloading,
we can achieve similar behavior using:

    - Default arguments
    - *args
    - **kwargs

Example using default arguments:
"""

class Calculator:

    def add(self, a, b, c=0):
        return a + b + c


calculator = Calculator()

print(calculator.add(10, 20))
print(calculator.add(10, 20, 30))

"""
Output:

30
60

Here c has a default value of 0.

Therefore, the same method can work with either two or three
arguments.

This is NOT traditional method overloading.
It is a Python technique that provides similar flexibility.
"""


# ============================================================
# 9. DUCK TYPING
# ============================================================

"""
DUCK TYPING
===========

Duck typing is an important concept in Python.

It is based on the idea:

    "If it walks like a duck and quacks like a duck,
     it must be a duck."

In programming, this means:

We do not necessarily care about the object's class.

We care about whether the object provides the required
behavior or method.

For example, if an object has a speak() method, we can use
that object with a function that expects speak().
"""


class Duck:

    def speak(self):
        print("Duck says: Quack!")


class Human:

    def speak(self):
        print("Human says: Hello!")


def make_it_speak(obj):
    obj.speak()


duck = Duck()
human = Human()

make_it_speak(duck)
make_it_speak(human)

"""
The function make_it_speak() does not check:

    Is this object a Duck?
    Is this object a Human?

It only assumes that the object has a speak() method.

Therefore:

    Duck -> speak() -> Quack!

    Human -> speak() -> Hello!

This is duck typing.

Python focuses on what an object CAN DO rather than what
class the object BELONGS TO.
"""


# ============================================================
# 10. DUCK TYPING WITH DIFFERENT CLASSES
# ============================================================

"""
The classes do not even need to have any relationship with
each other.
"""

class Printer:

    def start(self):
        print("Printer is starting...")


class Computer:

    def start(self):
        print("Computer is starting...")


class Car:

    def start(self):
        print("Car is starting...")


def start_device(device):
    device.start()


printer = Printer()
computer = Computer()
car = Car()

start_device(printer)
start_device(computer)
start_device(car)

"""
All three classes have a start() method.

Therefore, the same function can work with all three objects.

This is duck typing and runtime polymorphic behavior.
"""


# ============================================================
# 11. OPERATOR OVERLOADING
# ============================================================

"""
OPERATOR OVERLOADING
====================

Python also supports polymorphism through operators.

The same operator can behave differently depending on the
data types or objects being used.

For example:

    2 + 3

means addition.

But:

    "Hello " + "World"

means string concatenation.

The same '+' operator performs different operations depending
on the objects.
"""

print(2 + 3)
print("Hello " + "World")

"""
Output:

5
Hello World

The '+' operator has different behavior for integers and
strings.

This is an example of polymorphic behavior.
"""


# ============================================================
# 12. CUSTOM OPERATOR OVERLOADING
# ============================================================

"""
We can also define how operators should behave for our own
classes.

Special methods (also called magic methods or dunder methods)
are used for this.

For example:

    __add__()

controls the behavior of the '+' operator.
"""

class Number:

    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value


num1 = Number(10)
num2 = Number(20)

print(num1 + num2)

"""
When Python sees:

    num1 + num2

it internally uses:

    num1.__add__(num2)

The __add__() method defines how the '+' operator should work
for our Number objects.
"""


# ============================================================
# SUMMARY OF POLYMORPHISM
# ============================================================

"""
POLYMORPHISM
============

Polymorphism means:

    "One interface, many forms."

Important forms of polymorphism in Python:

1. Method Overriding
   ------------------
   A child class provides its own implementation of a method
   inherited from the parent class.

2. Duck Typing
   -------------
   Python focuses on whether an object provides the required
   behavior rather than checking its exact class.

3. Operator Overloading
   ---------------------
   The same operator can behave differently depending on the
   objects or data types involved.

4. Method Overloading
   -------------------
   Python does NOT support traditional method overloading.
   However, similar behavior can be achieved using default
   arguments, *args, and **kwargs.


IMPORTANT TERMS
===============

Polymorphism
    One interface with multiple behaviors.

Method Overriding
    Child class changes the implementation of a parent method.

Duck Typing
    Focus on what an object can do rather than its class.

Operator Overloading
    Defining or using different behavior for operators.

Runtime Polymorphism
    The behavior/method is determined at runtime based on the
    actual object.

super()
    Used to access functionality from a parent class.
"""
