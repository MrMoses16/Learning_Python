import requests
from bs4 import BeautifulSoup

url = 'https://archive.ics.uci.edu/ml/datasets.php'

# use requests get method to fetch the data
response = requests.get(url)

# check the status
status = response.status_code
print(status) # 200 means successful fetch

# Using beautifulSoup to parse content from page
content = response.content # get all the content from the website
soup = BeautifulSoup(content, 'html.parser')
print(soup.title) # <title> text</title>
print(soup.title.get_text()) # text
print(soup.body) # gives the whole page on the website

tables = soup.find_all('table', {'cellpadding' : '3'}) 
# We are targetung the table with cellpadding attribute with the value of 3
# We can select using id, class or HTML tag
if len(tables) > 0:
    table = tables[0] # result is a list taken from the data
    for td in table.find('tr').findall('td'):
        print(td.text)