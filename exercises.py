# Exercise 1: Calculate Area of a Triangle

from dis import disco


def calculate_area_triangle(base, height):
    #Calculating the area of a triangle
    area = base * height
    return area

print('Exercise 1:', calculate_area_triangle(10, 5))

# Exercise 2: Calculate Simple Interest

def simple_interest (principle, rate_of_interest, time):
    #Calculating the simple interest formula
    interest = (principle * rate_of_interest * time)/100
    return interest

print('Exercise 2:', simple_interest(1000, 5, 2))


# Exercise 3: Apply a Discount

def apply_discount(price, discount_rate):
    discount = (price) - (price * discount_rate/100)
# Define your function and call it to display the discounted price.
    return discount


print('Exercise 3:', apply_discount(100, 25))


# Exercise 4: Convert Temperature

def convert_temperature(temperature, unit):
    if unit=='F':
        convert_temperature = (temperature - 32) * 5/9
        return convert_temperature
    elif unit=='C':
        convert_temperature = (temperature * 9/5) + 32
        return convert_temperature
    else:
        return 'Please enter a valid temperature'

# Define the function and then call it below.

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))


# Exercise 5: Sum to N

def sum_to(n):
    sum = 0
    for i in range(1,n+1):
        sum += i
    return sum

print('Exercise 5:', sum_to(6))



# Define the function and then call it below.

# Exercise 6: Find the Largest Number

def largest(x,y,z):
    largest_num = 0
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z

print('Exercise 6: ', largest(1, 2, 3))



# Exercise 7: Calculate a Tip

def calculate_tip(bill_amount, tip_percentage):
    tip = (bill_amount * tip_percentage)/100
    return tip

print('Exercise 7:', calculate_tip(50, 20))


# Exercise 8: Calculate Product of Numbers

def product(*args):
    result = 1
    for number in args:
        result = result * number
    return result

print('Exercise 8:', product(2, 5, 5))


# Exercise 9: Basic calculator

def basic_calculator(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:  # Handle division by zero
            return "Error! Division by zero."
        return num1 / num2
    else:
        return "Invalid operation!"  # Return this if the operation is not recognized
    
print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))