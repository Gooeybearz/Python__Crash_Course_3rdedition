animal_1 = {
    'name' : 'ruthie',
    'animal' : 'dog',
    'owner' : 'michael',
}

animal_2 = {
    'name' : 'addie',
    'animal' : 'dog',
    'owner' : 'jeanne',
}

animal_3 = {
    'name' : 'wednesday',
    'animal' : 'cat',
    'owner' : 'jeanne',
}

pets = [animal_1, animal_2, animal_3]

for animal in pets:
    print(f'{animal['owner'].title()} owns {animal['name'].title()} which is a {animal['animal']}.')
