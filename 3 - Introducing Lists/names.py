names = ['robert', 'david', 'jeanne', 'ying']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())
#Print a greeting to everyone in the list
for i in range(0,4):
    print(f'Hello, {names[i].title()}!')
