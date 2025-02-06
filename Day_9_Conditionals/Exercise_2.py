# Write a code which gives grade to students according to theirs scores:
# 90-100, A
# 80-89, B
# 70-79, C
# 60-69, D
# 0-59, F
grade = int(input("Input your grade: "))
if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
else:
    letter = 'F'
print("You have a(n) {}" .format(letter))

# Check if the season is Autumn, Winter, Spring or Summer. If the user input is:
# September, October or November, the season is Autumn. December, January 
# or February, the season is Winter. March, April or May, the season is 
# Spring June, July or August, the season is Summer
month = str(input("What month is it? "))
Autumn = ['September', 'October', 'November']
Winter = ['December', 'January', 'February']
Spring = ['March', 'April', 'May']

if month in Autumn:
    print("This month falls into Autumn.")
elif month in Winter:
    print("This month falls into Winter.")
elif month in Spring:
    print("This month falls into Spring.")
else:
    print("This month falls into Summer.")

# If a fruit doesn't exist in the list add the fruit to the list and print the modified list. 
# If the fruit exists print('That fruit already exist in the list')
fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = str(input("Enter a fruit: "))
if new_fruit in fruits:
    print("This fruit is already within the current list of fruits.")
else:
    fruits.append(new_fruit)
    print("The new list of fruits is: {}" .format(fruits))

