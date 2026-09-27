a = 10
b = a
print(a is b)

a = 30
b = 30
print(a is not b)

a = [10, 20, 30] 
b = [10, 20, 30]
print(a == b)
print(a is b)
print(a is not b)
print(a != b)

x = None
print(x is None)
print(x is not None)

x = ["apple", "banana"]
y = x
print(x == y)
print(x is y)
print(x is not y)
print(x)
print(y)

a = int(input("Enter a value "))
b = int(input("Enter b value "))
c = a
print(c is a)
print(a is not b)