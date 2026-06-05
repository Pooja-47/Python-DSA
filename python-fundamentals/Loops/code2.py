# 1. for loop:-

""" Before starting we need to understand range function:

*range() generates a sequence of numbers
think of it as saying-
           "Counting from here to there"

range(start,stop,step)   # prints from starting digit to (stop digit - 1)
default start=0
default step=1
There is no default value for stop you will have to mention it manually always and increase actual stop by 1.
"""
""" # Create range for:
1. 10 - 100
2. 23 - 56
3. 0 - 45
"""
#1
range(10,101,1)
#2
range(23,57,1)
#3
range(0,46,1) 
range(46)   # prints from 0 upto stop-1

# Syntax: for loop
""" 
It follows indentation as the control statements.

# Numbers:
for i in range(start,stop,step):
    print(i)
    
where:
for and in: keywords
i: variable 
range(): function 

"""
for i in range(46): # start=0 stop=45(46-1) step=1
    print(i)
print()
for i in range(10,100,10):
    print(i)
print()

# To print table of 5:
for i in range(5,(5*10)+1,5):
    print(i)
print()

# print table of any input value:
n=int(input("Enter the number of which table you want to print:"))
for i in range(1,11,1):
    print(f"{n} x {i} = {n*i} ")
print()

# for loop on strings:
"""1. directly on string:"""

string="Students"
for i in string:
    print(i)
print()

"""2. using indexing:"""
# we use range functions because indexing is done in numbers
# len() it is a function usd to print the length of string

string="Students"
for i in range(0,len(string),1):   # len(string) = 8  so for loop runs for (stop-1) 7 times 
    print(f"{i} : {string[i]}") 
print()


"""There are some conditions used in loops:
1. break = completely stops the loop and gets out of it
2. continue = skips one iteration
3. else = it works with break (if break runs else don't run and vice versa)
"""   
# 1. break
for i in range(1,11,1):
    if i==4:
        break
    print(i)
print()

# 2. continue
for i in range(1,11,1):
    if i==4:
        continue
    print(i)
print()

# 3. else : it works with break
for i in range(1,11,1):
    if i==4:
        break
    print(i)
else:
    print("No break encountered")
print()

for i in range(1,11,1):
    if i==12:
        break
    print(i)
else:
    print("No break was encountered")
