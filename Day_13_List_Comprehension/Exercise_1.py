# Filter only negative and zero in the list using list comprehension
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]

negative_and_zero = [num for num in numbers if num <= 0]
print(negative_and_zero, end='\n\n')

# Flatten the following list of lists of lists to a one dimensional list
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]

flattened = [num for row in list_of_lists for col in row for num in col]
print(flattened, end='\n\n')

# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]
pow_to_five = [(i, i ** 0, i ** 1, i ** 2, i ** 3, i ** 4, i ** 5) for i in range(11)]
print(pow_to_five, end='\n\n')

# Flatten the following list into:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

new_list = [(country_1.upper(), country_1[0:3].upper(), country_2.upper()) for row in countries for country_1, country_2 in row]
print(new_list, end='\n\n')

# Change the following list to a list of dictionaries:
# output:
# [{'country': 'FINLAND', 'city': 'HELSINKI'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

country_city = [{'country' : country, 'city' : city} for row in countries for country, city in row]
print(country_city, end='\n\n')

# Change the following list of lists to a list of concatenated strings:
# output
# ['Asabeneh Yetaeyeh', 'David Smith', 'Donald Trump', 'Bill Gates']
names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
new_list = [(name1 + ' ' + name2) for row in names for name1, name2 in row]
print(new_list, end='\n\n')

# Write a lambda function which can solve a slope or y-intercept of linear functions.
function = input("Enter a linear function (mx + b): ")
find_y_intercpet = lambda function: function[(function.index('x') + 2)] + function[function.index('x') + 4:] 
print(find_y_intercpet(function))