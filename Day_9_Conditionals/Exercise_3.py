# person based on teacher from python course
person={
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
    }

 # Check if the person dictionary has skills key, if so print out the middle skill in the skills list.
 # Check if the person dictionary has skills key, if so check if the person has 'Python' skill and print out the result.
 # If a person skills has only JavaScript and React, print('He is a front end developer'), 
 # if the person skills has Node, Python, MongoDB, print('He is a backend developer'), 
 # if the person skills has React, Node and MongoDB, Print('He is a fullstack developer'), 
 # else print('unknown title') - for more accurate results more conditions can be nested!
 # If the person is married and if he lives in Finland, print the information in the following format:
 # Asabeneh Yetayeh lives in Finland. He is married.

if person.get('skills'):
    person_length = len(person['skills'])
    if person_length & 1 == 1:
        middle = person_length // 2 + 1
    else:
        middle = person_length // 2
    print(person['skills'][middle - 1])

    if 'Python' in person['skills']:
        print("Person has python skills.")
    
front_end_dev = ['JavaScript', 'React']
flag = False
if front_end_dev == person['skills']:
    print("Person is a front end developer.")
    flag = True
if 'Python' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print('Person is a back end developer.')
    flag = True
if 'React' in person['skills'] and 'Node' in person['skills'] and 'MongoDB' in person['skills']:
    print("Person is a fullstack developer.")
    flag = True
if not flag:
    print("Person has Unknown Title")

if person['is_marred'] and person['country'] == "Finland":
    print("{} {} lives in Finland. He is married." .format(person['first_name'], person['last_name']))