# Create an empty tuple
tpl = ()
# or
tpl = tuple()

# Create a tuple containing names of your sisters and your brothers
brothers = ('Lorenzo', 'Dillon', 'Angel')
sisters = ('Ella', 'Charolette', 'Anos')

# Join brothers and sisters tuples and assign it to siblings
siblings = brothers + sisters

# How many siblings do you have?
print("I have {} siblings." .format(len(siblings)))

# Modify the siblings tuple and add the name of your father and mother and assign it to family_members
siblings_list = list(siblings)
siblings_list.append('Jim')
siblings_list.append('Kathrin')
family_members = tuple(siblings_list)
print(family_members)
