import math
# Declare a function add_two_numbers. It takes two parameters and it returns a sum.
def add_two_numbers(num1, num2):
    return num1 + num2

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.
def area_of_circle(radius):
    return 3.14 * radius * radius

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. 
# Check if all the list items are number types. If not do give a reasonable feedback.
def add_all_nums(*nums):
    sum = 0
    for i in nums:
        if isinstance(i, int):
            sum += i
        else:
            return "Incorrect data type."
    return sum

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. 
# Write a function which converts °C to °F, convert_celsius_to-fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.
def check_season(month):
    Winter = ['December', 'January', 'Febuary',]
    Spring = ['March', 'April', 'May']
    Summer = ['June', 'July', 'August']
    if month in Winter:
        return "Winter"
    if month in Spring:
        return "Spring"
    if month in Summer:
        return "Summer"
    return "Fall"

# Write a function called calculate_slope which return the slope of a linear equation
def calculate_slope(equation):
    return int(equation[0:equation.index("x")])

# Quadratic equation is calculated as follows: ax² + bx + c = 0. 
# Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.
def solve_quadratic_equ(equation):
    a = int(equation[0 : equation.index("x^2")])
    b = int(equation[equation.index("x^2")+6 : equation.index("x ")])
    c = int(equation[equation.index("x ")+3:])
    if b * b < 4 * a * c:
        return "No Solution"
    res = []
    x = (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a)
    res.append(x)
    x = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    res.append(x)
    return res

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.
def print_list(lst):
    for i in lst:
        print(i, end=' ')

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).
def reverse_list(lst):
    rev_lst = lst.copy()
    for i in range(len(lst)):
        rev_lst[i] = lst[len(lst) - 1 - i]
    return rev_lst

# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items
def capitalize_list_items(lst):
    cap_list = []
    for i in lst:
        if not i.isupper():
            cap_list.append(i.upper())
        else:
            cap_list.append(i)
    return cap_list

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.
def add_item(lst, item):
    new_list = lst.copy()
    new_list.append(item)
    return new_list

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.
def remove_item(lst, item):
    new_list = lst.copy()
    new_list.remove(item)
    return new_list

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.
def sum_of_numbers(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.
def sum_of_odds(num):
    sum = 0
    for i in range(0, num, 2):
        sum += i+1
    return sum

# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that range.
def sum_of_even(num):
    sum = 0
    for i in range(0, num+1, 2):
        sum += i
    return sum
