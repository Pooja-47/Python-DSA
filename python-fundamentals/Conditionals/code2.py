# Question practice on conditional statements:

# Q1 Accept two numbers and print the greatest between them.
num1=int(input("Enter any number:"))
num2=int(input("Enter another number:"))

"""==>
if num1>num2:
    print(f"{num1} is greatest.")
else:
    print(f"{num2} is gratest.")
"""

""" But in above program if the user gives both numbers equal as input then also it prints else statement
To overcome this problem we use 'elif' """

if num1>num2:
    print(f"{num1} is greatest.")
elif num2>num1:
    print(f"{num2} is greatest.")
else:
    print("Both the numbers are equal.")
print()

# Q2 Accept gender from user and print a greeting message.

gender=input("Tell your gender(M/F) please:")

if gender=="F" or gender=="f":
    print("Good morning mam")
elif gender=="M" or gender=="m":
    print("Good morning sir")
else:
    print("Others")
print()

# Q3 Accept an integer and check if it is even or odd.

integer=int(input("Enter any integer:"))

if integer % 2 == 0:
    print(f"Given integer {integer} is Even.")
else:
    print(f"Given integer {integer} is Odd.")
print()

# Q4 Accept name and age — check if the user is a valid voter (18+).

name=input("Please tell your name:")
age=int(input("Enter your age:"))

if age >= 18:
    print(f"Congrats {name}! You can vote.") 
else:
    print(f"Sorry {name}! Can't vote yet. You can vote after {18 - age} years.") 
print()

# Q5 Accept a year and check if it is a leap year.

year=int(input("Enter a year:"))

if year % 100 == 0 and year % 400 == 0:
    print(f"Given year is leap year")
elif year % 100 != 0 and year % 4 == 0:
    print("It is leap year")
else:
    print("Not a leap year")
print()

# Q6 — Temperature Ladder
""" Accept temperature in °C and print a description.
- for temp -5 to 5  print very cold
- for 6 to 18 print cold
-for 18 to 30 print hot""" 

temp=float(input("Enter the temperature:"))

if -5<=temp<=5:
    print("Very cold")
elif 5<temp<=18:
    print("Cold")
elif 18<temp<=30:
    print("Hot")
else:
    print(" Temperature not in range")
