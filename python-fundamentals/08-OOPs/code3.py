# THE FOUR PILLARS OF OOP (Object-Oriented Programming)

# 1. INHERITANCE

"""
Inheritance is a mechanism in which one class acquires the
properties and behaviors (attributes and methods) of another class.

The class whose properties are inherited is called the Parent Class
(or Base Class), and the class that inherits them is called the Child
Class (or Derived Class).

Inheritance works between classes.

Benefits of Inheritance:
1. Code Reusability
2. Better Code Organization
3. Easy Maintenance
4. Easy Extension of Existing Code

Example:
If many classes require the same functionality, we can define that
functionality once in a parent class and reuse it in multiple child
classes.
"""

# ------------------------------------------------------------
# SYNTAX OF INHERITANCE

"""
Syntax:

class ParentClass:
    code

class ChildClass(ParentClass):
    code

The child class automatically receives the accessible attributes
and methods of the parent class.
"""

# ------------------------------------------------------------
# BASIC EXAMPLE OF INHERITANCE

class Parent:

    value = 123      # Class Attribute

    def speak(self):
        print("Hi, I am a method of the Parent class.")


class Child(Parent):

    def reply(self):
        print("Hello, I am a method of the Child class.")


parent_obj = Parent()
child_obj = Child()

"""
The Child class inherits all accessible members of the Parent class.

Therefore, a Child object can use both Parent and Child methods.
"""

# ------------------------------------------------------------
# ACCESSING MEMBERS USING A PARENT OBJECT

"""
A Parent object can access only the members defined in the
Parent class.
"""

print(parent_obj.value)
parent_obj.speak()

# ------------------------------------------------------------
# ACCESSING MEMBERS USING A CHILD OBJECT

"""
A Child object can access:

1. Members inherited from the Parent class.
2. Members defined inside the Child class.
"""

print(child_obj.value)
child_obj.speak()
child_obj.reply()

# ------------------------------------------------------------
# CONSTRUCTOR IN INHERITANCE

"""
If the Child class does not define its own constructor, then the
constructor of the Parent class is automatically executed.

This allows the Child class to initialize data using the Parent
constructor.
"""

class Parent:

    def __init__(self, name):
        self.name = name


class Child(Parent):

    def introduce(self):
        print(f"Hello, my name is {self.name}.")


student = Child("Kriti")
student.introduce()

"""
Explanation:

The Child class has no constructor of its own.

When Child("Kriti") is created, Python automatically calls the
Parent constructor.

Therefore, self.name is initialized in the Parent class.
"""

# ------------------------------------------------------------
# USING super() IN INHERITANCE

"""
Suppose the Child class requires an additional parameter that is
not present in the Parent class.

In that case, the Child class creates its own constructor.

The parameters belonging to the Parent class are initialized using
super().__init__().

super() refers to the Parent class.
"""

class BagFactory:

    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def details(self):
        print("Bag Details:")
        print(f"Material : {self.material}")
        print(f"Zips     : {self.zips}")
        print(f"Pockets  : {self.pockets}")


class Reebok(BagFactory):

    def __init__(self, material, zips, pockets, color):

        # Initialize Parent class attributes
        super().__init__(material, zips, pockets)

        # Initialize Child class attribute
        self.color = color

    def details(self):
        print(f"Color    : {self.color}")
        super().details()


r1 = Reebok("Polyester", 10, 5, "Black")
r1.details()

print()

bf = BagFactory("Leather", 4, 2)
bf.details()

"""
Explanation:

The Parent constructor initializes:

material
zips
pockets

The Child constructor initializes:

color

super().__init__() prevents duplication of Parent class code.
"""

# ------------------------------------------------------------
# TYPES OF INHERITANCE

# 1. SINGLE INHERITANCE

"""
Single Inheritance means one Child class inherits from one
Parent class.

Parent
   |
Child
"""

class Parent:

    def __init__(self, name):
        self.name = name


class Child(Parent):

    def display(self):
        print(f"My name is {self.name}.")


obj = Child("Cheeku")
obj.display()

# ------------------------------------------------------------
# 2. MULTILEVEL INHERITANCE

"""
Multilevel Inheritance means a class is derived from another
derived class.

GrandParent
      |
   Parent
      |
    Child

Attributes and methods are passed through every level.
"""

class GrandParent:

    def __init__(self, name):
        self.name = name


class Parent(GrandParent):

    def __init__(self, name, age):

        # Initialize GrandParent attribute
        super().__init__(name)

        # New attribute of Parent
        self.age = age


class Child(Parent):

    def __init__(self, name, age, gender):

        # Initialize Parent attributes
        super().__init__(name, age)

        # New attribute of Child
        self.gender = gender

    def show(self):
        print(f"I am a {self.gender}. My name is {self.name} and my age is {self.age}.")


obj = Child("Aarav", 22, "Male")
obj.show()

"""
Explanation:

GrandParent provides: name
Parent adds: age
Child adds: gender

The Child object can access all three attributes.
"""

# ------------------------------------------------------------
# 3. MULTIPLE INHERITANCE

"""
Multiple Inheritance means one Child class inherits from
more than one Parent class.

Parent1      Parent2
     \\        /
      \\      /
        Child

The Child class receives attributes and methods from both parents.
"""

class Parent1:

    def __init__(self, name):
        self.name = name


class Parent2:

    def __init__(self, age):
        self.age = age


class Child(Parent1, Parent2):

    def __init__(self, name, age):

        # Call constructors of both Parent classes
        Parent1.__init__(self, name)
        Parent2.__init__(self, age)

    def display(self):
        print(f"My name is {self.name} and my age is {self.age}.")


obj = Child("Riya", 23)
obj.display()

"""
Explanation:

Parent1 initializes: name
Parent2 initializes: age

Both constructors are called explicitly, so the Child object receives
data from both Parent classes.
"""

# ------------------------------------------------------------
# METHOD RESOLUTION ORDER (MRO)

"""
In multiple inheritance, Python follows a specific order to search
for attributes and methods.

This order is called Method Resolution Order (MRO).

Example:

class Child(Parent1, Parent2)

Python searches in this order:

Child → Parent1 → Parent2 → object

If both Parent classes contain a method with the same name,
Python uses the method from the class that appears first in the
inheritance list.
"""

# ------------------------------------------------------------
# IMPORTANT POINTS

"""
1. Inheritance allows one class to reuse the code of another class.

2. A Child class automatically inherits accessible attributes and
   methods from the Parent class.

3. If the Child class does not define a constructor, the Parent
   constructor is executed automatically.

4. super() is used to call methods or constructors of the Parent
   class from the Child class.

5. Multiple inheritance allows a Child class to inherit from more
   than one Parent class.

6. Python follows Method Resolution Order (MRO) to decide the
   order in which classes are searched.
"""

