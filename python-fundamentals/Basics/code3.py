#  STRINGS and TYPE CONVERSION::--

## STRINGS:-
"""
*As we studied String is a datatype for anythying (alphabets, numbers, special characters, alphanumerics)
 written in quotes(single orr double)
*Takes more memory than integrs because each character in string is stored with it's own Unicode number
"""
#*We can see the unicode number of any character using ord function-
print(ord("A")) # Stored as 65 so this prints 65
print(chr(65),"/n")   # prints character using unicode (A)

#  *Indexing in strings:-
""" 1. Every character in string has position number called index
2. Positive indexing:- left to right (from 0 to +ve infinity) 
3. Negative indexing:- right to left (from -1 to -ve infinity)

For example:-     H  E  L  L  O  
                  0  1  2  3  4  -- +ve indexing
                 -5 -4 -3 -2 -1  -- -ve indexing
"""

a="Hello"

print(a)
print(a[0],a[-1])  # prints H o
print(ord(a[2]),"/n")    # prints unique number of character at index 2 in string stored in a

#  *Slicing in strings:-
""" 
*To print a required part of string not the complete string
*Spaces are also assigned index

*syntax : stringname[start index : stop index + 1 : steps] 
    start index is included, stop index is excluded

*default start is 0 (if we won't give any starting index it will be 0 by default)
*default stop is end index of string (length of string)
*default step is 1

"""

b="COLLEGE"
print(b[3:6:1]) # prints L  E  G
                     #   3  4   5  +ve indexing steps increase by 1

print(b[0:7:2]) # prints C L E E  steps increase by 2

x="Hello how are you"

print(x[6:9:1])  # spaces also included in indexing
print(x[14: :1])
print(x[ :5:1],"/n")

#  TYPE CONVERSION::-
""" 
*Converting one datatype into another using built in functions.
  1. Implicit Conversion: automatically by interpretor
  2. Explicit Conversions: manually by the user using built in functions

*For Explicit conversion we use these built-in functions
  1. int() : convert only float and valid integer strings to integers
           * example: a="hello" , a="45.5"
                     these cannot be converted to integer as these strings do not hold valid integers
  2. float() : all integers orr integer/float strings to float
  3. str() : any datatype to string
  4. bool() : any datatype to boolean
            * These 7 values are False and all others are True
              1. False
              2. 0
              3. 0.0
              4. "" empty string
              5. [] empty list
              6. {} empty dictionary
              7. () empty tuple
  
"""

# Implicit Conversion:-
x=24  # int
y=6    # int
print((x/y))   # result is float
print(type(x/y),"/n")

#  ALL EXPLICT CNVERSIONS
# 1. int():-
a= "12"
print("before type conversion a is:",a,type(a))
a=int(a)
print("after type conversion a is:",a,type(a),"\n")

b=12.5
print("before type conversion b is:",b,type(b),"\n")
b=int(b)
print("after type conversion b is:",b,type(b),"\n")

# 2. float:-
x=22
print("before type conversion x is:",x,type(x))
x=float(x)
print("after type conversion x is:",x,type(x),"\n")

y="22.45"
print("before type conversion y is:",y,type(y))
y=float(y)
print("after type conversion y is:",y,type(y),"\n")

z="20"
print("before type conversion z is:",z,type(z))
z=float(z)
print("after type conversion z is:",z,type(z),"\n")

# 3. str():-

a=134
print("before type conversion a is:",a,type(a))
a=str(a)
print("after type conversion a is:",a,type(a),"\n")

b=2.0
print("before type conversion b is:",b,type(b))
b=str(b)
print("after type conversion b is:",b,type(b),"\n")

c=2+3j
print("before type conversion c is:",c,type(c))
c=str(c)
print("after type conversion c is:",c,type(c),"\n")

d=True
print("before type conversion d is:",d,type(d))
d=str(d)
print("after type conversion d is:",d,type(d),"\n")

# 4. bool()

a=False
print("before type conversion a is:",a,type(a))
a=bool(a)
print("after type conversion a is:",a,type(a),"\n")

b=True
print("before type conversion b is:",b,type(b))
b=bool(b)
print("after type conversion b is:",b,type(b),"\n")

c=0.0
print("before type conversion c is:",c,type(c))
c=bool(c)
print("after type conversion c is:",c,type(c),"\n")

d=12
print("before type conversion d is:",d,type(d))
d=bool(d)
print("after type conversion d is:",d,type(d),"\n")

e=0
print("before type conversion e is:",e,type(e))
e=bool(e)
print("after type conversion e is:",e,type(e),"\n")

f=12.80
print("before type conversion f is:",f,type(f))
f=bool(f)
print("after type conversion f is:",f,type(f),"\n")

g="hello"
print("before type conversion g is:",g,type(g))
g=bool(g)
print("after type conversion g is:",g,type(g),"\n")