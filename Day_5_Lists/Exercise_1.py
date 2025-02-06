# Declare an empty list
empty_list = []

# Declare a list with more than 5 items
pets = ['dog', 'cat', 'hamster', 'bird', 'fish', 'lizard']

# Find the length of your list
len_pets = len(pets)
print("Length of pets list is",len_pets)

# Get the first item, the middle item and the last item of the list
first_item = pets[0]
middle_item = pets[len_pets//2]
last_item = pets[-1]
print("First item is {}, middle item is {}, last time is {}" .format(first_item, middle_item, last_item))

# Declare a list called mixed_data_types, put your(name, age, height, marital status)
mixed_data_types = ['Kris', '20', '5.5', 'False']

#Declare a list variable named it_companies and assign initial values Facebook, Google, Microsoft, Apple, IBM, Oracle and Amazon
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the list using print()
print(it_companies)

# Print the number of companies in the list
print("Length of list above is", len(it_companies))

# Print the first, middle and last company
first_item = it_companies[0]
middle_item = it_companies[len(it_companies)//2]
last_item = it_companies[-1]
print("First item is {}, middle item is {}, last time is {}" .format(first_item, middle_item, last_item))

# Print the list after modifying one of the companies
it_companies[3] = 'Samsung'
print(it_companies)

# Add an IT company to it_companies
it_companies.append('Apple')
print(it_companies)

# Insert an IT company in the middle of the companies list
it_companies.insert(len(it_companies)//2, 'Instagram')
print(it_companies)

# Change one of the it_companies names to uppercase
it_companies[0] = it_companies[0].upper()
print(it_companies)

# Join the it_companies with a string '#;  '
it_companies_str = '#'.join(it_companies)
print(it_companies_str)

# Check if a certain company exists in the it_companies list
contains_Google = 'Google' in it_companies
print("Is \"Google\" within the list?", contains_Google)

# Sort the list using sort() method
it_companies.sort()
print(it_companies)

# Reverse the list in descending order using reverse() method
it_companies.sort(reverse = True)
# or it.companies.reverse()
print(it_companies)

# Slice out the first 3 companies from the list
print(it_companies[3:])

# Slice out the last 3 companies from the list
print(it_companies[:-3])

# Slice out the middle IT company or companies from the list
print(it_companies[0:len(it_companies)//2] + it_companies[len(it_companies)//2+1:])

# Remove the first IT company from the list
del it_companies[0]
print(it_companies)

# Remove the middle IT company or companies from the list
it_companies.pop(len(it_companies)//2)
print(it_companies)

# Remove the last IT company from the list
it_companies.pop()
print(it_companies)

# Remove all IT companies from the list
it_companies.clear()
print(it_companies)

# Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
front_back_end = front_end + back_end
print(front_back_end)

# After joining the lists in question 26. Copy the joined list and assign it to a variable full_stack. 
# Then insert Python and SQL after Redux
copy_front_back_end = front_back_end.copy()
copy_front_back_end.insert(front_back_end.index('Redux'), 'Python')
copy_front_back_end.insert(front_back_end.index('Redux'), 'SQL')
print(copy_front_back_end)