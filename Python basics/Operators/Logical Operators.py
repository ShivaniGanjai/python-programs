x = 5                          # Returns true if both statements are true.
print(x > 3 and x < 10)

x = 5                          # Returns true if one of the statements is true.
print(x > 3 or x < 4)

x = 5                          # Reverse the result, returns false if the result is true.
print(not(x > 3 and x < 10))

# Examples
a = int(input("Enter num1: "))
b = int (input("Enter num2: "))
print(a > 5 and b > 30)

a = int(input("Enter a value: "))
b = int(input("Enter b value: "))
print(a > 15 or b > 30)

num = int(input("Enter num: "))
print(not(num < 10))

age = int(input("Enter age: "))
print(age >= 18 and age <= 60)

username = "Adhi"
password = "1234"
print(username == "Adhi" and password == "1234")

num = int(input("Enter a num: "))
print(num > 0 and num % 2 == 0)
print(num % 5 == 0 or num % 10 == 0)

a = 20
print(a >= 1 and a <= 100 and not a == 50)