cities = {
    'chicago' : {
        'country' : 'united states of america',
        'population' : 20_000_000,
        'fact' : 'windy city comes from people being full of hot air',
    },

    'new york' : {
        'country' : 'united states of america',
        'population' : 35_000_000,
        'fact' : 'the city that never sleeps',
    },

    'london' : {
        'country' : 'united kingdom',
        'population' : 15_750_000,
        'fact' : 'the king lives in a castle',
    },

    'paris' : {
        'country' : 'france',
        'population' : 12_500_000,
        'fact' : 'the eiffel tower is located here',
    },
}

for city, city_info in cities.items():
    location = city_info['country']
    population = city_info['population']
    interesting_fact = city_info['fact']
    print(f'\nInformation about the city of {city.title()}:'
          f'\n\t{city.title()} is located in {location.title()}'
          f'\nAn interesting fact about {city.title()} is : \'{interesting_fact.title()}.\' '
          )




