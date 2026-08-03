# Getting the data type
a = 10
print(a)
print(type(a))
b = "Welcome"
print(b)
print(type(b))
c = 10.5
print(c)
print(type(c))
d = 1j
print(d)
print(type(d))
x = ["apple", "banana", "cherry"]
print(x)
print(type(x))
x = ("cat", "dog", "rat")
print(x)
print(type(x))
x = range(10)
print(x)
print(type(x))
x = {"name" : "Ravi", "age" : 30}
print(x)
print(type(x))
x = {"book", "pencil", "pen"}
print(x)
print(type(x))
x = frozenset({"bat", "ball", "big"})
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = b"World"
print(x)
print(type(x))
x = bytearray(5)
print(x)
print(type(x))
x = memoryview(bytes(5))
print(x)
print(type(x))
x = None
print(x)
print(type(x))

# Setting the specific data type
x = int(10)
print(x, type(x))
x = str("Welcome")
print(x, type(x))
x = float(10.5)
print(x, type(x))
x = complex(1j)
print(x, type(x))
x = list(("apple", "banana", "cherry"))
print(x, type(x))
x = tuple(("cat", "dog", "rat"))
print(x, type(x))
x = range(10)
print(x, type(x))
x = dict(name = "Ravi", age = 30)
print(x, type(x))
x = set(("book", "pencil", "pen"))
print(x, type(x))
x = frozenset(("bat", "ball", "big"))
print(x, type(x))
x = bool(5)
print(x, type(x))
x = bytes(5)
print(x, type(x))
x = bytearray(5)
print(x, type(x))
x = memoryview(bytes(5))
print(x, type(x))

# Python  Numbers
# Integers
x = 5
y = 11778845522265653
z = -2322555
print(type(x))
print(type(y))
print(type(z))

# Float 
x = 2.10
y = 3.0
z = -55.69
a = 12E4
b = -78.6e200
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))

# Complex Numbers
x = 5+6j
y = 7j
z = -8j
print(type(x))
print(type(y))
print(type(z))

x = 5
y = 3.7
z = 5j
print(type(x))
print(type(y))
print(type(z))

a = 1
print("The type of a", type(a))
b = 20.8
print("The type of b", type(b))
c = 2+7j
print("The type of c", type(c))
print("c is a complex number", isinstance(2+7j, complex))
d = 3.0+3.2j
print(d, "The type of d", type(d))