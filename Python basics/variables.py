name = "John"
age = 20
print(name)
print(age)

a = 10
b = 30
print(a,b)

# Valid variable names
name = "A"
n_a_m_e = "B"
_name = "C"
name2 = "D"
print(name,n_a_m_e,_name,name2)

x = 5
x = "Hyderabad"
print(x)

# Variables are case sensitive
a = 5
A = "Java"
print(a)
print(A)

subject = "Python"
marks = 95
print("Subject:", subject)
print("Marks:", marks)

year = 2026
print("Welcome to the year",year)

oranges = 5
print("I have", oranges, "oranges.")

# Many values to multiple variables
x, y, z = "Apple", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Also use the + operator to output multiple variables
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)

# One value to multiple variables
x = y = z = "Tab"
print(x)
print(y)
print(z)

# Swap two variables
a = 5
b = 10
a, b = b, a
print(a)
print(b)

# Take an integer input from the user 
num = int(input("Enter number: "))
print(num)

# Take a string (text) input from the user
name = input("Enter name: ")
print(name)

# Local variables
def student():
    name = "Ruthvik"
    print(name)
student()  

def add():
    a = 20
    b = 30
    c = a + b
    print("The sum is:", c)
add() 

def value():
    num = 5
    print(num)
value()
num = 10
print(num)

def area_of_the_rectangle():
    length = 7
    width = 5
    print("area_of_the_rectangle:", length * width)
area_of_the_rectangle()

# Global variables
a = 10
def display():
    print("a:", a)
display()

x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

x = "awesome"
def myfunc():
    x = "fantastic"
    print(x)
myfunc()
print(x)

# Global keyword
def myfunc():
    global x
    x = "Python"
myfunc()
print(x)

country = "India"
def update():
    global country
    country = "USA"
update()
print(country)    

x = 101
def mainFunction():
    global x
    print(x)
    x = 'Welcome To Hyderabad'
    print(x)
mainFunction()
print(x)  

def mainfunction():
    global num
    num = 25
    print(num)
mainfunction()
print(num)    