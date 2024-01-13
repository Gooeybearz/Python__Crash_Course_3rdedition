favorite_numbers = {
    'ray' : [42, 27],
    'tim' : [37, 11],
    'roger' : [25, 99],
    'bill' : [69, 420],
    'michael' : [42, 300],
}

for person, favorite_numbers in favorite_numbers.items():
    print(f'\n{person.title()}\'s favorite number is:')
    for number in favorite_numbers:
        print(f'\t{number}')
