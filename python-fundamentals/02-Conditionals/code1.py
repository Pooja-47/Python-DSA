# CONDITIONAL Statements::-
""" -> These statements are used to make decisions in code.
-> The real programs don't run the same code everytime-they make dicisions.
    Real programs are designed to respond to different situations dynamically.
-> Conditional statements let your program choose what to do based on a condition.
-> They are also called control flow statements.

Various conditional statements:
1.if
2.if-else
3.if-elif"""

# 1. if:
"""
*Syntax-  
if condition :
    statement block

-> condition always returns boolean datatype either True or False.
-> if block runs when the condition is true otherwise the interpretor skips if block.
-> Python uses indentation (spaces or tabs at the beginning of a line)
   to identify which statements belong to a block.
-> All statements inside the same block must have the same indentation level.
"""
if True:
    print("Hello") # the condition is true, if block runs (prints Hello)

if False:
    print("Nothing") # condition is false, so the if block is skipped by interpretor (no output)

if (5 > 3 and 10 == 10) or (4 != 4 and 2 < 1) :
    print("Hello, how are you?") # condition returns True, so if block runs (prints Hello, how are you?)

if not(5 == 5 and 3 != 4) or (10 > 20):
    print("bye") # condition returns False, if block is skipped.

"""# Q1. Take age as input and tell if a person can vote or not-

==>
age=int(input("Enter your age:"))
if age>=18:
    print("You can vote,:)")
    

*This only prints when someone can vote but not for those who can not vote(age less than 18).-
-> one way for this is writing print statement outside the if block. BUT
  this statement runs everytime even the condition is true or false because
   it is not the part of if block.
-> The interpretor runs code line by line so it will always print this statement 

==> print("You can not vote.") # This is open statement not control flow statement


-> To solve the above issue we have 
else statement:

# 2. else:
-> No condition required.
-> It runs only when if statement do not run.
-> It is always written after if , it can not be written alone.
-> Both if and else statements never run together always only one of them runs at a time.
-> So for above problem--

==> 
else:
    print("You can not vote")"""

# 2. if-else:

# Q1. Take age as input and tell if a person can vote or not-

age=int(input("Enter your age:"))
if age>=18:
    print("You can vote :)")
else:
    print("You cannot vote :(")

# 3. if-elif ladder:
""" We use this if there are more than 2 conditions.
we can write many elif statements as per our requirement.
For example:
you ask your mom for money to eate something and there are three options:
1 she gives 10 rupee note for this you buy a kurkure packt
2 a 50 rupee note, you will buy kurkure + pepsi
3 100 rupee note, buy a mini pizza"""

rupees=int(input("Enter the amount:"))
if rupees==10:
    print("Eat kurkure :)")
elif rupees==50:
    print("Eat kurkure + pepsi ;)")
elif rupees==100:
    print("Eat pizza <3")
elif rupees==500:
    print("Woooou! parrtttyyy!!!")
else:
    print("Stay hungry! :'( ")

# IMPORTANT NOTES:__
"""
==>

Python does not use {} like many other programming languages.
Instead, it uses indentation to define blocks of code.

Example:

if True:
    print("Inside block")  

print("Outside block")  

==>
if condition:
    runs when condition is True.

elif another-condition:
    runs if the above was False, this is True.

else:
    runs when nothing above is true

==>
if   use: when you have one condition to check

if-else    use: two paths-- True or False 

if-elif-else   use: multiple conditions checked one by one

==>
==>
In an if-elif-else ladder, only one block runs at a time.
Once a True condition is found, Python executes that block and skips the remaining elif and else blocks.

==>
Priority order:-
if : True then execute otherwise move to elif or else 

1st elif : True then execute otherwise next elif... so on
2nd elif
3rd elif.... so on

else : at last priority"""