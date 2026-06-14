# Sets:
"""
Unique values only, that is no duplicacy is allowed.
A set automatically removes duplicates and has no guaranteed order. 
Great for checking membership and performing math-style set operations.
"""
set1={1,2,3,2,2,2,4,5,5,66,64,43,244}
print(f"set1: {set1}\n") # removes duplicates automatically

# Convert list and tuple into  set using set function{set()}

l1=[1,2,3,33,1,2,33,1,2,4,5,6]
print(f"list1:{l1}")

l1=set(l1)
print(f"list1 in set: {l1}\n")

T1=(1,2,3,4,1,2,3,3,3)
print(f"Tuple1:{T1}")

T1=set(T1)
print(f"Tuple1 in set: {T1}\n")

# Internal working of sets:
"""
Sets use a hash table internally for fast lookup.
Elements are stored using their hash values.
Since sets store only unique elements, duplicates are automatically removed.
Because of hashing, the order of elements is not guaranteed.
Only hashable (immutable) objects can be stored in a set.
"""
# Seeing hash value of set elements using hash function{hash()}:

set2={1,"hello","coders"}
print(f"set2: {set2}")
print(f'hash value of hello: {hash("hello")}')
print(f"hash value of 1: {hash(1)}")
print(f'hash value of coders:{hash("coders")}\n')

# Only hashable objects can be stored in sets.
# Most immutable objects (int, str, tuple, etc.) are hashable.
set3={1,"hello",(1,2,3,3)}  # this is allowed
print(f"set3: {set3}")
"""
print(set3[0])   This gives error because sets are not ordered elements cannot be accessed using index.
"""

# Loop on sets:
"""
We can iterate over set elements directly.
Since sets are unordered, they do not support indexing.
"""

set3={1,"hello",(1,2,3,3)}
print("Elements in set3:")
for i in set3:
    print(f"{i}")
print()

# Methods on set:

set4={10,20,30,40}
print(f"set4: {set4}\n")
"""
1. add():
We can add the elements which do not exist in the set.
If we try to add already existing element then the set remains unchanged.
"""
set4.add(40)  # No error. Since 40 already exists, the set remains unchanged.
print(f"set4 after add(40): {set4}")
set4.add(50)
print(f"Set4 after add(50): {set4}\n")

"""
2. discard():
Removes the specified item.
Does NOT raise an error if the item does not exist.

3. remove():
Removes the specified item.
Raises KeyError if the item does not exist.
"""
set4.discard(30)
print(f"set4 after discard(30): {set4}\n")

set4.remove(20)
print(f"set4 after remove(20): {set4}\n")
# set4.remove(70)  # Raises KeyError because 70 does not exist

"""
4. pop():
Removes and returns an arbitrary element from the set.
Since sets are unordered, we cannot predict which element will be removed.
"""
set4.pop()
a=set4.pop()   # the element popped is returned here and stored in variable a
print(f"Popped element a: {a}")
print(f"set4 after pop(): {set4}\n")

"""
5. clear():
Removes all the elements of the set and makes it empty.
"""
set4.clear()
print(f"set4 after clear(): {set4}")



