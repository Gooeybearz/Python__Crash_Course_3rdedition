#3.4
guests = ['Abe', 'albert', 'robin']
for i in range(3):
    print(f'I would like to invite you, {guests[i].title()}, over for dinner.')
#3.5
unavailable_guests = guests.pop(1)
print(f'I am sorry you, {unavailable_guests.title()}, cannot make it to this party, maybe next time.')
#3.6
guests.insert(0, 'roger')
guests.insert(1, 'tim')
guests.append('john')
print(guests)
for i in range(5):
    print(f'I would like to invite you, {guests[i].title()}, over for dinner.')
#3.7
unavailable_guests = guests.pop()
print(f'I am sorry you will not be able to make it sonce we only have enough spots for two people. I do apoligize {unavailable_guests.title()}.')
unavailable_guests = guests.pop(0)
print(f'I am sorry you will not be able to make it sonce we only have enough spots for two people. I do apoligize {unavailable_guests.title()}.')
unavailable_guests = guests.pop(0)
print(f'I am sorry you will not be able to make it sonce we only have enough spots for two people. I do apoligize {unavailable_guests.title()}.')
print(f'There are {str(len(guests))} guests coming to dinner now.')

for i in range(2):
    print(f'You are still invited to the party {guests[i]}.')

del guests[0]
del guests[0]
print(guests)
        
