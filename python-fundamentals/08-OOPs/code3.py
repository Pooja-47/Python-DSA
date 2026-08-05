# The four pillars of OOPs in detail :

""" 
1.  ** Inheritance **
    -It works between classes
    -Inheritance allows a class (child class) to inherit properties and
    behaviors (attributes and methods) from another class (parent class).

**Benefits of using inheritance is 
 -Code reusabilit2
 -Organized structurH
 -Easy to maintain and extend
"""

# Syntax :

"""
Syntax is very simple just like you take parameters in functions
here you will take parameters but those parameters will be
classes.

class class_name:        # this is parent class
    code
class class_name(Parent class_name):    # this is inhereted or child class
    code
"""

class Parent:
    a=123
    def speak(self):
        print("Hii, I am Parent class method tell me your name")

class Child(Parent):
    def reply(self):
        print("Hello, My name is child class method")

obj = Parent()
obj1 = Child()

"""
Now the inherited class has all the powers of parent class that
means all the methods, attributes can be accessed by the
instance of child class as well.
"""

# Accessing attributes and methods using instance of Parent class :
""" We can only access those which are defined in parent class.  """
print(obj.a)
obj.speak()

# Accessing attributes and methods using instance of Child class
""" We can access both defined in parent and child class. """
print(obj1.a)
obj1.speak()
obj1.reply()

# Constructor in Inheretance :-

"""
Lets say you have created a parent class with a constructor
function inside it and then this class is inherited by another class
then the constructor function of parent class will work for the
child class as well.
"""

class Parent:
    def __init__(self,name):
        self.name=name

class Child(Parent):
    def say(self):
        print(f"Hello, My name is {self.name}")


obj2 = Child("bachha")    # The parameter given is initialised in parent class as it is defined in parent not child class
obj2.say()


"""
Now lets say you need a new parameter in your child class you
have to create a constructor function for your child class but the
parameters that can be initialized in the parent class will be
initialized using the super() function. Super function will target the
parent class.
"""
class BagFactory:
    def __init__(self,material,zips,pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def details(self):
        print("Your bag details are :")
        print(self.material)
        print(self.zips)
        print(self.pockets)

class Reebok(BagFactory):
    def __init__(self, material, zips, pockets,color):   # these parameters are initialized in parent class
        super().__init__(material, zips, pockets)
        self.color = color   # Here color is new parameter so initialized seperately

    def details(self):
        print(self.color)
        return super().details()
        

R1 = Reebok("Polyster",10,5,"Black")
R1.details()
BF = BagFactory("leather",4,2)
BF.details()
