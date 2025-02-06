# Get user input using input(“Enter your age: ”). If user is 18 or older,
# give feedback: You are old enough to drive. 
# If below 18 give feedback to wait for the missing amount of years.
age = int(input("Enter your age: "))
print('You are old enough to drive.') if age >= 18 else print('You need {} more years to learn to drive.' .format(18 - age))

# Compare the values of my_age and your_age using if … else. 
# Who is older (me or you)?
my_age = 20
your_age = int(input('Enter your age: '))
if my_age > your_age:
    print('I am {} year(s) older than you.' .format(my_age - your_age))
elif my_age < your_age:
    print('You are {} year(s) older than me.' .format(your_age - my_age))
else:
    print('You are the same age as me.')
# Get two numbers from the user using input prompt. If a is greater than b 
# return a is greater than b, if a is less b return a is smaller than b, 
# else a is equal to b
a = input("Enter number one: ")
b = input("Enter number two: ")
if a > b:
    print('{} is greater than {}' .format(a, b))
elif a < b:
    print('{} is less than {}' .format(a, b))
else:
    print('{} is equal to {}' .format(a, b))