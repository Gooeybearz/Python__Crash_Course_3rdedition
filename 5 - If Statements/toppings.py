#requested_toppiong = ['mushroom', 'extra cheese']
#if 'mushroom' in requested_toppiong:
#    print('Adding mushrooms.')
#if 'extra cheese' in requested_toppiong:
#    print('Adding extra cheese.')
#if 'pepperoni' in requested_toppiong:
#    print('Adding pepperoni.')
#print('\nFinished making your pizza!')

# // EFFICIENT METHOD //
#requested_toppings = ['pepperoni', 'green peppers', 'extra cheese', 'bacon']
#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print('Sorry, we are out of green peppers right now.')
#    else:
#        print(f'Adding {requested_topping.title()}.')


# // CHECKING FOR EMPTY LIST //
#requested_toppings = []
#if requested_toppings:
#    for requested_topping in requested_toppings:
#        print(f'Adding {requested_topping.title()}.')
#    print('\nFinished making your pizza!')
#else:
#    print('Are you sure you want a plain pizza?')

# // MULTIPLE LISTS //
available_toppings = ['mushrooms', 'olives', 'green pepeprs', 'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['pepperoni', 'canadian bacon', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f'Adding {requested_topping.title()}.')
    else:
        print(f'Sorry, we don\'t have {requested_topping.title()}.')
print('\nFinished making your pizza.')