# Exercise 1: 
def calculate_area_triangle(base, height):
    return (base * height) / 2

print('Exercise 1:', calculate_area_triangle(10, 5))


# Exercise 2: 
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print('Exercise 2:', simple_interest(1000, 5, 2))


# Exercise 3: 
def apply_discount(price, discount_percentage):
    return price - (price * discount_percentage / 100)

print('Exercise 3:', apply_discount(100, 25))


# Exercise 4: 
def convert_temperature(temp, unit):
    if unit == 'C':  # Celsius to Fahrenheit
        return (temp * 9 / 5) + 32
    elif unit == 'F':  # Fahrenheit to Celsius
        return (temp - 32) * 5 / 9
    else:
        return "Invalid unit"

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: 
def sum_to(n):
    return sum(range(1, n + 1))

print('Exercise 5:', sum_to(6))


# Exercise 6: 
def largest(a, b, c):
    return max(a, b, c)

print('Exercise 6:', largest(1, 2, 3))


# Exercise 7:
def calculate_tip(bill, tip_percentage):
    return bill * (tip_percentage / 100)

print('Exercise 7:', calculate_tip(50, 20))


# Exercise 8: 
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

print('Exercise 8:', product(2, 5, 5))


# Exercise 9: 
def basic_calculator(a, b, operation):
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid operation"

print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
