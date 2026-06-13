# Tuple:
"""
Tuples are ordered collections similar to lists, but they are immutable.
A tuple is exactly like a list, except you cannot change it once created. 
Use tuples for data that should stay constant — like days of the week, coordinates, or config values.
"""
# Syntax:
"""
tuple_name = (value1, value2, value3)
"""
tup1=("Monday","Tuesday",123,567)
print(tup1)
print(type(tup1))
print(tup1,"\n")

# Length of tuple:
print(f"Length of tup1 is: {len(tup1)}")

# Single element tuple

a = (10)
print(type(a))      # int

# A comma is required to create a single-element tuple.
b = (10,)
print(type(b))      # tuple

# Convert list into tuple using tuple function{tuple()}:
fruits=["Apple","Grapes","Banana","Pineapple"]
print(fruits)
print(type(fruits),"\n")

fruits=tuple(fruits)
print(fruits)
print(f"after converting {type(fruits)}\n")

# Properties of tuples:-

# Ordered:
"""Elements maintain the order in which they are inserted:
"""
print(fruits[0])
print(fruits[3])
print(fruits[1],"\n")

# Tuple is immutable:
"""
fruit[0]= "Mango" # gives error same as in strings
"""

# Tuple allows duplicate values.
numbers = (1, 2, 2, 3, 3, 3)
print(numbers,"\n")

# Methods on tuple:
"""
1. index:
gives the index of values stored in tuple
"""
days=("Monday","Tuesday","Wednesday",123,567,123,123,123)
print(days)
print("Index of wednesday:",days.index("Wednesday"))
print("Index of 123:",days.index(123),"\n")  # gives index of first occurance

"""
2. count:
counts the number of occurrences
"""
days=("Monday","Tuesday","Wednesday",123,567,123,123,123)
print(days)
print("Number of times 123 occurred:",days.count(123),"\n")

# Slicing on tuples:
"""
It works same as strings and lists on tuples.
"""
fruits=(1,"Mango",2,"Grapes",3,"Apple",4,"Pineapple")
print(fruits)
print(f"slicing from 1 to 3: {fruits[1:4]}")  # prints values at index 1,2,3

days=("Sun","Mon","Tue","Wed","Thu","Fri","Sat")
print(days)
print(f"slicing from 0 to 7:{days[:7]}")

print(f"slicing in reverse: {days[::-1]}\n")

# Membership operators:
"""

1. in: It returns True if tuple contains given value.
2. not in: It returns True if tuple does not contain given value.
"""
days=("Mon","Tue","wed")

print(f'"tue" in days: {"tue" in days}')   # False as days contain "Tue" not "tue"
print(f'"wed" in days: {"wed" in days}')   # True
print(f'"Thu" not in days: {"Thu" not in days}\n')  # True


# Real life usecase of tuple:
""" Tuple packing and unpacking:
"""
# A function that returns set of information:

# Packing-
def student():
    return "Alex", 20, "alex@example.com"  

# return statement returns the values in it at the place where function is called
# python takes the information as tuple automatically.

student()  # function called it returns the given information here we can store it in a variable
info=student()
print(info,"\n")

# Unpacking-
"""
def student():
    return "Alex", 20, "alex@example.com"
"""

name,age,mail = info
print(name)   # Alex
print(age)    # 20
print(mail)   # alex@example.com