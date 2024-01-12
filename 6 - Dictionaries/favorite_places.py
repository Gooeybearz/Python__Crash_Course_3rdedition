favorite_places = {
    'jim' :  ['home', 'farm'],
    
    'sarah' : ['lake', 'gym'],

    'roger' :  ['gym', 'office'],
}

for person, places in favorite_places.items():
    print(f'{person.title()}\'s favorite places are:')
    for place in places:
        print(f'\t{place}')

