cars = ['bmw', 'audi', 'toyota', 'subaru']

#temporary sort
print('Here is the original list:')
print(cars)
print('\nHere is the sorted list:')
print(sorted(cars))
print('\nHere is the original list again:')
print(cars)

#Permanment sort
cars.sort()
print(f'\n{cars}')
cars.sort(reverse=True)
print(f'\n{cars}')

cars.reverse()
print(f'\n{cars}')