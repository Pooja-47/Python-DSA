# 1. for loop practice questions:-

#Q1 Print "Hello World" n times.

n=int(input("Enter number:"))
for i in range(n):
    print("Hello world")
print()


a="Students"
for i in range(len(a)):
    print(a)
a="College"
print(ord(a[2]))

print()

#Q2 Print natural numbers from 1 to n.

n=int(input("Enter number:"))
for i in range(1,n+1):
    print(i)
print()

#Q3 Reverse for loop — print n down to 1.

n=int(input("Enter number:"))
for i in range(n,0,-1):
    print(i)
print()

#Q4 Print the multiplication table of a number

n=int(input("Enter number:"))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")
print()

#Q5 Sum of first n natural numbers.

n=int(input("Enter number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i
print(sum)
print()

#Q6 Factorial of a number.

n=int(input("Enter number:"))
fact = 1
for i in range (n,0,-1):
    fact = fact * i
print(fact)
print()

#Q7 Print sum of all even and odd numbers in a range separately.

n=int(input("Enter number:"))
sumE=0
sumO=0
for i in range(1,n+1):
    if i % 2==0:
        sumE=sumE+i
    else:
        sumO=sumO+i
print("Even Sum =",sumE)
print("Odd sum =",sumO)
print()

#Q8 Print all factors of a number.

n=int(input("Enter number:"))
for i in range(1,n+1):
    if n % i == 0:
        print(i)
print()

#Q9 Check if a number is perfect (sum of factors = the number itself).

n=int(input("Enter number:"))
sumF=0
for i in range(1,n):
    if n % i == 0:
        sumF=sumF+i
if sumF == n:
    print(f"{n} is a Perfect Number")
else:
    print("Not Perfect")
print()

#Q10 Check if a number is prime.

n=int(input("Enter number:"))
count=0
for i in range(1,n+1):
    if n % i == 0:
        count=count+1
if count==2:
    print("Prime Number")
else:
    print("Composite number")
print()
        
#Q11 Reverse a string without using built-in functions.

a="Pooja"
print(a[: : -1])

a=(input("Enter string:"))
rev=""
for i in range(len(a)-1,-1,-1):
    rev=rev+a[i]
print(rev)
print()

#Q12 Check if a string is a palindrome.

string=(input("Enter string:"))
rev=""
for i in range(len(string)-1,-1,-1):
    rev=rev+string[i]
if rev==string:
    print(f"Given string {string} is palindrome")
else:
    print("Not palindrome.")
print()

#Q13 Count letters, digits, and special symbols in a string.

""" 1 Using ascii (unicode) values:"""

string=input("Enter your string: ")
char=0
digit=0
spchar=0
for i in string:
    if (65<=ord(i)<=90) or (97<=ord(i)<=122):
        char=char+1
    elif (48<=ord(i)<=57):
        digit=digit+1
    else:
        spchar=spchar+1
print(f"Characters={char}, Special characters={spchar}, Digits={digit}")
print()  

"""2 Using built in functions:"""

string=input("Enter your string: ")
char=0
digit=0
spchar=0
for i in string:
    if i.isalpha():   # isalpha(): check on characters
        char=char+1
    elif i.isdigit():  # isdigit(): check on numbers
        digit=digit+1
    else:
        spchar=spchar+1
print(f"Characters={char}, Special characters={spchar}, Digits={digit}") 