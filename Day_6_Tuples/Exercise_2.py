# Unpack siblings and parents from family_members
# family_members from Exercise 1
family_members = ('Lorenzo', 'Dillon', 'Angel', 'Ella', 'Charolette', 'Anos', 'Jim', 'Kathrin')
siblings = family_members[0:-2]
parents = family_members[-2:]
print(siblings)
print(parents)

# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp
fruits = ('apple', 'banana', 'strawberry', 'mango')
vegetables = ('Carrot', 'Broccoli', 'asparagus')
animal_products = ('steak', 'chicken breast', 'pork chop')
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)

# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
if len(food_stuff_lt) & 1 == 0:
    slice_middle_item = food_stuff_lt[0:len(food_stuff_lt) // 2 - 1] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:]
else:
    slice_middle_item = food_stuff_lt[0:len(food_stuff_lt) // 2] + food_stuff_lt[len(food_stuff_lt) // 2 + 1:]
print(slice_middle_item)

# Slice out the first three items and the last three items from food_staff_lt list
slice_first_last_three = food_stuff_lt[3:-3]
print(slice_first_last_three)

# Delete the food_staff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
if 'Estonia' in nordic_countries:
    print("Estonia is a nordic country.")
else:
    print("Estonia is not a nordic country.")

if 'Iceland' in nordic_countries:
    print("Iceland is a nordic country.")
else:
    print("Iceland is not a nordic country.")