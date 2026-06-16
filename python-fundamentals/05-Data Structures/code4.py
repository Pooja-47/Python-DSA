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
1. copy():
Returns the copy of the set.
"""

set4.copy()  # returns copy
copy=set4.copy()  # stored copy of set
print(f"set4.copy: {copy}\n")

"""
2. add():
We can add the elements which do not exist in the set.
If we try to add already existing element then the set remains unchanged.
"""
set4.add(40)  # No error. Since 40 already exists, the set remains unchanged.
print(f"set4 after add(40): {set4}")
set4.add(50)
print(f"Set4 after add(50): {set4}\n")

"""
3. discard():
Removes the specified item.
Does NOT raise an error if the item does not exist.

4. remove():
Removes the specified item.
Raises KeyError if the item does not exist.
"""
set4.discard(30)
print(f"set4 after discard(30): {set4}\n")

set4.remove(20)
print(f"set4 after remove(20): {set4}\n")
# set4.remove(70)  # Raises KeyError because 70 does not exist

"""
5. pop():
Removes and returns an arbitrary element from the set.
Since sets are unordered, we cannot predict which element will be removed.
"""
set4.pop()
a=set4.pop()   # the element popped is returned here and stored in variable a
print(f"Popped element a: {a}")
print(f"set4 after pop(): {set4}\n")

"""
6. clear():
Removes all the elements of the set and makes it empty.
"""
set4.clear()
print(f"set4 after clear(): {set4}\n")

# Now movig to the methods that work on two sets:
s1={10,20,30,40}
print(f"set s1: {s1}")
s2={30,40,50,60}
print(f"set s2: {s2}\n")

"""
1. difference() or - :
Returns a new set containing elements that are present in the first set
but not in the other set(s).
"""
s1.difference(s2)   # Returns elements that are present in s1 but not in s2
diff=s1.difference(s2)
print(f"difference between s1 and s2(s1 - s2): {diff}\n")

s2.difference(s1)   # Returns elements that are present in s2 but not in s1
diff=s2.difference(s1)
print(f"difference between s2 and s1(s2 - s1): {diff}\n")
# Another way:
print(f"s1-s2 is {s1-s2}") 
print(f"s2-s1 is {s2-s1}\n")

"""
2. difference_update() or -= :
Removes all elements from this set that are also present in another set.
The original set is modified in place.
"""

s1.difference_update(s2)    # Equivalent to: s1 -= s2
print(f"s1 is updated after s1.difference_update(s2): {s1}")
print(f"s2 is unchanged after s1.difference_update(s2): {s2}")

s2.difference_update(s1)   # Equivalent to: s2 -= s1
print(f"s2 is updated after s2.difference_update(s1): {s2}")
print(f"s1 is unchanged after s2.difference_update(s1): {s1}\n")


s1={10,20,30,40}
print(f"set s1: {s1}")
s2={30,40,50,60}
print(f"set s2: {s2}\n")

"""
3. intersection() or & :
Returns a new set containing elements common to both sets.
The order of the sets does not affect the result.
"""

s1.intersection(s2) 
intersect=s1.intersection(s2)
print(f"intersection after s1.intersection(s2): {intersect}")

print(f"intersection of s2 & s1: {s2 & s1}\n")

"""
4. intersection_update() or &= :
Updates the set in place, keeping only the elements
that are common to both sets.
"""

s1 &= s2
print(f"s1 after s1 &= s2: {s1}")
s2 &= s1
print(f"s2 after s2 &= s1: {s2}\n")

s1={10,20,30,40}
print(f"set s1: {s1}")
s2={30,40,50,60}
print(f"set s2: {s2}")
s3={10,20}
print(f"set s3: {s3}\n")

"""
5. issubset() or <= or < :
Checks whether all elements of one set are contained in another set.

<= : True if this set is a subset of the other set (equal sets allowed).
<  : True only if this set is a proper subset of the other set.
"""
print(f"is s3.issubset(s1): {s3.issubset(s1)}") # True because every element of s3 exists in s1
print(f"is s3 <= s1: {s3 <= s1}")
print(f"is s3 < s1: {s3 < s1}\n")
print(f"is s1 <= s3: {s1 <= s3}")
print(f"is s1 < s3: {s1 < s3}")
print(f"is s2 <= s3: {s2 <= s3}")
print(f"is s2 < s3: {s2 < s3}\n")

"""
6. issuperset() or >= or > :
Checks whether this set contains all elements of another set.

>= : True if this set is a superset of the other set (equal sets allowed).
>  : True only if this set is a proper superset of the other set.
"""
print(f"s1.issuperset(s3): {s1.issuperset(s3)}") # True as all items of s3 are in s1 with more items
print(f"is s3 >= s1: {s3 >= s1}")
print(f"s1 >= s3: {s1 >= s3}\n")

"""
7. symmetric_difference() or ^ :
Returns a new set containing elements that exist in either set,
but not in both.
"""
s1.symmetric_difference(s2)  
print(f"Symmetric difference of s1 and s2: {s1.symmetric_difference(s2)}")

"""
8. symmetric_difference_update() or ^= :
Updates the set in place, keeping only elements that are present
in either set but not in both.
"""
# Updates s1 with the symmetric difference; s2 remains unchanged
print(f"s1 after s1 ^= s2: {s1}")


s1 = {10,20,30,40}
s2 = {30,40,50,60}

print(f"set s1: {s1}")
print(f"set s2: {s2}\n")

"""
9. union() or | :
Returns a new set containing all unique elements
from both sets.
"""
print(f"Union of s1 and s2: {s1.union(s2)}\n")

"""
10. update() or |= :
Updates the set in place by adding all elements
from another set (union operation).
"""
s1 |= s2
print(f"s1 after update(s1 |= s2): {s1}\n")