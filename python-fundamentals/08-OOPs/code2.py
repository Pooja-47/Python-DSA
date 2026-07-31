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

# ------------------------------------------------------------

# TYPES OF ATTRIBUTES AND METHODS

"""
Python mainly has two types of attributes.

1. Class Attribute
   A variable that is created directly inside the class is called
   a class attribute.

   - Shared by all objects of the class.
   - Stored only once in memory.

2. Instance Attribute
   A variable created using self inside the constructor or an
   instance method is called an instance attribute.

   - Each object has its own separate copy.
   - Can have different values for different objects.
"""

class Year:
    birth_year = 2009      # Class Attribute

    def __init__(self, leap_year):
        self.leap_year = leap_year      # Instance Attribute

obj = Year(2000)

print(obj.birth_year)
print(obj.leap_year)

# Instance attributes can be modified using an object
obj.leap_year = 2004
print(obj.leap_year)

# ------------------------------------------------------------

# CLASS ATTRIBUTE VS INSTANCE ATTRIBUTE

"""
Class Attribute
---------------
Created directly inside the class.

Example:
birth_year = 2009

Access:
obj.birth_year
Year.birth_year

Instance Attribute
------------------
Created using self.

Example:
self.leap_year = leap_year

Access:
obj.leap_year

Only the instance attribute of that particular object changes.
The class attribute remains the same.
"""

# ------------------------------------------------------------

# TYPES OF METHODS

"""
Python mainly has three types of methods.

1. Instance Method
   - Works with an object of the class.
   - Can access and modify instance attributes.
   - Takes self as the first parameter.

2. Class Method
   - Works with the class itself.
   - Can access and modify class attributes.
   - Created using @classmethod.
   - Takes cls as the first parameter.

3. Static Method
   - Does not automatically receive the object or the class.
   - Created using @staticmethod.
   - Behaves like a normal function placed inside a class.
"""

class Animal:

    species = "Lion"      # Class Attribute

    def __init__(self, name):
        self.name = name      # Instance Attribute

    # ---------------- Instance Method ----------------

    def instance_method(self):
        print("This is an instance method.")
        print(f"Animal name : {self.name}\\n")

    # ---------------- Class Method ----------------

    @classmethod
    def class_method(cls):
        print("This is a class method.")
        print(f"Species : {cls.species}\\n")

    # ---------------- Static Method ----------------

    @staticmethod
    def static_method():
        print("This is a static method.")
        print("It does not access class or instance attributes.\\n")

obj = Animal("Simba")

obj.instance_method()
obj.class_method()
obj.static_method()

# ------------------------------------------------------------

# IMPORTANT DIFFERENCE

"""
Method Type       First Parameter     Can Access
---------------------------------------------------------
Instance Method   self                Instance + Class attributes
Class Method      cls                 Class attributes
Static Method     None                Neither self nor cls automatically

Example:
obj.instance_method()
Animal.class_method()
Animal.static_method()

Remember:
- self refers to the current object.
- cls refers to the class itself.
- A static method behaves like a normal utility function.
"""