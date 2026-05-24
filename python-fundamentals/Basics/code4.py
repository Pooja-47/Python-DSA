#  INPUT, OUTPUT and OPERATORS::-
# OUTPUT
"""
For generating output we use print function
"""

print("Hello! how are you?")  # output is given string
name="Pooja"
age=20
print(name)  # output is value stored in name
print(age,"/n")   # output is value stored in age

""" Using formated string:
  syntax:- print(f"text.. {variable name} text... {variable name} ")"""

print(f"Hello! My name is {name} and my age is {age}")   # f-string

""" Another way is seperating text and variable names by coma(,)"""

print("hello! My name is",name,"and my age is",age,"\n")  # multiple values

# INPUT:-
""" *Taking input from user. 
*We use input() function
*This always returns a string
  bcoz string can hold every type of values(numbers, alphabets, special characters, boolean values)
*If we want output in datatype other than string ,
  convert it manually(Explicit type conversion) 
*If the datatype is not defined explicitly input can take any datatype value,
   else it takes the defined datatype value
"""

input("Enter password:") # this input can be stored in any variable as
passwrd = input("Enter password:") 

name=input("What is your name:")  # takes any datatype but always returns string,
#name is a string so no need of conversion

age=input("Enter your age:") # returns string but age is an integer or float So,
age=float(input("Enter your age:")) # always takes and returns number as input not string

print(f"Welcome! {name}, you are {age} years old","\n")

# OPERATORS:-
"""" Used to perform mathematical operations.
"""
# 1. ARITHMETIC Operators:
"""
*Addition(+): add numbers (flaot, integers etc)
*Subtraction(-): subtract numbers 
Multiplication(): product
*Division(/): returns quotient (always float value)
*Floor division(//): return quotient (always integer value)
Exponential(*): power
*Modulus(%): returns remainder (integer value)
"""

a=20
b=25
print(a+b+12+43+34)
print(a-b-20)
print(a*2*5)
print(a/10) # 2.0 if we want integer value use floor division or explicit conversion as
print(int(a/10), a//10)  # 2, 2
print(2*2 , a*1)  # 2^2==4, 20^1==20
print(a % 5,"\n") # 0

""" Priority order for arithmetic operations:
()- Brackets
**- Exponential
*, /, //, %  all at same priority, So moving left to right the operator which comes first solved first
+, - left to right whichever comes first solved first
"""

print(3 + 4 * 2)  # Multiplication(*) first as its priority is higher than addition(+)
print(15 // 4 + 15 % 4) # // , % same priority reading from left to right // first then % then +(least priority)
print(3 + 2 * 5 * 2 - 1,"/n") ## first * then * then + and -(left to right)

# 2. COMPARISION operators:
""" 
*To compare various values
*Always return boolean values True orr False
(==)equals to: results true if values given are equal
(<) less than: returns true if left value is smaller than the right side value
(>) greater than: True if left side value is greater
(>=) greater than equal to: True if left ualue is greater than or equal to right value
(<=) less than equal to: True if left ualue is less than or equal to right value
(!=) not equal to: True if given values are not equal
"""
a=20
b=15
print(a>b)  # True
print(b>=a)  # False
print(a==20)  # True
print(a!=b,"/n") # True

# 3. LOGICAL Operators:-
"""
* When we compare multiple values at a time in combined form.
* Multiple comparisions at a time.
1. and: when both conditions True returns True.
2. or: any one condition True returns True.
3. not: reverses the result if True gives False and vice-versa.
"""
print((5 > 3 and 10 == 10) or (4 != 4 and 2 < 1)) # True
      # (T    and    T )     or   (F    and   F)
      #        T          or           F
      #                  T
print((10 == 10 and 23 != 23) or (34 == 12 and bool("hello"))) # False
      #  (T     and     F)    or   (  F      and     T)
      #          F            or              F
      #                       F
print( not(5 == 5 and 3 != 4) or (10 > 20),"/n") # False
      # not( T    and     T)   or ( F )
      # not(    T    )   or ( F )
      #         F      or       F
      #                F

# 4. ASSIGNMENT Operators:-
""" To assign values to variables.
* assignment(=): simply assign value to variable.

# perform operation and then assign resulting value to the same variable---
   * add and assign(+=)
   * subtract and assign(-=)
   * Multiply and assign(*=)
   * Divide and assign(/=)
   * Exponent and assign(**=)
   * Modulas and assign(%=)
   * Floor division and assign(//=)
"""
a=20
a += 12 # a = a + 12 == a = 20 + 12 (Now a = 32)
a -= 20 # a=0
a *= 4 # a=80  all others in the same way