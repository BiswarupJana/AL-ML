
## Python Data Types

In Python, variables can hold different types of data. Here are some commonly used data types:

- **String**: A sequence of characters, enclosed in single or double quotes. For example:
    ```python
    x = "Hello World"
    ```

- **Integer**: A whole number, without a fractional part. For example:
    ```python
    x = 20
    ```

- **Float**: A number with a decimal point. For example:
    ```python
    x = 20.5
    ```

- **Complex**: A number with a real and imaginary part. For example:
    ```python
    x = 1j
    ```

- **List**: An ordered collection of items, enclosed in square brackets. For example:
    ```python
    x = ["apple", "banana", "cherry"]
    ```

- **Tuple**: An ordered, immutable collection of items, enclosed in parentheses. For example:
    ```python
    x = ("apple", "banana", "cherry")
    ```

- **Range**: A sequence of numbers, commonly used in loops. For example:
    ```python
    x = range(6)
    ```

- **Dictionary**: A collection of key-value pairs, enclosed in curly braces. For example:
    ```python
    x = {"name": "John", "age": 36}
    ```

- **Set**: An unordered collection of unique items, enclosed in curly braces. For example:
    ```python
    x = {"apple", "banana", "cherry"}
    ```

- **FrozenSet**: An immutable version of a set, enclosed in curly braces. For example:
    ```python
    x = frozenset({"apple", "banana", "cherry"})
    ```

- **Boolean**: Represents either `True` or `False`. For example:
    ```python
    x = True
    ```

- **Bytes**: A sequence of bytes, prefixed with `b`. For example:
    ```python
    x = b"Hello"
    ```

- **Bytearray**: A mutable version of bytes. For example:
    ```python
    x = bytearray(5)
    ```

- **Memoryview**: A memory-efficient way to access the data of an object. For example:
    ```python
    x = memoryview(bytes(5))
    ```

- **None**: A special value representing the absence of a value. For example:
    ```python
    x = None
    ```

These are the basic data types in Python. Understanding them will help you work with different kinds of data in your programs.



## Python Number Data Types

Python supports three types of numeric data:

### int
An integer is a whole number, positive or negative, without decimals, of unlimited length. For example:
```python
x = 10
y = -5
z = 1234567890123456789
```

### float
A float is a number, positive or negative, containing one or more decimals. Float can also be scientific numbers with an "e" to indicate the power of 10. For example:

x = 20.5
y = -10.7
z = 35e3

### complex
Complex numbers are written with a "j" as the imaginary part. For example:
x = 3+5j
y = 5j
z = -5j


## Python string
### String Slicing
a = "Hello, World!"
print(a[7:12])  # Output: "World"

### String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)  # Output: "Hello World"

### String Formatting
name = "Alice"
age = 25
message = "My name is {} and I am {} years old.".format(name, age)
print(message)  # Output: "My name is Alice and I am 25 years old."

### String Methods
a = "Hello, World!"
print(a.upper())  # Output: "HELLO, WORLD!"
print(a.lower())  # Output: "hello, world!"
print(a.strip())  # Output: "Hello, World!"
print(a.replace("Hello", "Hi"))  # Output: "Hi, World!"
print(a.split(","))  # Output: ["Hello", " World!"]

### Escape String Methods

In Python, certain characters have special meanings when used in strings. These are known as escape characters and they are used to insert special characters like newline, tab, carriage returns, etc., into strings. Here are some commonly used escape characters:

- `\n`: Inserts a newline in the text at this point.
- `\t`: Inserts a tab in the text at this point.
- `\\`: Inserts a backslash character in the text at this point.
- `\"`: Inserts a double quote character in the text at this point.
- `\'`: Inserts a single quote character in the text at this point.

# Python Boolean Data Type

In Python, Boolean is a data type that can be one of two values, either True or False. These are often used in conditional statements and loops.

## Creating Booleans
You can create a Boolean by using the keywords `True` and `False` (note the capitalization). For example:
```python
x = True
y = False
```


# Perform bitwise operations on two numbers
def bitwise_operations(num1, num2):
    """
    This function performs bitwise operations on two numbers.

    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.

    Returns:
    int: The result of the bitwise operation.

    Raises:
    None

    Examples:
    >>> bitwise_operations(5, 3)
    7
    >>> bitwise_operations(10, 6)
    14

    Bitwise operations are used to manipulate individual bits of binary numbers. The common bitwise operators in Python are:

    - AND (&): Returns a number where each bit is set to 1 only if both corresponding bits of the input numbers are 1.
    - OR (|): Returns a number where each bit is set to 1 if at least one of the corresponding bits of the input numbers is 1.
    - XOR (^): Returns a number where each bit is set to 1 if only one of the corresponding bits of the input numbers is 1.
    - NOT (~): Returns the complement of the input number, flipping all the bits.

    Note that bitwise operations are performed on the binary representation of the numbers.

    """
    return num1 & num2