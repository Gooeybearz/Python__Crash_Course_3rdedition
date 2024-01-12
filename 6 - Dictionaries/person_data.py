person_1 = {
    'first_name' : 'michael',
    'last_name' : 'jones',
    'age' : 24,
    'city' : 'orlando',
    }

person_2 = {
    'first_name' : 'james',
    'last_name' : 'may',
    'age' : 60,
    'city' : 'london',
}

person_3 = {
    'first_name' : 'richard',
    'last_name' : 'hammond',
    'age' : 54,
    'city' : 'leeds',
}

people = [person_1, person_2, person_3]


for person in people:
    #PRINT NAME, AGE, AND CITY
    first_name = person['first_name']
    last_name = person['last_name']
    age = person['age']
    city = person['city']
    full_name = f'{first_name} {last_name}'
    print(f'\nFull name : {full_name.title()}'
          f'/\nAge : {age}'
          f'\nCity : {city.title()}')

   
    