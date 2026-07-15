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

# Objects :
"""
We can create multiple objects for same class

Syntax :

variable_name = class_name()

here we called a class in variable outside the class
now the variable_name is an object of class called in it
"""

class Bags:
    name = "BagFactory"
    def details():
        print("This is a factory that manufactures bags")

company = Bags()
reebok = Bags()
"""
The object has all the powers of a class therefore a class
object can access attributes and methods of a class.
"""

print(company.name)
print(reebok.details)

# Access method using object

# CONSTRUCTOR :
"""
A constructor is a method that runs automatically when we
call a class and this constructor function will target the
objects location.

Example :
class Bag:
    def __init__(self)  # here self targets the location of your object.

you can give parameters to the constructor as it is used to take inputs from user. 
"""
class student:
    def __init__(self,name,subject):    # name and subject are parameters.
        print("Student Name:\nSubject:")
student()   # called class
obj = student("xyz","CSE") # creadted object its location is targeted by self
