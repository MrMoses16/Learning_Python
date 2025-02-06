import re

# Write a pattern which identifies if a string is a valid python variable
def is_valid_variable(str):
    match = re.findall(r'^[a-zA-Z_][a-zA-Z0-9_]*$', str, re.I)
    if len(match) > 0:
        return "True"
    else:
        return "False"
    
print(is_valid_variable('first_name')) # True
print(is_valid_variable('first-name')) # False
print(is_valid_variable('1first_name')) # False
print(is_valid_variable('firstname')) # True
print(is_valid_variable('first_name_1')) # True