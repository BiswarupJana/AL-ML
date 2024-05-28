## Access List
thislist = ["apple", "banana", "cherry"]
print(thislist[1]) ## Output: banana

thislist = ["apple", "banana", "cherry"]
print(thislist[-1]) ## Output: cherry

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5]) ## Output: ['cherry', 'orange', 'kiwi']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4]) ## Output: ['cherry', 'orange', 'kiwi', 'melon']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:]) ## Output: ['cherry', 'orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1]) ## Output: ['orange', 'kiwi', 'melon']

## Change List Items
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist) ## Output: ['apple', 'blackcurrant', 'cherry']

## Loop Through a List
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x) ## Output: apple banana cherry
  
## Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list") ## Output: Yes, 'apple' is in the fruits list

## List Length
thislist = ["apple", "banana", "cherry"]
print(len(thislist)) ## Output: 3

## Add Items

# To add an item to the end of the list, use the append() method:

thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist) ## Output: ['apple', 'banana', 'cherry', 'orange']

# To add an item at the specified index, use the insert() method:

thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist) ## Output: ['apple', 'orange', 'banana', 'cherry']

## Remove Item

# The remove() method removes the specified item:

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist) ## Output: ['apple', 'cherry']

# The pop() method removes the specified index, (or the last item if index is not specified):

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist) ## Output: ['apple', 'banana']

# The del keyword removes the specified index:

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist) ## Output: ['banana', 'cherry']

# The del keyword can also delete the list completely:

thislist = ["apple", "banana", "cherry"]
del thislist

# The clear() method empties the list:

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist) ## Output: []

## Copy a List
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist) ## Output: ['apple', 'banana', 'cherry']

## Join Two Lists
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2

print(list3) ## Output: ['a', 'b', 'c', 1, 2, 3]

# Another way to join two lists are by appending all the items from list2 into list1, one by one:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1) ## Output: ['a', 'b', 'c', 1, 2, 3]

# Use the extend() method to add list2 at the end of list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1) ## Output: ['a', 'b', 'c', 1, 2, 3]

## List Methods
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

## List Comprehension
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist) ## Output: ['apple', 'banana', 'mango']

# With list comprehension you can do all that with only one line of code:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist) ## Output: ['apple', 'banana', 'mango']

# The Syntax
# newlist = [expression for item in iterable if condition == True]

# The return value is a new list, leaving the old list unchanged.

# Condition
# The condition is like a filter that only accepts the items that evaluate to True.

# Example

# Only accept items that are not "apple":

newlist = [x for x in fruits if x != "apple"]

print(newlist) ## Output: ['banana', 'cherry', 'kiwi', 'mango']

# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

# The condition is optional and can be omitted:

# Example

# With no if statement:

newlist = [x for x in fruits]

print(newlist) ## Output: ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist) ## Output: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# Sort Descending
# To sort descending, use the keyword argument reverse = True:

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist) ## Output: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first):

# Example

# Sort the list based on how close the number is to 50:

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist) ## Output: [50, 65, 23, 82, 100]

# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Example

# Case sensitive sorting can give an unexpected result:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist) ## Output: ['Kiwi', 'Orange', 'banana', 'cherry']

# Luckily we can use built-in functions as key functions when sorting a list.

# So if you want a case-insensitive sort function, use str.lower as a key function:

# Example

# Perform a case-insensitive sort of the list:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist) ## Output: ['banana', 'cherry', 'Kiwi', 'Orange']

# Reverse Order

# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements.

# Example

# Reverse the order of the list items:

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist) ## Output: ['cherry', 'Kiwi', 'Orange', 'banana']

