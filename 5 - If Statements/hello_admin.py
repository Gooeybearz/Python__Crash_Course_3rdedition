current_usernames = ['tom', 'tim', 'roger', 'robert', 'betty']
new_users = ['velma', 'fred', 'betty', 'TIM', 'roger']
if current_usernames:
    for username in new_users:
        if username.lower() in current_usernames:
            print('You need to enter a new username')
        else:
            print('The username is available.')
else:
    print('We need to find some users!')