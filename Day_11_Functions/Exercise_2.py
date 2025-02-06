import math
# Declare a function named evens_and_odds. It takes a positive integer as parameter and it counts number of evens and odds in the number.
def evens_and_odds(num):
    even = num // 2 + 1
    if num & 1 == 1:
        odd = even
    else:
        odd = even - 1
    print("The number of odds are {}. The number of evens are {}." .format(odd, even))

# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number
def factorial(num):
    fact = 1
    for i in range(1, num+1, 1):
        fact *= i
    return fact

# Call your function is_empty, it takes a parameter and it checks if it is empty or not
def is_empty(parameter):
    if len(parameter) == 0:
        return True
    else:
        return False
    
# Write different functions which take lists. 
# They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).
def calculate_mean(lst):
    sum = 0
    for i in lst:
        sum += i
    return sum / len(lst)

def calculate_median(lst):
    new_list = lst.copy()
    new_list.sort()
    if len(lst) & 1 == 1:
        return new_list[len(new_list) // 2]
    else:
        return (new_list[len(new_list) // 2 - 1] + new_list[len(new_list) // 2]) / 2
    
lst = [1, 2, 3, 4]

def calculate_range(lst):
    new_list = lst.copy()
    new_list.sort()
    return new_list[len(new_list) - 1] - new_list[0]

def calculate_variance(lst):
    mean = calculate_mean(lst)
    sum = 0
    for i in lst:
        diff = i - mean
        diff_squared = diff * diff
        sum += diff_squared
    return sum / (len(lst) - 1)

def calculate_std(lst):
    return math.sqrt(calculate_variance(lst))
