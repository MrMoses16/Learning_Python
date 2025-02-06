import math
# ask user for name
print("What is your first name?")
first_name = input()
print("The length of your first name is: ", len(first_name))

print("\nWhat is your last name?")
last_name = input()
print("The length of your first name is: ", len(last_name))

num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

print("\nEnter a radius for a circle: ")
rad = int(input())
area = rad * rad * math.pi
circum = rad * 2 * math.pi

print("The area of said circle is", area, "and the circumfance is", circum)

