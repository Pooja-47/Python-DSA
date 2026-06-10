#  Parameters and Arguments in functions:
"""
* Parameters: Variables in the function definition that act as placeholders for values.
* Arguments: The actual value you pass when calling the function.
"""

def addition(a,b):   # Here, a and b are parameters.
    print(a+b)

addition(66,44)     # The values 66 and 44 are arguments for a and b, respectively.
addition(1234567890,3456674532378)

# Palindrome Checker using Functions (Parameters and Arguments)

def palindrome_checker(num):
    copy=num
    rev=0
    while num>0:
        rev=rev*10+num%10
        num=num//10
    if copy==rev:
        print(f"{copy} is a palindrome number.")  
    else:  
        print(f"{copy} is not a palindrome number.")    

palindrome_checker(121)   # a= 121
palindrome_checker(123)   # a= 123
palindrome_checker(111)    # a= 111
palindrome_checker(141)     # a= 141

# Common ways of passing arguments:
"""
1. Positional arguments
2. Default arguments
3. Keyword arguments
"""

# Positional Arguments: 
"""
- Number of Parameters must be = Number of Arguments.
- First argument = First parameter, second argument = Second parameter
- All parameters must receive arguments; otherwise, Python raises an error.

"""
def multiply(a,b,c):
    print(a*b*c)

multiply(1,2,3)  # a=1 b=2 c=3
multiply(4,5,6)  # a=4 b=5 c=6
# multiply(1,2)   This gives error as a=1 b=2 but value missing for c


# Default Arguments:
"""
- Values are assigned to parameters at the time of function definition.
- There can be any number of non-default parameters before a default parameter.
- Once a parameter is given a default value, all parameters that follow must also have default values.
- The parameter with default value does not need an argument while calling the function.
"""

def subtraction(a,b,c=2):
        # def subtraction(a,b=2,c=4,d,e)  This gives error
    print(b-a-c)

subtraction(8,5)    # a=8 b=5 and already c=2
subtraction(9,4,1)   # a=9 b=4 c=1 (overwrites the default value of c)

# Keyword Argument:
"""
- This is done at the time of calling a function.
- Here we can give arguments to parameters as we want (not in ordered form as in positional)
- Once a keyword argument is used, all arguments that follow must also be keyword arguments.

"""

def multiplication(a,b,c):
    print(a*b*c)

multiplication(b=3,c=4,a=2)
multiplication(4,b=3,c=2)

# multiplication(4,5,a=3) this gives error as a is already given first value goes to a a=4
# multiplication(b=4,4,c=1) gives an error because a positional argument cannot follow a keyword argument.