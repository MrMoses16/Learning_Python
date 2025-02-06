# sets
age = [22, 19, 24, 25, 26, 24, 25, 24]

# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age)
print(age)
print(age_set)

if len(age) > len(age_set):
    print("Length of age list is larger than age set.\n")
elif len(age) < len(age_set):
    print("Length of age set is larger than age list.\n")
else:
    print("Age list and age set have the same length.\n")

# "I am a teacher and I love to inspire and teach people.""
# How many unique words have been used in the sentence? 
# Use the split methods and set to get the unique words.
str = 'I am a teacher and I love to inspire and teach people.'
list = str.split(' ')
str_set = set(list)
print("Their are {} unique words in the following sentence: {}" .format(len(str_set), str))