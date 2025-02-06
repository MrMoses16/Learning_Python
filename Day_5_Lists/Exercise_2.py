# Given list of 10 students
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
print(ages)

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]
print("The minimum age is {} and the maximum age is {}." .format(min_age, max_age))
# Add the min age and the max age again to the list
ages.append(min_age)
ages.append(max_age)
print(ages)
# Find the median age (one middle item or two middle items divided by two)
median_age = ''
ages.sort()
if len(ages) % 2 == 0:
    median_age = (ages[len(ages)//2 - 1] + ages[len(ages)//2]) / 2
else:
    median_age = ages[len(ages)//2]
print("The median age of the list is", median_age)
# Find the average age (sum of all items divided by their number)
sum = 0
for i in range(0, len(ages)):
    sum += ages[i]
average_age = sum / len(ages)
print("The average age is", average_age)
# Find the range of the ages (max minus min)
range = max_age - min_age
print("The range is", range)
# Compare the value of (min - average) and (max - average), use abs() method
min_average = abs(min_age - average_age)
max_average = abs(max_age - average_age)
print("The value of (min - average) is {} and (max - average) is {}" .format(min_average, max_average))

# Find the middle country(ies) in the given list
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]

# Find the middle country(ies)
if len(countries) % 2 == 0:
    middle_country = countries[len(countries) // 2 - 1] + countries[len(countries) // 2]
else:
    middle_country = countries[len(countries) // 2]
print("The middle country within the list is", middle_country)

# Divide the countries list into two equal lists if it is even if not one more country for the first half
if len(countries) % 2 == 0:
    first_half = countries[0:len(countries) // 2]
    second_half = countries[len(countries) // 2:]
else:
    first_half = countries[0:len(countries) // 2 + 1]
    second_half = countries[len(countries) // 2 + 1:]

print("The first half of the list is:", first_half)
print("\nThe second half of the list is:", second_half)

# ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']. 
# Unpack the first three countries and the rest as scandic countries
first_country, second_country, third_country, *rest = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print("The first country is {}, the second country is {}, the third country is {}, and the rest are {}." .format(first_country, second_country, third_country, rest))