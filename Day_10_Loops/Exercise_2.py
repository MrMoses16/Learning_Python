# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for i in range(101):
    sum = sum + i
print('The sum of all numbers from 0 to 100 is: {}' .format(sum))

# Use for loop to iterate from 0 to 100 and print the sum of all evens and the sum of all odds.
sum_even = 0
sum_odd = 0
for i in range(0, 101, 2):
    sum_even = sum_even + i
for i in range(0, 100, 2):
    sum_odd= sum_odd + i + 1
print('The sum of all evens from 0 to 100 is {}. The sum of all odds from 0 to 100 is {}.' .format(sum_even, sum_odd))