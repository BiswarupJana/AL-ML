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
