favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

people = ['jen', 'sarah', 'tim', 'phil']

for name in favorite_languages:
    if name in people:
        print(f'{name.title()}, thank you for responding to our poll.')
    else:
        print(f'{name.title()}, we would like to invite you to take our poll.')
