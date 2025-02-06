# Iterate 0 to 10 using for loop, do the same using while loop.
for i in range(11):
    print(i, end=' ')
print()
count = 0
while count < 11:
    print(count, end=' ')
    count = count + 1
print()

# Iterate 10 to 0 using for loop, do the same using while loop.
for i in range(10, -1, -1):
    print(i, end=' ')
print()
count = 10
while count > -1:
    print(count, end=' ')
    count = count - 1
print()

# Write nested loops so we get on the output a triangle
for i in range(1, 8, 1):
    for j in range (i):
        print('#', end='')
    print()

# Print the following pattern: number^2 table
for i in range(11):
    print('{} x {} = {}' .format(i, i, i*i))

# Iterate through the list, ['Python', 'Numpy','Pandas','Django', 'Flask'] using a for loop and print out the items.
lst = ['Python', 'Numpy','Pandas','Django', 'Flask']
for items in lst:
    print(items, end=' ')
print()

# Use for loop to iterate from 0 to 100 and print only even numbers
for i in range (0, 101, 2):
    print(i, end=' ')
print()

for i in range (0, 100, 2):
    print(i+1, end=' ')