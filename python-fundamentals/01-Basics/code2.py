#   DATA TYPES::--

""" * In Python every value has a type not variables.
* You don't need to declare datatype (like in C, C++ etc) python figures it automatically.
* Datatypes tell what kind of data it is and what operations can be performed on it. 
"""

# *Different Datatypes:-
"""
1. int: it is for integers [-ve infinity to -1] and [0 to +ve inffinity]
2. float: it is for decimal numbers both +ve and -ve 
3. complex: it is for (real + imaginary) numbers
4. str: it is for text(strings) in quotes(single or double)
      String example:- {Name= 'Pooja said,'Helllo''} -- this gives error so we can use quotes as:"
                       1. Name= 'Pooja said,"Hello"'
                       2. Name1= "Pooja said,'Hello'"
5. bool: True and False (boolean data types)
6. NoneType: represents nothing (None)
"""
# *To print the type of data we use type function as below:--

x=20
y=-20.9
z=12/3 # the result is 4.0 (not 4 an integer) float in p/q form
result="x+y" # x and y are in double quotes so treated as string not variables
comp_num=2+3j
a=True
b=None

print(type(x))
print(type(y))
print(type(z))
print(type(result))
print(type(comp_num))
print(type(a))
print(type(b))
print(x==20)  # returns boolean type either True or False
print(type(x+y)) # the value of x+y is float