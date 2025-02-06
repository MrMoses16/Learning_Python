# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'
str1 = 'Thirty'
str2 = 'Days'
str3 = 'Of'
str4 = 'Python'
space = ' '
single_str = str1 + space + str2 + space + str3 + space + str4
print(single_str)

# Concatenate the string 'Coding', 'For' , 'All' to a single string, 'Coding For All'
str1 = 'Coding'
str2 = 'For'
str3 = 'All'
single_str = str1 + space + str2 + space + str3
print(single_str)

# Declare a variable named company and assign it to an initial value "Coding For All"
company = single_str

# Print the variable company using print()
print(company)

# Print the length of the company string using len() method and print()
print(len(company))

# Change all the characters to uppercase letters using upper() method
print(company.upper())

# Change all the characters to lowercase letters using lower() method
print(company.lower())

# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All
print(company.capitalize())
print(company.title())
print(company.swapcase())

# Cut(slice) out the first word of Coding For All string
print(company[7:])

# Check if Coding For All string contains a word Coding using the method index, find or other methods
print("Check if \"Coding For All\" string contains a word \"Coding\": ", company.index('Coding') >= 0)

# Replace the word coding in the string 'Coding For All' to Python
company = company.replace('Coding', 'Python')
print(company)

# Change Python for Everyone to Python for All using the replace method or other methods
company = company.replace('Python', 'Everyone')
print(company)

# Split the string 'Coding For All' using space as the separator (split())
company = 'Coding For All'
company = company.split()
print(company)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma
str = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
str = str.split(',')
print(str)

# What is the character at index 0 in the string Coding For All
company = 'Coding For All'
print("Character at index 0 is: ", company[0])

# What is the last index of the string Coding For All
print("The last index is: ", len(company) - 1)

# What character is at index 10 in "Coding For All" string
print("Character at index 10 is: ", company[10])

# Create an acronym or an abbreviation for the name 'Python For Everyone'
str = 'Python For Everyone'
result = ''
for i in range(0, len(str)):
    if str[i].isupper():
        result += str[i]
print(result)

# Use index to determine the position of the first occurrence of C in Coding For All
print("Index of C in \"Coding For All\" is: ", company.index('C'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People
str = "Coding For All People"
print("The last index of I in \"Coding For All People\" is: ", str.rfind('I'))

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
str1 = 'You cannot end a sentence with because because because is a conjunction'
str2 = 'because because because '
print(str1.replace(str2, ''))

# Does 'Coding For All' start with a substring Coding
str = 'Coding For All'
print("Does \"Coding For All\" start with \"Coding\"? ", str.startswith('Coding'))

# Does 'Coding For All' end with a substring coding?
print("Does \"Coding For All\" end with \"Coding\"? ", str.endswith('Coding'))

# '   Coding For All      '  , remove the left and right trailing spaces in the given string
str = '   Coding For All      '
str = str.strip(' ')
print(str)

# Which one of the following variables return True when we use the method isidentifier():
str = '30DaysOfPython'
print("isidentifier() on the string \"30DaysOfPython:", str.isidentifier())
str = 'thirty_days_of_python'
print("isidentifier() on the string \"thirty_days_of_python:", str.isidentifier())

# The following list contains the names of some of python libraries: 
# ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. 
# Join the list with a hash with space string.
list = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
list = '-'.join(list)
print(list)

# Use the string formatting method to display the following:
radius = 10
area = 3.14 * radius ** 2
print("The are of a circle with the radius %d is %.2f" %(radius, area))

# Make the following using string formatting methods
print('8 + 6 = {}\n8 - 6 = {}\n8 * 6 = {}\n8 / 6 = {:.2f}\n8 % 6 = {}\n8 // 6 = {}\n8 ** 6 = {}' .format(8+6, 8-6, 8*6, 8/6, 8%6, 8//6, 8**6))
