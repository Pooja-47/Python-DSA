# Dictionary:-
"""
-A dictionary stores data as key: value pairs — like a real dictionary,
where you look up a word (key) to find its meaning (value).

- Keys in a dictionary must be unique.
  If the same key is used multiple times, the last assigned value overwrites the previous one.

- Different keys can have the same value.

- Dictionaries do not use numerical indexing like lists.
  Instead, values are accessed using their keys.

- Keys play a role similar to indexes, but they can be of different data types
  such as strings, integers, tuples, etc.

- Dictionaries are mutable, meaning their elements can be added,
  modified, or removed after creation.

# Syntax:

dictionary_name = {key : value}

"""
d = {}    # This is a dictionary, not a set. An empty set cannot be created using {}.
print(f"d: {d}")
print(f"Type of d: {type(d)}\n")

# Example:
student = {
    "name": "Pookie",
    "age": 16,
    "city": "myworld"
}

print(f"student: {student}")
print(f"Value of key 'name' in student dictionary: {student['name']}\n")

numbers = {10:100, 20:200, 30:300, 40:400, 50:500}

print(
    f"numbers: {numbers}\n"
    f"with keys: 10, 20, 30, 40, 50\n"
    f"and respective values: 100, 200, 300, 400, 500\n"
)

# We can access dictionary values using their keys:
print(f"numbers: {numbers}")
print(f"Value of key 20: {numbers[20]}\n")

# CRUD Operations

# Vanilla Python: Performing CRUD operations directly using keys.

"""
- Create (C):
    To create a dictionary or add a new key-value pair.

    If the key does not exist, it will be added to the dictionary.
"""
my_dict = {1:10, 2:20, 3:30, 4:40}
print(f"Dictionary created: {my_dict}")

my_dict[5] = 50
print(f"Created new key-value pair my_dict[5] = 50: {my_dict}\n")

"""
- Read (R):
    To access the value associated with a key.
"""
print(f"Value of key 3: {my_dict[3]}\n")

"""
- Update (U):
    To modify the value of an existing key.
"""
my_dict[4] = 400
print(f"Updated value of key 4: {my_dict[4]}\n")

"""
- Delete (D):
    To remove key-value pairs from a dictionary.

    Methods:
    - del
    - pop()
    - popitem()
    - clear()
"""
"""
Delete using del:
The del keyword removes the specified key-value pair from the dictionary.
It does not return the value deleted.
"""

dict2 = {1:10, 2:20, 3:30, 4:40}
print(f"dict2 before del: {dict2}")

del dict2[2]
print(f"dict2 after del dict2[2]: {dict2}\n")

# Methods on Dictionary:

dict1 = {10:100, 20:400, 30:900, 40:1600, 50:2500}
print(f"dict1: {dict1}\n")


"""
1. copy(): Returns a shallow copy of the dictionary.
"""
dict_copy = dict1.copy()
print(f"Copy of dict1: {dict_copy}")
print(f"dict1 is dict_copy: {dict1 is dict_copy}\n")


"""
2. get(): Returns the value of the specified key.
If the key does not exist, it returns None by default.
"""
print(f"Value of key(30): {dict1.get(30)}\n")


"""
3. items(): Returns a view object containing all key-value pairs as tuples.
"""
print(f"Key-value pairs [dict1.items()]: {dict1.items()}\n")


"""
4. keys(): Returns a view object containing all keys of the dictionary.
"""
print(f"Keys in dict1 [dict1.keys()]: {dict1.keys()}\n")


"""
5. values(): Returns a view object containing all values of the dictionary.
"""
print(f"Values in dict1 [dict1.values()]: {dict1.values()}\n")


"""
6. pop(): Removes and returns the value associated with the specified key.
"""
p = dict1.pop(50)
print(f"Popped value of key(50): {p}")
print(f"dict1 after dict1.pop(50): {dict1}\n")


"""
7. popitem(): Removes and returns the last inserted key-value pair.
"""
last_item = dict1.popitem()
print(f"Popped last inserted item: {last_item}")
print(f"dict1 after dict1.popitem(): {dict1}\n")


"""
8. clear(): Removes all elements from the dictionary.
"""
dict1.clear()
print(f"dict1 after dict1.clear(): {dict1}\n")


dict2 = {1:10, 2:20, 3:30, 4:40}
print(f"dict2: {dict2}\n")


"""
9. setdefault(): Returns the value of the specified key.

If the key exists:
    Returns its value without making any changes.

If the key does not exist:
    Inserts the key with the specified value and returns that value.
"""
dict2.setdefault(3, 300)  # Key 3 already exists.
print(f"dict2 after dict2.setdefault(3, 300): {dict2}")

dict2.setdefault(5, 50)   # Key 5 does not exist.
print(f"dict2 after dict2.setdefault(5, 50): {dict2}\n")


"""
10. update(): Updates existing key-value pairs and/or adds new key-value pairs.
"""
dict2.update({4:400, 7:700})
print(f"dict2 after dict2.update({{4:400, 7:700}}): {dict2}\n")


"""
11. fromkeys(): Creates a new dictionary using the given keys and a common value.
"""
dict3 = dict.fromkeys([1, 2, 3, 4], 0)
print(f"dict3 created using dict.fromkeys([1, 2, 3, 4], 0): {dict3}")

"""
Note:
Dictionary keys must be immutable data types such as:
- int
- float
- str
- tuple

Mutable types like list, set, and dictionary cannot be used as keys.
"""