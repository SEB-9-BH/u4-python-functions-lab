# Exercise 1: Calculate Area of a Triangle
#
# Write a function named `calculate_area_triangle` that takes the base and height
# of a triangle and returns the area.
# The area formula is (base * height) / 2.
#
# Examples:
# calculate_area_triangle(10, 5) should return 25.0
# calculate_area_triangle(7, 3) should return 10.5

# Define the function
def calculate_area_triangle(base, height):
    return (base * height) / 2

# Call the function with sample inputs and print the results
print('Exercise 1:', calculate_area_triangle(10, 5))
print('Exercise 1:', calculate_area_triangle(7, 3))


# Exercise 2: Calculate Simple Interest
#
# Write a function named `simple_interest` that takes principal, rate of interest (as a percentage), and time (years).
# Calculate and return the simple interest using the formula: (principal * rate * time) / 100

# Define the function
def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Call the function with example values and print the result
print('Exercise 2:', simple_interest(1000, 5, 2))
print('Exercise 2:', simple_interest(1500, 3.5, 5))

# Exercise 3: Apply a Discount
#
# Write a function named `apply_discount` that takes a product's price and a discount percentage (from 0 to 100).
# Return the new price after applying the discount.

# Define the function
def apply_discount(price, discount_percent):
    discount_amount = (price * discount_percent) / 100
    return price - discount_amount

# Call the function with example inputs and print the result
print('Exercise 3:', apply_discount(100, 25))
print('Exercise 3:', apply_discount(80, 10))


# Exercise 4: Convert Temperature
#
# Write a function called `convert_temperature` that takes a
# temperature and a unit ('C' for Celsius, 'F' for Fahrenheit)
# and converts the temperature to the other unit.

# Define the function
def convert_temperature(temp, unit):
    if unit == 'C':
        # Convert Celsius to Fahrenheit
        return (temp * 9/5) + 32
    elif unit == 'F':
        # Convert Fahrenheit to Celsius
        return (temp - 32) * 5/9
    else:
        # Invalid unit
        return "Invalid unit. Use 'C' for Celsius or 'F' for Fahrenheit."

# Call the function and print results
print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))



# Exercise 5: Sum to N
#
# Write a function named `sum_to` that takes a single integer n
# and returns the sum of all integers from 1 to n.

# Define the function
def sum_to(n):
    return sum(range(1, n + 1))

# Call the function with example values and print the results
print('Exercise 5:', sum_to(6))
print('Exercise 5:', sum_to(10))


# Exercise 6: Find the Largest Number
#
# Write a function named `largest` that takes three integers as arguments
# and returns the largest of them.

# Define the function
def largest(a, b, c):
    return max(a, b, c)

# Call the function with sample inputs and print the results
print('Exercise 6:', largest(1, 2, 3))
print('Exercise 6:', largest(10, 4, 2))
print('Exercise 6:', largest(5, 15, 10))




# Exercise 7: Calculate a Tip
#
# Create a function called `calculate_tip`. It should take the bill amount and the tip percentage (as a whole number).
# The function should return the amount of the tip.

# Define the function
def calculate_tip(bill_amount, tip_percent):
    return (bill_amount * tip_percent) / 100

# Call the function and print the result
print('Exercise 7:', calculate_tip(50, 20))



# Exercise 8: Calculate Product of Numbers
#
# Write a function named `product` that takes an arbitrary number of numbers,
# multiplies them, and returns the product.

# Define the function
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

# Call the function and print the result
print('Exercise 8:', product(2, 5, 5))
print('Exercise 8:', product(-1, 4))
print('Exercise 8:', product(1, 2, 3, 4))

def basic_calculator(num1,num2,operation):
    if operation == "add":
        return(num1 + num2)
    elif operation == "subtract":
        return(num1 - num2)
    elif operation == "multiply":
        return(num1 * num2)
    elif operation == "divide":
        return(num1 / num2)
    else:
        return("not a valid operation")
print('Exercise 9 Result:', basic_calculator(10, 5, "subtract"))
