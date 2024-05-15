
print("Hello, World!")



# numeric datatype
print(type(1))  # <class 'int'>
print(type(1.0))  # <class 'float'>
print(type(1+2j))  # <class 'complex'>

# Sequence datatype
print(type([1, 2, 3]))  # <class 'list'>
print(type((1, 2, 3)))  # <class 'tuple'>
print(type({'a': 1, 'b': 2}))  # <class 'dict'>
print(type(range(5)))  # <class 'range'>

# Other datatype
print(type(None))  # <class 'NoneType'>
print(type('hello'))  # <class 'str'>
print(type(True))  # <class 'bool'>
print(type(b'hello'))  # <class 'bytes'>
print(type(bytearray([1, 2, 3])))  # <class 'bytearray'>
print(type(memoryview(b'hello')))  # <class 'memoryview'>

#################################################################

# List of all type of condition statements example in Python

# if statement
age = 10
if age >= 18:
    print("You are an adult")
else:
    print("You are a child")

# if ... elif ... else statement
age = 10
if age < 10:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
else:
    print("You are an adult")

# while loop
i = 0
while i < 5:
    print(i)
    i += 1

# for loop
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# break statement
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        break
    print(num)

# continue statement
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        continue
    print(num)

# pass statement
def do_nothing():
    pass

do_nothing()

# assert statement
num = 10
assert num > 0, "Number is not positive"


################################################################

# for loop examples

# range function
for i in range(5):
    print(i)

# range with step
for i in range(0, 10, 2):
    print(i)

# range with infinite loop
for i in range(10):
    if i == 5:
        break
    print(i)

# range with reverse loop
for i in range(5, -1, -1):
    print(i)

# enumerate function
fruits = ['apple', 'banana', 'cherry']
for i, fruit in enumerate(fruits):
    print(i, fruit)

# zip function
names = ['John', 'Anna', 'Peter']
ages = [28, 24, 35]
for name, age in zip(names, ages):
    print(name, age)

# while True loop
i = 0
while True:
    print(i)
    i += 1
    if i == 5:
        break

# while loop with condition
i = 0
while i < 5:
    print(i)
    i += 1


#################################################################


# Function examples
def greet(name):
    return "Hello, " + name + "!"

print(greet("Alice"))

def add(a, b):
    return a + b

print(add(1, 2))

def multiply(a, b=2):
    return a * b

print(multiply(3))
print(multiply(3, 4))

def multiply_and_add(a, b=2, c=3):
    return a * b + c

print(multiply_and_add(3))
print(multiply_and_add(3, 4))
print(multiply_and_add(3, c=5))

def return_none():
    pass

print(return_none())

def variable_length_arguments(*args):
    return sum(args)

print(variable_length_arguments(1, 2, 3))
print(variable_length_arguments(*[1, 2, 3]))

def variable_keyword_arguments(**kwargs):
    return sum(kwargs.values())

print(variable_keyword_arguments(a=1, b=2, c=3))
print(variable_keyword_arguments(**{'a': 1, 'b': 2, 'c': 3}))

def function_with_default_argument(a=1, b=2):
    return a + b

print(function_with_default_argument())
print(function_with_default_argument(1))
print(function_with_default_argument(1, 2))

def function_with_default_argument_and_variable_length_arguments(a=1, *args):
    return a + sum(args)

print(function_with_default_argument_and_variable_length_arguments())
print(function_with_default_argument_and_variable_length_arguments(1))
print(function_with_default_argument_and_variable_length_arguments(1, 2, 3))
print(function_with_default_argument_and_variable_length_arguments(1, *[2, 3]))

