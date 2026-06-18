# Sets
"""
- A set stores only unique values; duplicate elements are automatically removed.
- Sets are unordered collections, so they do not maintain insertion order.
- They are useful for membership testing and performing mathematical set operations.
"""

set1 = {1, 2, 3, 2, 2, 2, 4, 5, 5, 66, 64, 43, 244}
print(f"set1: {set1}\n")  # Duplicates are removed automatically


# Convert a list and tuple into a set using the set() constructor

l1 = [1, 2, 3, 33, 1, 2, 33, 1, 2, 4, 5, 6]
print(f"list1: {l1}")

l1 = set(l1)
print(f"list1 in set: {l1}\n")

T1 = (1, 2, 3, 4, 1, 2, 3, 3, 3)
print(f"Tuple1: {T1}")

T1 = set(T1)
print(f"Tuple1 in set: {T1}\n")


# Internal Working of Sets
"""
- Sets use a hash table internally for fast lookups.
- Elements are stored based on their hash values.
- Duplicate elements are automatically removed.
- The order of elements is not guaranteed.
- Only hashable (immutable) objects can be stored in a set.
"""


# Viewing hash values using the hash() function

set2 = {1, "hello", "coders"}
print(f"set2: {set2}")

# Note: Hash values of strings may vary between Python sessions.
print(f'hash value of "hello": {hash("hello")}')
print(f"hash value of 1: {hash(1)}")
print(f'hash value of "coders": {hash("coders")}\n')


# Only hashable objects can be stored in sets.
# Most immutable objects such as int, str, and tuple are hashable.

set3 = {1, "hello", (1, 2, 3, 3)}  # Valid: tuple is hashable
print(f"set3: {set3}\n")

"""
print(set3[0])

Raises TypeError because sets are unordered collections
and do not support indexing.
"""

# Iterating Over a Set (Running loop)
"""
- We can iterate over set elements directly using a loop.
- Since sets are unordered collections, they do not support indexing.
- The order of elements during iteration is not guaranteed.
"""

set3 = {1, "hello", (1, 2, 3, 3)}

print("Elements in set3:")
for element in set3:
    print(element)

print()

# Common Set Methods

set4 = {10, 20, 30, 40}
print(f"set4: {set4}\n")


"""
1. copy()
Returns a shallow copy of the set.
"""

copy_set = set4.copy()
print(f"copy of set4: {copy_set}\n")


"""
2. add()
Adds an element to the set.

- If the element already exists, the set remains unchanged.
- No error is raised for duplicate values.
"""

set4.add(40)  # 40 already exists
print(f"set4 after add(40): {set4}")

set4.add(50)
print(f"set4 after add(50): {set4}\n")


"""
3. discard()
Removes the specified element.

- Does NOT raise an error if the element does not exist.

4. remove()
Removes the specified element.

- Raises KeyError if the element does not exist.
"""

set4.discard(30)
print(f"set4 after discard(30): {set4}\n")

set4.remove(20)
print(f"set4 after remove(20): {set4}\n")

# set4.remove(70)  # Raises KeyError because 70 does not exist


"""
5. pop()
Removes and returns an arbitrary element from the set.

- Since sets are unordered, we cannot predict which element will be removed.
"""

set4.pop()  # Removes one arbitrary element

popped_element = set4.pop()
print(f"Popped element: {popped_element}")
print(f"set4 after pop(): {set4}\n")


"""
6. clear()
Removes all elements from the set, making it empty.
"""

set4.clear()
print(f"set4 after clear(): {set4}\n")

# Methods That Work on Multiple Sets

s1 = {10, 20, 30, 40}
print(f"set s1: {s1}")

s2 = {30, 40, 50, 60}
print(f"set s2: {s2}\n")


"""
1. difference() or -

Returns a new set containing elements that are present
in the first set but not in the other set(s).
"""

difference_set = s1.difference(s2)
print(f"s1.difference(s2): {difference_set}")

difference_set = s2.difference(s1)
print(f"s2.difference(s1): {difference_set}")

# Using the - operator
print(f"s1 - s2: {s1 - s2}")
print(f"s2 - s1: {s2 - s1}\n")


"""
2. difference_update() or -=

Removes all elements from the set that are also present
in another set.

The original set is modified in place.
"""

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

s1.difference_update(s2)  # Equivalent to: s1 -= s2
print(f"s1 after difference_update(s2): {s1}")

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

s2.difference_update(s1)  # Equivalent to: s2 -= s1
print(f"s2 after difference_update(s1): {s2}\n")


s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print(f"set s1: {s1}")
print(f"set s2: {s2}\n")


"""
3. intersection() or &

Returns a new set containing elements common to both sets.

The order of the sets does not affect the result.
"""

intersection_set = s1.intersection(s2)
print(f"s1.intersection(s2): {intersection_set}")

# Using the & operator
print(f"s1 & s2: {s1 & s2}")
print(f"s2 & s1: {s2 & s1}\n")


"""
4. intersection_update() or &=

Updates the set in place, keeping only the elements
that are common to both sets.
"""

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

s1.intersection_update(s2)  # Equivalent to: s1 &= s2
print(f"s1 after intersection_update(s2): {s1}\n")


s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}
s3 = {10, 20}

print(f"set s1: {s1}")
print(f"set s2: {s2}")
print(f"set s3: {s3}\n")


"""
5. issubset() or <= or <

Checks whether all elements of one set are contained
in another set.

<= : True if the set is a subset (equal sets allowed)
<  : True if the set is a proper subset
"""

print(f"s3.issubset(s1): {s3.issubset(s1)}")
print(f"s3 <= s1: {s3 <= s1}")
print(f"s3 < s1: {s3 < s1}\n")

print(f"s1 <= s3: {s1 <= s3}")
print(f"s1 < s3: {s1 < s3}")

print(f"s2 <= s3: {s2 <= s3}")
print(f"s2 < s3: {s2 < s3}\n")


"""
6. issuperset() or >= or >

Checks whether a set contains all elements
of another set.

>= : True if the set is a superset (equal sets allowed)
>  : True if the set is a proper superset
"""

print(f"s1.issuperset(s3): {s1.issuperset(s3)}")

print(f"s1 >= s3: {s1 >= s3}")
print(f"s1 > s3: {s1 > s3}\n")

print(f"s3 >= s1: {s3 >= s1}")
print(f"s3 > s1: {s3 > s1}\n")


"""
7. union() or |

Returns a new set containing all unique elements
from both sets.

The original sets remain unchanged.
"""

union_set = s1.union(s2)

print(f"s1.union(s2): {union_set}")
print(f"s1 | s2: {s1 | s2}\n")


"""
8. symmetric_difference() or ^

Returns a new set containing elements that exist
in either set, but not in both.
"""

symmetric_diff = s1.symmetric_difference(s2)

print(f"s1.symmetric_difference(s2): {symmetric_diff}")

# Using the ^ operator
print(f"s1 ^ s2: {s1 ^ s2}")

"""
9. symmetric_difference_update() or ^=

Updates the set in place, keeping only the elements
that are present in either set but not in both.

The original set is modified.
"""

s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

s1 ^= s2  # Equivalent to: s1.symmetric_difference_update(s2)

print(f"s1 after s1 ^= s2: {s1}")
print(f"s2 remains unchanged: {s2}\n")


s1 = {10, 20, 30, 40}
s2 = {30, 40, 50, 60}

print(f"set s1: {s1}")
print(f"set s2: {s2}\n")

"""
10. update() or |=

Updates the set in place by adding all elements
from another set.

Equivalent to a union operation, but modifies
the original set.
"""

s1 |= s2  # Equivalent to: s1.update(s2)

print(f"s1 after s1 |= s2: {s1}")
print(f"s2 remains unchanged: {s2}\n")

"""
Summary of Set Operators

|  -> Union
&  -> Intersection
-  -> Difference
^  -> Symmetric Difference
<= -> Subset
<  -> Proper Subset
>= -> Superset
>  -> Proper Superset
"""