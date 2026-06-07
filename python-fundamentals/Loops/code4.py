# 2. while loop:-

"""
while loop keeps running as long as the condition is True.
You use it when you don't know how many times you will need to repeat.
"""
# Syntax:
"""
while condition:
    codeblock
"""

# Print 1 to 20
a=1
while a<=20:
    print(a)
    a+=1
print()

# Warning /!\:
"""
Always make sure your condition will eventually become False - 
Otherwise program runs forever:

while True:
    print("Hi")
     
*This is known as "Infinite Loop"
"""

# while loop also supports :
"""
break
continue
else
        Exactly like for loops.
"""

# Practice questions on while loop:-

# Q1 Separate each digit of a number and print on a new line.

num=int(input("Enter any number:"))
while num!=0:
    print(num % 10)      # digits are printed from right to left.
    num=num//10
print()

# Q2 Accept a number and print its reverse.

num=int(input("Enter a number:"))
rev=0
while num!=0:
    rev=rev*10+num%10
    num//=10
print(f"reverse of given number is : {rev}")
print()

# Q3 Check if a number is palindromic (equal to its reverse).

num=int(input("Enter a number:"))
rev=0
copy=num
while num!=0:
    rev=rev*10+num%10
    num=num//10
print(f"reverse of given number is : {rev}")
if rev == copy:
    print("Palindrome")
else:
    print("Not palindrome")
