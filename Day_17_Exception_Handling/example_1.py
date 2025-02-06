# Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print("Unpack the first five countries from given list and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.")
print(f"The nordic countriesd are {nordic_countries}") 
print(f"es represents {es} and ru represents {ru}\n")

# An example of exception handling
try:
    print("Exception handling is structured with a \'try\', \'except\', \'else\', and \'finally\'.\nIn this example, the code is trying to access an array not declared yet.\n")
    response = input("Would you like to cause an exception: yes or no\n")
    if response == "yes":
        x = arr[10]
except Exception as e:
    print(f"Something went wrong: {e}")
else:
    print("The \'else\' section of the exception handling runs only if an exception was not thrown.")
finally:
    print("The \'finally\' section of exception handling always runs reguardless of if an exception was thrown.\n")

# Unpacking a list
lst = [1, 2, 3]
def sum_of_three_num(a, b, c):
    return a + b + c

sum = sum_of_three_num(*lst)

# Unpacking a dictionary
def unpacking_person_info(name, age, country):
    return f"My name is {name} and live in {country}. I am {age} year(s) old."

person_info = {'name' : 'Kris', 'age' : '20', 'country' : 'USA'}
print("Example of unpacking a dictionary:")
print(unpacking_person_info(**person_info))

# Packing a list
def sum_all_num(*lst):
    sum = 0
    for num in lst:
        sum += num
    return sum

sum = sum_all_num(*lst)

# Packing a dictionary
def packing_a_dict(**args):
    for key in args:
        print(f"{key} = {args[key]}")

print("\nExample of packing a dictionary")  
packing_a_dict(**person_info)

# Spreading
lst_1 = [1, 2, 3]
lst_2 = [4, 5, 6]

lst = [*lst_1, *lst_2]

# Enumerate gets the index of each item in the list
print("\nExample of using enumerate: gets the index of each item in the list")
for index, item in enumerate(lst):
    print(index, item)

# Zip combines lists
even = [0, 2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
even_and_odd = []
for even, odd in zip(even, odd):
    even_and_odd.append([even, odd])

print("\nExample of using zip: combines lists")
print(even_and_odd)


