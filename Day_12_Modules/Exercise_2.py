from random import randint
from string import ascii_letters, digits
from Exercise_1 import rgb_color_gen

# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. 
# Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. 
def list_of_hexa_colors(num):
    all_possible_values = digits + ascii_letters[0:6]
    res = []
    for i in range(num):
        value = "#"
        for j in range(6):
            value += all_possible_values[randint(0, len(all_possible_values) - 1)]
        res.append(value)
    return res

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.
def list_of_rgb_colors(num):
    res = []
    for i in range(num):
        res.append(rgb_color_gen())
    return res

# Write a function generate_colors which can generate any number of hexa or rgb colors.
def generate_colors(input_type, num):
    if input_type == 'hexa':
        return list_of_hexa_colors(num)
    if input_type == 'rgb':
        return list_of_rgb_colors(num)
    return "Invalid input type."
