# Exercise 1: Calculate Area of a Triangle
def calculate_area_triangle(base, height):
    area = (base * height) /2
    return area
    
print('Exercise 1 (10, 5):', calculate_area_triangle(10, 5)) # calculate_area_triangle(10, 5) should return 25.0.
print('Exercise 1 (7, 3):', calculate_area_triangle(7, 3))  # calculate_area_triangle(7, 3) should return 10.5.



# Exercise 2: Calculate Simple Interest
def simple_interest(principal, rate, time):
    interest= (principal * rate * time) / 100
    return interest

print('Exercise 2 (1000, 5, 2):', simple_interest(1000, 5, 2))   # simple_interest(1000, 5, 2) should return 100.
print('Exercise 2 (1500, 3.5, 5):', simple_interest(1500, 3.5, 5)) # simple_interest(1500, 3.5, 5) should return 262.5.



# Exercise 3: Apply a Discount
def apply_discount(price, discount):

    if discount > 100 or discount < 0:
        print("Invalid discount number")

    discount_percentage= (price * discount) / 100
    discount_price = price - discount_percentage
    return discount_price

print('Exercise 3 (100, 25):', apply_discount(100, 25))   # apply_discount(100, 25) should return 75.
print('Exercise 3 (80, 10):', apply_discount(80, 10))    # apply_discount(80, 10) should return 72.



# Exercise 4: Convert Temperature
def convert_temperature(temp, unit):

    if unit=='C':
        temperature = (temp * 9/5) + 32
    
    elif unit=='F':
        temperature =(temp -32) * 5/9
    
    return temperature

print('Exercise 4: Convert 0°C to Fahrenheit:', convert_temperature(0, 'C'))    # convert_temperature(0, 'C') should return 32.0.
print('Exercise 4: Convert 32°F to Celsius:', convert_temperature(32, 'F'))     # convert_temperature(32, 'F') should return 0.0.



# Exercise 5: Sum to N
def sum_to(n):
    total=0

    for i in range(1, n+1):
        total += i
    
    return total

print('Exercise 5 (6):', sum_to(6))     # sum_to(6) should return 21.
print('Exercise 5 (10):', sum_to(10))    # sum_to(10) should return 55.



# Exercise 6: Find the Largest Number
def largest(x, y, z):
    return max(x, y, z)

print('Exercise 6 (1, 2, 3):', largest(1, 2, 3))  # largest(1, 2, 3) should return 3.
print('Exercise 6 (10, 4, 2):', largest(10, 4, 2))  # largest(10, 4, 2) should return 10.



# Exercise 7: Calculate a Tip
def calculate_tip(bill, tip_per):

    if bill < 0:
        print("Invalid Bbll amount") 
    if tip_per < 0 or tip_per > 100:
        print("Invalid tip percentage") 

    tip = (bill * tip_per) / 100
    return tip

print('Exercise 7 (50, 20):', calculate_tip(50, 20)) # calculate_tip(50, 20) should return 10.



# Exercise 8: Calculate Product of Numbers
def product(*args):
    product_ret=1
    
    for num in args:
        product_ret *= num
    
    return product_ret

print('Exercise 8 (2, 5, 5):', product(2, 5, 5))  # product(2, 5, 5) should return 50.
print('Exercise 8 (-1, 4):', product(-1, 4))    # product(-1, 4) should return -4.



# Exercise 9: Basic Calculator
def basic_calculator(n1, n2, oper):
    if oper=='add':
        calc = n1 + n2
    
    elif oper=='subtract':
        calc = n1 - n2

    elif oper=='multiply':
        calc = n1 * n2

    elif oper=='divide':
        calc = n1 / n2
    
    return calc

print('Exercise 9 (10, 5, "subtract"):', basic_calculator(10, 5, "subtract"))    # basic_calculator(10, 5, 'subtract') should return 5.
print('Exercise 9 (10, 5, "add"):', basic_calculator(10, 5, "add"))         # basic_calculator(10, 5, 'add') should return 15.
print('Exercise 9 (10, 5, "multiply"):', basic_calculator(10, 5, "multiply"))    # basic_calculator(10, 5, 'multiply') should return 50.
print('Exercise 9 (10, 5, "divide"):', basic_calculator(10, 5, "divide"))      # basic_calculator(10, 5, 'divide') should return 2.
