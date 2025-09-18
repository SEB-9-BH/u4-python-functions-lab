# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):
    return 0.5 * base * height

print("Exercise 1: ", calculate_area_triangle(5, 10))

# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("Exercise 2: ", simple_interest(1000, 5, 2))

# Exercise 3: Apply a Discount
def apply_discount(price, discount):
    return price - (price * discount / 100)

print('Exercise 3:', apply_discount(100, 25))

# Exercise 4: Convert Temperature
def convert_temperature(temperature, unit):
    if unit == 'C':
        return (temperature * 9/5) + 32
    elif unit == 'F':
        return (temperature - 32) * 5/9
    
print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))

# Exercise 5: Sum to N
def sum_to(n):
    return sum(range(1, n + 1))

print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number
def largest (num1 , num2, num3):
    return max(num1, num2, num3)

print('Exercise 6:', largest(1, 2, 3))

# Exercise 7: Calculate a Tip
def calculate_tip(bill_amount, tip_percentage):
    return bill_amount * (tip_percentage / 100)

print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8: Calculate Product of Numbers
def product(*num):
    nums = 1
    for i in num:
        nums *= i
    return nums

print('Exercise 8:', product(2, 5, 5))

# Exercise 9: Basic Calculator
def basic_calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        return num1 / num2

print('Exercise 9 Result:', basic_calculator(10, 5, "subtract")) 