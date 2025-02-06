# declare int, float, and complex variables
age = 20
height = 5.5
complex_number = 2 + 5j

# prompt user to enter dimensions of a rectangle
print("Lets build a rectangle.")
print("Enter base: ")
base = float(input())
print("Enter height: ")
height = float(input())
area = base * height
print("The area of the rectangle is", area)

# prompt user to enter side dimensions of a triangle
print("\nLets build a triangle.")
print("Enter side a: ")
a = float(input())
print("Enter side b: ")
b = float(input())
print("Enter side c: ")
c = float(input())
perimeter = a + b + c
print("The perimenter of triangle is", perimeter)

# prompt user to enter two point (x, y) and calculate slope
print("\nEnter position of point one (x 'enter' y): ")
x1 = float(input())
y1 = float(input())
print("Enter position of point two (x 'enter' y: ")
x2 = float(input())
y2 = float(input())
slope = (y2 - y1) / (x2 - x1)
print("The slope between the two points is", slope)

# comparing strings 
dragon = 'dragon'
python = 'python'
print("\nThe world dragon is the same length as python:", len(dragon) == len(python))
print("\nIs 'on' within the word dragon and python: ", 'on' in dragon and 'on' in python)

# converting from one data type to another
len = len(python)
len_float = float(len)
len_string = str(len)

# comparing different data types
print("Is '10' equivalent to 10:", '10' == 10)
print("Is '9.8' equal to 10:", int(float('9.8')) == 10)

# print an exponent table
print("Lets build an exponent table.\nEnter max natural number value for the base:", end = ' ')
base_exp = int(input())
print("Enter max natural number value for the power:", end = ' ')
power_exp = int(input()) 
for i in range(1, base_exp+1):
    print(i, end = ' ')
    for j in range(power_exp+1):
        print(i ** j, end = ' ')
    print()

