## Tuples 
# - A tuple is a sequence of immutable Python objects.  
# - Tuples are sequences, just like lists.
mytuple = ("apple", "banana", "cherry")
print(mytuple) ## Output: ('apple', 'banana', 'cherry')

# Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple) ## Output: ('apple', 'banana', 'cherry', 'apple', 'cherry')

# Tuple Length
thistuple = ("apple", "banana", "cherry")
print(len(thistuple)) ## Output: 3

# Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple)) ## Output: <class 'tuple'>
#NOT a tuple
thistuple = ("apple")
print(type(thistuple)) ## Output: <class 'str'>

# Tuple Items - Data Types
# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry") ## string
tuple2 = (1, 5, 7, 9, 3) ## int
tuple3 = (True, False, False) ## bool

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) ## note the double round-brackets
print(thistuple) ## Output: ('apple', 'banana', 'cherry')



# -----------------------------------------------------------------


# Access Tuples
thistuple = ("apple", "banana", "cherry")
print(thistuple[1]) ## Output: banana

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1]) ## Output: cherry

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5]) ## Output: ('cherry', 'orange', 'kiwi')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4]) ## Output: ('apple', 'banana', 'cherry', 'orange')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:]) ## Output: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1]) ## Output: ('orange', 'kiwi', 'melon')

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# Update Tuple
# You are allowed to take portions of existing tuples to create new tuples as the following example demonstrates:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)
# Add Items
# 1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)

print(thistuple) ## Output: ('apple', 'banana', 'cherry', 'orange')

# 2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple:

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y ## Output: ('apple', 'banana', 'cherry', 'orange')

# Remove Items
# Tuples are unchangeable, so you cannot remove items from it, but you can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
# print(thistuple) ## Output: NameError: name 'thistuple' is not defined


