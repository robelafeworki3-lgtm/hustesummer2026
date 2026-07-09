#Snippet 1
x = 10
y = 0

if y != 0:
    result = x / y
    print("Result:", result)
else:
    print("Cannot divide by zero")
#zero division error

#Snippet2
numbers = [1, 2, 3, 4, 5]

for i in range(len(numbers)):
    print(numbers[i])
#index error

#snippet3
def calculate_area(radius):
    area = 3.14 * radius ** 2
    return area

radius = 5
print(calculate_area(radius))
#syntax error

#snippet4
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))
print(is_even(7))
#syntax error

#snippet5
for i in range(5):
    print(i)
#syntax error

#snippet6
def greet(name):
    return "Hello, " + name

print(greet("Alice"))
#syntax error

#snippet7
numbers = [1, 2, 3, 4, 5]
total = 0

for number in numbers:
    total += number

print("Sum of numbers:", total)
#indentation error

#snippet8
def factorial(n):

    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
#recursion error

#snippet9
name = input("Enter your name: ")

if name == "Alice" or name == "Bob":
    print("Hello, " + name)
else:
    print("Hello, stranger!")
    
#Snippet10
def divide_numbers(x, y):
    if y == 0:
        return "Cannot divide by zero"
    
    result = x / y
    return result

num1 = 10
num2 = 0

print(divide_numbers(num1, num2))
#zero division error

