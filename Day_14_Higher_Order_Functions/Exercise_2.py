from functools import reduce
from string import ascii_uppercase

countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use map to create a new list by changing each country to uppercase in the countries list
def uppercase(name):
    return name.upper()
uppercase_countries = map(uppercase, countries)
print(list(uppercase_countries))

# Use map to create a new list by changing each number to its square in the numbers list
def square(num):
    return num * num
square_list = map(square, numbers)
print(list(square_list))

# Use map to change each name to uppercase in the names list
uppercase_names = map(uppercase, names)
print(list(uppercase_names))

# Use filter to filter out countries containing 'land'.
def contains_land(name):
    if 'land' in name:
        return False
    return True
countries_without_land = filter(contains_land, countries)
print(list(countries_without_land))

# Use filter to filter out countries having exactly six characters.
def exactly_six_letters(name):
    if len(name) == 6:
        return False
    return True
countries_excluding_six_char = filter(exactly_six_letters, countries)
print(list(countries_excluding_six_char))

# Use filter to filter out countries containing six letters and more in the country list.
def exactly_six_letters(name):
    if len(name) >= 6:
        return False
    return True
countries_under_six_char = filter(exactly_six_letters, countries)
print(list(countries_under_six_char))

# Use filter to filter out countries starting with an 'E'
def starting_with_E(name):
    if name[0] == 'E':
        return False
    return True
countries_not_starting_with_E = filter(starting_with_E, countries)
print(list(countries_not_starting_with_E))

# Chain two or more list iterators
def is_even(num):
    return num & 1 == 0

def sum(num1, num2):
    return num1 + num2
sum_even_num = reduce(sum, list(filter(is_even, numbers)))
print(sum_even_num)

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.
def get_string_list(lst):
    res = []
    for i in lst:
        if isinstance(i, str):
            res.append(i)
    return res
print(get_string_list(numbers))

# Use reduce to sum all the numbers in the numbers list.
sum_num = reduce(sum, numbers)
print(sum_num)

# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
def list_to_string(item1, item2):
    if item1 == countries[-1]:
        return item1 + ", and " + item2
    if item2 == countries[-1]:
        return item1 + ", and " + item2
    return item1 + ', ' + item2
    
print("{} are north European countries." .format(reduce(list_to_string, countries)))

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
# Declare a function called categorize_countries that returns a list of countries with some common pattern.
def is_land(name):
    if 'Island' in name:
        return False
    return 'land' in name

def is_stan(name):
    return 'stan' in name

def is_ia(name):
    return 'ia' in name

def is_island(name):
    return 'Island' in name

def categorize_countries(lst):
    countries_land = list(filter(is_land, lst))

    countries_stan = list(filter(is_stan, lst))

    countries_ia = list(filter(is_ia, lst))

    countries_island = list(filter(is_island, lst))

    return countries_land + countries_stan + countries_ia + countries_island

print(categorize_countries(countries))

# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.
def sort_alph(alph, lst):
    res = []
    for i in lst:
        if i[0] == alph:
            res.append(i)
    return res

def sort_by_first_letter(lst):
    countries_by_first_letter = dict()
    alphabet = list(ascii_uppercase)
    for i in alphabet:
        countries_by_first_letter[i] = sort_alph(i, lst)
    return countries_by_first_letter

print(sort_by_first_letter(countries))


