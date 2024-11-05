# Exercise 1: Calculate Area of a Triangle
#
def calculate_area_triangle(base, height):
  return(base * height) / 2

print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: Calculate Simple Interest
#
def simple_interest(principal, rate, time):
  return(principal * rate * time) / 100

print('Exercise 2:', simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount
#
def apply_discount(price, discount):
  return price - (price * discount / 100)

print('Exercise 3:', apply_discount(100, 25))


# Exercise 4: Convert Temperature
#
def convert_temperature(temp, unit):
  if unit == "C":
    return(temp * 9/5) + 32
  elif unit == "F":
    return(temp - 32) * 5/9
  else:
    return("Invalid unit")

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N
#
def sum_to(n):
  total = 0
  i = 1
  while i <= n:
    total += i
    i += 1
  return(total)

print('Exercise 5:', sum_to(6))


# Exercise 6: Find the Largest Number
#
def largest(a, b, c):
  return max(a, b, c)

print('Exercise 6:', largest(1, 2, 3))


# Exercise 7: Calculate a Tip
#
def calculate_tip(bill, percentage):
  return(bill * percentage) / 100

print('Exercise 7:', calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers
#
def product(*arg):
  result = 1
  for number in arg:
    result *= number
  return result

print('Exercise 8:', product(2, 5, 5))


# Exercise 9: Basic Calculator
#
# Create a function named `basicCalculator` that takes three arguments: 
# two numbers and a string representing an operation ('add', 'subtract', 'multiply', 'divide'). 
# Perform the provided operation on the two numbers. In operations where the order of numbers is important, 
# treat the first parameter as the first operand and the second parameter as the second operand.
#
# Examples:
# basicCalculator(10, 5, 'subtract') should return 5.
# basicCalculator(10, 5, 'add') should return 15.
# basicCalculator(10, 5, 'multiply') should return 50.
# basicCalculator(10, 5, 'divide') should return 2.
#
# Define the function and then call it below.
def basicCalculator(num1, num2, operation):
  if operation == 'add':
    return num1 + num2
  elif operation == 'subtract':
    return num1 - num2
  elif operation == 'multiply':
    return num1 * num2
  elif operation == 'divide':
    return num1 / num2 if num2 != 0 else "can't divide by 0" 
  else:
    return("Invalid operation")


print('Exercise 9 Result:', basicCalculator(10, 0, "divide"))
