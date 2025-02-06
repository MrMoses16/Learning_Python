# sets
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}

# Find the length of the set it_companies
print(it_companies)
print("The set above contains {} item(s)." .format(len(it_companies)))

# Add 'Twitter' to it_companies
it_companies.add('Twitter')
print(it_companies)

# Insert multiple IT companies at once to the set it_companies
it_companies.update(['Instagram', 'Snapchat', 'Samsung'])
print(it_companies)

# Remove one of the companies from the set it_companies
it_companies_copy = it_companies.copy()
if 'Facebook' in it_companies:
    it_companies.remove('Facebook')

print(it_companies)

# What is the difference between remove and discard
difference = it_companies_copy.difference(it_companies)
print(difference)