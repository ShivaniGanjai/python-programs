# Getting the data type
a = 10
b = "Welcome"
c = 10.5
d = 1j
print(type(a))
print(type(b))
print(type(c))
print(type(d))
x = ["apple", "banana", "cherry"]
print(type(x))
x = ("cat", "dog", "rat")
print(type(x))
x = range(10)
print(type(x))
x = {"name" : "Ravi", "age" : 30}
print(type(x))
x = {"book", "pencil", "pen"}
print(type(x))
x = frozenset({"bat", "ball", "big"})
print(type(x))
x = True
print(type(x))
x = b"World"
print(type(x))
x = bytearray(5)
print(type(x))
x = memoryview(bytes(5))
print(type(x))
x = None
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