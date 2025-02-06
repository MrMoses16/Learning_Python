# installing packages using pip (Preferred Installer Program) 
# Step 1) Open terminal
# Step 2) pip install 'package'

# how to check the version of pip
# pip --version

# install numpy and provide example of use:
import numpy

lst = [1, 2, 3, 4, 5]
np_arr = numpy.array(lst)
print(np_arr)
print(len(np_arr))
np_arr *= 2
print(numpy)


# example of webbrowser
import webbrowser

url_list = [
    'http://www.python.org'
]

for url in url_list:
    webbrowser.open_new_tab(url)


# Uninstalling pip packages
# pip uninstall 'package'


# List of packages
# pip list


# Show information about a package
# pip show 'package'

# Show more information about a package
# pip show --verbose 'package'


# PIP Freeze generates all Python packages with their version 
# pip freeze


# Reading from URL needs the package 'requests' to be installed
# requests have the follow methods:
# get(): to open a network and fetch data from url; it returns a response object
# status_code: after we fetched data, we can check the status of the operation (success, error, etc.)
# headers: to check the header types
# text: to extract the text from the fetched response object
# json: to extract json data

import requests

url = 'https://www.w3.org/TR/PNG/iso_8859-1.txt'
response = requests.get(url)
print(response)
print(response.status_code)
print(response.headers)
print(response.text)


url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
print(response)
print(response.status_code)
countries = response.json()
print(countries[:1])







