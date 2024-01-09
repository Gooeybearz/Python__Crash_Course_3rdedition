rivers = {'egypt' : 'nile', 'usa' : 'mississippi','germany' : 'rhine'}
for country, river in rivers.items():
    if country == 'usa':
        country = country.upper()
    else:
        country = country.title()
    print(f'The {river.title()} is in {country}')