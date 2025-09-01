# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):
    area= (base * height) / 2
    return area

print('Exercise 1:', calculate_area_triangle(10, 5))
# Exercise 2
def simple_interest(principal, rate, time):
    interest= (principal * rate * time) / 100
    return interest

print('Exercise 2:', simple_interest(1000, 5, 2))
print(simple_interest(1500, 3.5, 5))
# Exercise 3
def apply_discount(price , discount):
    if (discount>100 or discount<0):
        print('discount percentage should be in the range 0-100')
        return
    else:
        updated_price= price - ((discount/100)*price)
        return updated_price
print('Exercise 3:', apply_discount(80, 10))
# Exercise 4
def convert_temperature(temp, unit):
    if unit == 'C':  # Celsius → Fahrenheit
        return (temp * 9/5) + 32
    elif unit == 'F':  # Fahrenheit → Celsius
        return (temp - 32) * 5/9
    else:
        print('Invalid input')
        return
print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))
# Exercise 5
def sum_to(n):
    return n * (n + 1) // 2
print('Exercise 5:', sum_to(6))
# Exercise 6
def largest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c
print('Exercise 6:', largest(1, 2, 3))      # → 3
print('Exercise 6:', largest(10, 4, 2))     # → 10
print('Exercise 6:', largest(-5, -2, -9))   # → -2
print('Exercise 6:', largest(1, 0, 3))      # → 3
# Exercise 7
def calculate_tip(bill , tip_percentage):
    tip= (tip_percentage/100) * bill
    return tip
print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result
print('Exercise 8:', product(2, 5, 5))    # → 50
print('Exercise 8:', product(-1, 4))      # → -4
print('Exercise 8:', product(1, 2, 3, 4)) # → 24
print('Exercise 8:', product())           # → 1
# Exercise 9
def basic_calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:  
            return a / b
        else:
            return "Error: Division by zero"
    else:
        return "Error: Invalid operation"
print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))   # → 5
print('Exercise 9 Result:', basic_calculator(10, 5, "add"))        # → 15
print('Exercise 9 Result:', basic_calculator(10, 5, "multiply"))   # → 50
print('Exercise 9 Result:', basic_calculator(10, 5, "divide"))     # → 2.0
print('Exercise 9 Result:', basic_calculator(10, 0, "divide"))     # → Error: Division by zero
print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))