from random import randint
from string import ascii_letters, digits

# Write a function which generates a six digit/character random_user_id
def random_user_id():
    all_possible_char = ascii_letters + digits
    user_id = ""
    for i in range(6):
        user_id += all_possible_char[randint(0, len(all_possible_char) - 1)]
    return user_id

# Modify the previous task. Declare a function named user_id_gen_by_user. It doesn’t take any parameters but it takes two inputs using input(). 
# One of the inputs is the number of characters and the second input is the number of IDs which are supposed to be generated.
def random_user_id_specified_length(length):
    all_possible_char = ascii_letters + digits
    user_id = ""
    for i in range(length):
        user_id += all_possible_char[randint(0, len(all_possible_char) - 1)]
    return user_id

def user_id_gen_by_user():
    num_char = int(input("Enter the length of wanted username: "))
    num_user_names = int(input("Enter the number of wanted username(s): "))
    res = []
    for i in range(num_user_names):
        res.append(random_user_id_specified_length(num_char))
    return res

# Write a function named rgb_color_gen. It will generate rgb colors (3 values ranging from 0 to 255 each).
def rgb_color_gen():
    return "rgb(" + str(randint(0, 255)) + ", " + str(randint(0, 255)) + ", " + str(randint(0, 255)) + ")"