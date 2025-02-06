# Create an empty dictionary called dog
dog = dict()

# Add name, color, breed, age to the dog dictionary
dog = {
    'name' : 'Moses',
    'color' : 'brown',
    'age' : 8
}

# Create a student dictionary and add first_name, last_name, gender, age, 
# skills, country, and city 
student = {
    'first_name' : 'Kris',
    'Last_name' : 'Tellez',
    'gender' : 'Male',
    'age' : 20,
    'skills' : ['C, Python', 'Java'],
    'country' : 'USA',
    'city' : 'Orlando'
}

# Get the length of the student dictionary
print(student)
print("The length of the following dictionary is", len(student), end="\n\n")

# Get the value of skills and check the data type, it should be a list
skills = student['skills']
print(skills)
if(isinstance(skills, list)):
    print("Skills are a list.\n")
else:
    print("Skills are not a list.\n")

# Modify the skills values by adding one or two skills
skills.append('Construction')
student['skills'] = skills
print(student['skills'], end="\n\n")

# Get the dictionary keys as a list
keys = student.keys()
print(keys)

# Get the dictionary values as a list
values = student.values()
print(values, end='\n\n')

# Change the dictionary to a list of tuples using items() method
student_tuples = tuple(student.items())

# Delete one of the items in the dictionary
student.popitem()

# Delete one of the dictionaries
del student