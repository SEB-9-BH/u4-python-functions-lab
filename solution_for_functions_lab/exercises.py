# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):
    area = base*height/2

    return area
print('Exercise 1:', calculate_area_triangle(10, 5))

# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    formula = principal*rate*time/100
    return formula

print('Exercise 2:', simple_interest(1500,3.5, 5))

# Exercise 3: Apply a Discount
def apply_discount(price, discount):
    discount_amount = price*discount/100
    new_price = price - discount_amount
    return new_price
print('Exercise 3:', apply_discount(100, 25))

# Exercise 4: Convert Temperature
def convert_temperature(temp, unit):
    #convert to Fahrenheit
    if unit == "C":
        return (temp * 9/5) + 32
    #convert to Celsius
    elif unit == "F":
        return (temp - 32) * 5/9
    else:
        print(f"{unit} is invalid")

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N
def sum_to(n):
    sum = 0
    for i in range(n):
        sum += i
    return sum

print('Exercise 5:', sum_to(6))

# Exercise 6: Find the Largest Number
def largest(a,b,c):
    if b>a and b>c:
        return b
    elif c>a and c>b:
        return c
    else:
        return a
print('Exercise 6:', largest(1, 2, 3))

# Exercise 7: Calculate a Tip
def calculate_tip(bill,tip):
    tip_percent = (bill/100) * tip
    return tip_percent

print('Exercise 7:', calculate_tip(50, 20))

# Exercise 8: Calculate Product of Numbers
def product(*args):
    p=1
    for arg in args:
        p *= arg
    return p
print('Exercise 8:', product(2, 5, 5))

# Exercise 9: Basic Calculator
def basic_calculator(num1,num2,operator):
    if operator == 'add':
        return num1+num2
    elif operator == 'subtract':
        return num1-num2
    elif operator == 'multiply':
        return num1*num2
    elif operator == 'divide':
        return num1/num2
    else:
        return "Invalid"

print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))