# Creating first class :
"""
Syntax:

class class_name:
    block of code

Here class is keyword

Inside our class we store Attributes and Methods:

Attributes :
    Variables defined inside the class are known as Attributes.

Methods : 
    Functions defined inside a class are known as Methods.
"""
class Car:
    brand = "Toyota"

class Animal:
    species="Dog"  # Attribute

    def make_sound():    # Method
        print("bark")

# ------------------------------------------------------------

# Accessing class attributes and methods:
"""
A class is initialised only one time when we first run the
program. and for accessing the attributes and methods we
have to first access the class and then attributes and
methods.
"""
# directly accessing attributes and methods using class

print(Animal.species)   # accessing attribute
Animal.make_sound()     # accessing methods

# ------------------------------------------------------------

# OBJECTS
"""
An object is an instance of a class.

A single class can have multiple objects.
Each object has its own identity and can access the
attributes and methods defined inside the class.

Syntax:

object_name = ClassName()

Example:
student1 = Student()
student2 = Student()

Here, student1 and student2 are two different objects
created from the same Student class.
"""

class Bags:
    company = "BagFactory"

    def details():
        print("This factory manufactures bags.")

company = Bags()
reebok = Bags()

print(company.company)

"""
Notice that the method cannot be called using an object
because it does not accept the object's reference.

company.details()   # Gives an error
"""

# ------------------------------------------------------------

# SELF KEYWORD

"""
The 'self' keyword represents the current object.

Whenever an object calls a method, Python automatically
passes that object's reference as the first argument.

Therefore, every instance method must have 'self' as its
first parameter.

Syntax:

def method_name(self):
    ...
"""

class Bags:
    company = "BagFactory"

    def details(self):
        print("This factory manufactures bags.")

company = Bags()
reebok = Bags()

company.details()
reebok.details()

# ------------------------------------------------------------

# CONSTRUCTOR

"""
A constructor is a special method that is executed
automatically whenever an object is created.

In Python, the constructor is written using:

__init__()

It is mainly used to initialize object data.

Syntax:

class Student:
    def __init__(self):
        ...

A constructor can also receive parameters.
"""

class Student:

    def __init__(self, name, subject):
        print(f"Student Name : {name}")
        print(f"Subject      : {subject}")

Student("Pooja", "PCM")
obj = Student("Kritika", "CSE")

# ------------------------------------------------------------

# WHY DO WE USE SELF?

"""
The 'self' keyword allows each object to store and access
its own data.

Suppose we create multiple Student objects.

Each student has a different name and subject.

Using self, these values are stored separately for every
object.

Without self, Python would not know which object's data
is being referred to.
"""

class Student:

    def __init__(self, name, subject):
        self.name = name
        self.subject = subject

student1 = Student("Priyanka", "PCM")
student2 = Student("Kritika", "CSE")

print(student1.name)
print(student2.subject)

"""
Output:

Priyanka
CSE
"""

# ------------------------------------------------------------

# IMPORTANT POINTS

"""
1. Class
   A blueprint used to create objects.

2. Object
   A real instance of a class.

3. self
   Refers to the current object.

4. __init__()
   Constructor that runs automatically whenever an object
   is created.

5. self.variable = value
   Stores data inside a particular object.

Example:

student1.name = "Priyanka"
student2.name = "Kritika"

Both objects have their own independent data.
"""


