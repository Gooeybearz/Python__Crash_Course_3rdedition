favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
 }

friends = ['sarah', 'edward']

if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!')


# SAME AS (for name in favorite_languages:)
for name in favorite_languages.keys():
    print(f'Hello {name.title()}')
    if name in friends:
        language = favorite_languages[name].title()
        print(f'\t{name.title()}, I see you love {language}!')