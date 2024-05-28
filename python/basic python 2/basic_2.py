## Python Data Type

x = "Hello World"
x = 20
x = 20.5
x = 1j
x = ["apple", "banana", "cherry"]
x = ("apple", "banana", "cherry")
x = range(6)
x = {"name": "John", "age": 36}
x = {"apple", "banana", "cherry"}
x = frozenset({"apple", "banana", "cherry"})
x = True
x = b"Hello"
x = bytearray(5)
x = memoryview(bytes(5))
x = None

## Python Numbers

x = 1

x = 1.10

x = 3j


## Python Casting
# example
x = int(1)  # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3

x = float(1)  # x will be 1.0
y = float(2.8)  # y will be 2.8
z = float("3")  # z will be 3.0

x = str("s1")  # x will be 's1'
y = str(2)  # y will be '2'
z = str(3.0)  # z will be '3.0'


## Python Strings

# string are array
a = "Hello, World!"
print(a[1])

# Looping Through a String
for x in "banana":
    print(x)

# String Length
a = "Hello, World!"
print(len(a))

# Check String
txt = "The best things in life are free!"
print("free" in txt)

txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# Check if NOT
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("No, 'expensive' is NOT present.")

# Method
a = "Hello, World!"
print(a.upper())  # Output: "HELLO, WORLD!"
print(a.lower())  # Output: "hello, world!"
print(a.strip())  # Output: "Hello, World!"
print(a.replace("Hello", "Hi"))  # Output: "Hi, World!"
print(a.split(","))  # Output: ["Hello", " World!"]

# String Concatenation
a = "Hello"
b = "World"
c = a + b
print(c)

# String Format
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# Escape Character
txt = 'We are the so-called "Vikings" from the north.'
print(txt)

txt = "It's alright."
print(txt)

txt = "This will insert one \\ (backslash)."
print(txt)

txt = "Hello\nWorld!"
print(txt)

txt = "Hello\rWorld!"
print(txt)


## Python Booleans

print(10 > 9)
print(10 == 9)
print(10 < 9)

a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")


## Python Operators
### Python Arithmetic Operators
x = 5
y = 10
print(x + y)  # Output: 15
print(x - y)  # Output: -5
print(x * y)  # Output: 50
print(x / y)  # Output: 0.5
print(x % y)  # Output: 5
print(x**y)  # Output: 9765625
print(x // y)  # Output: 0


### Python Assignment Operators
x = 5
x += 3  # Output: 8
x -= 3  # Output: 2
x *= 3  # Output: 15
x /= 3  # Output: 1.6666666666666667
x %= 3  # Output: 2
x //= 3  # Output: 0
x **= 3  # Output: 125
x &= 3  # Output: 1
x |= 3  # Output: 3
x ^= 3  # Output: 2
x >>= 3  # Output: 0
x <<= 3  # Output: 24
print(x := 3)  # Output: 3

### Python Comparison Operators
x = 5
y = 3
print(x == y)  # Output: False
print(x != y)  # Output: True
print(x > y)  # Output: True
print(x < y)  # Output: False
print(x >= y)  # Output: True
print(x <= y)  # Output: False

### Python Logical Operators
x = 5
print(x > 3 and x < 10)  # Output: True
print(x > 3 or x < 4)  # Output: True
print(not (x > 3 and x < 10))  # Output: False

### Python Identity Operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)  # Output: True
print(x is y)  # Output: False
print(x == y)  # Output: True

print(x is not z)  # Output: False
print(x is not y)  # Output: True
print(x != y)  # Output: False

### Python Membership Operators
x = ["apple", "banana"]
print("banana" in x)  # Output: True
print("pineapple" not in x)  # Output: True

### Python Bitwise Operators
x = 5
y = 3
print(x & y)  # Output: 1
print(x | y)  # Output: 7
print(x ^ y)  # Output: 6
print(~x)  # Output: -6
print(x << 2)  # Output: 20
print(x >> 2)  # Output: 1
