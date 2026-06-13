# List:

# Syntax:
"""
list_name = [v1, v2, values, v3, v4]

Here:
list_name is the name of list, it can be anything like variable names
Values (Separated by comma and can be of different data types) are written in squared brackets []

a=[1,12.4,True,"hello",print()]   # Heterogeneous in nature (can store values of different data types)

You can store anything (any datatype, data structure, function)

"""

fruits=[1,"Mango",2,"Grapes",3,"Lichi"]
print("Type of fruits is",type(fruits),"\n")
print("fruits is",fruits,"\n")

# Length of list:
""" Using len function {len()}"""
print(f"Length of fruits: {len(fruits)}\n")

# Properties of Lists:
"""
1 Ordered: 
Elements in a list maintain the order in which they are inserted.
Lists use indexing like strings, so they are ordered.
Their elements (values) can be accessed using indexes.
"""
#-ve -5      -4        -3-2-1                        
list=["Hello","Mic Testing",1,2,3]
#+ve     0         1        2 3 4
print(list)
print(list[0])    # Hello
print(list[1])    # Mic Testing
print(list[2])    # 1
print(list[3])    # 2
print(list[4],"\n")    # 3

"""
2 Mutable:
The elements of a list can be modified after creation.
This is not possible with strings because strings are immutable.
As: 
a="Hellq"
a[-1]=O   # this shows error bcoz Strings are immutable"""

age=[20,30,40,50]
print(age)
age[0]=10
print(f"after changing: {age}\n")

"""
3 Duplicacy:
Lists allow duplicate values.
"""
duplicates=[100, 200, 300, 100, 100, 200,300,300,300]
print(duplicates,"\n")

# List slicing:
""" 
# Slicing is used to access a portion of a list.
Same as in strings.
"""
days=["Monday","Tuesday","Wednesday","Thursday","Friday"]
print(days)
print(f"Slicing from 0 to 5: {days[:5]}")
print(f"Reverse of list: {days[::-1]}\n")

# Membership operators:
"""
Two membership operators:
'in' and 'not in' are used to check whether an element exists in a list.
"""
fruits = ["Mango", "Apple", "Grapes"]
print(fruits)
print(f'"Apple" in fruits: {"Apple" in fruits}')
print(f'"Banana" not in fruits: {"Banana" not in fruits}\n')

# Traversing on lists:
"""
Traversing means iterating through a list and accessing its elements one by one.
"""
# Traversing on values-
a=[20,30,40,50,60,70,80,90,100]
print(a)
for i in a:
    print("Using values",i)  # i access values

# Traversing on index:
a=[20,30,40,50,60,70,80,90,100]
for i in range(0,len(a)):
    print(f"Using index: {i}={a[i]}\n")   # i access the index

# Methods on lists:
"""
Syntax:
list_name.method(object)
# Here, object refers to the value to be added, removed, or modified.
"""
a=[20,30,40,50,60,70,80,90,100]
a.append(200)   # Adds an element at the end of the list
print("Appended 200:",a)

a.insert(0,10)   # insert(index,object) adds element at given index
print("Inserted 10 at index 0:",a,"\n")

a=[10,20,30,40,50,60,70,80,90,100,200]

a.pop()  # pop(index) removes and returns the element at the given index
# by default index is -1

b=a.pop()
print(f"Default pop: {a}, {b}")

a.pop(2)       # removes object at index 2
print(f"Pop value at index 2: {a}\n")  

a=[10,20,30,40,50,60,70,80,90,100,200]
a.remove(20)  # Removes the first occurrence of the given value and does not return it
print(a)
a.clear()    # remove all the elements make the list empty
print(a)

a=[21,23,12,9,56,101,0,45,334,56,123,56,3,1,1,22,22]
a.sort()  # Sorts the list in ascending order
print(f"Sorted in ascending order: {a}")
a.sort(reverse=True)  # in descending order
print(f"Sorted in descending order: {a}\n")

a.reverse()  # Reverses the order of elements in the list
print(f"Reverse of a: {a}\n")

# Practice questions on list:

# Q1 Print all positive and negative elements separately.
list1 = [1,-2,3,-4,5,6,-7,-7,8,-9]
positive=[]
negative=[]
for i in list1:
    if i>=0:
        positive.append(i)
    else:
        negative.append(i)
print(f"Positive: {positive}")
print(f"Negative: {negative}")

# Q2 Find the mean (average) of all list elements.

list2=[18,28,35,-45,-23,48,69,-71]

sum=0
for i in list2:
    sum=sum+i
mean=sum/len(list2)
print(f"Your average is: {mean}")

# Q3 Find the greatest element and print its index.

list3=[4, 8, 2, 9, 1]
largest=list3[0]
index=0
for i in range(0,len(list3)):
    if list3[i] > largest:
        largest=list3[i]
        index=i

print(f"Your largest value is: {largest} at index: {index}")

# Q4 Find the second greatest element.

list4=[4, 8, 2, 9, 1,10,8,11]

# Method1 using sorting:
"""
list4.sort()
print(list4[-2])
"""

# Method2:
largest=list4[0]
second_largest=list4[0]
for i in list4:
    if i>largest:
        second_largest=largest
        largest=i  
    elif i > second_largest:
        second_largest=i    
print(f"Your second_largest element is:{second_largest}")

# Q5 Check if the list is already sorted.

list5=[1, 3, 5, 7, 6, 5, 3]

for i in range(0,len(list5)-1):
    if list5[i] > list5[i+1]:
        print("Your list is not sorted")
        break
else:
    print("Your list is sorted")

   
