#aliens_0 = {'color' : 'green', 'points' : 5}

# // PRINT VALUES IN DICTIONARY //
#print(aliens_0['color'])
#print(aliens_0['points'])

# // PRINT POINT VALUE W/ TEXT //
#new_points = aliens_0['points']
#print(f'You just earned {new_points} points!')

# // ADD NEW KEY-VALUE PAIR TO DICTIONARY //
#print(aliens_0)
#aliens_0['x_poisition'] = 0
#aliens_0['y_position'] = 25
#print(aliens_0)

# // STARTING W/ EMPTY DICTIONARY AND ADDING KEY-VALUE PAIRS //
#alien_0 = {}

#alien_0['color'] ='green'
#alien_0['points'] = 5

#print(alien_0)

#print(f'The alien is {alien_0['color'].title()}.')

# // CHANGE ALIEN COLOR //
#alien_0['color'] = 'yellow'
#print(f'The alien is now {alien_0['color'].title()}.')

# // TRACKING MOVEMENT //
alien_0 = {}
alien_0['x_position'] = 0
alien_0['y_posotion'] = 25
alien_0['speed'] = 'medium'
print(alien_0)

print(f'Original position is {alien_0['x_position'], alien_0["y_posotion"]}')

# MOVE THE ALIEN TO THE RIGHT
# DETERMINE HOW FAR TO MOVE THE ALIEN BASED ON ITS CURRENT SPEED
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    #THIS MUST BE A FAST ALIEN
    x_increment = 3

# THE NEW POSITION OS THE OLD POSITION PLUS THE INCREMENT.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f'The new position is {alien_0['x_position'], alien_0["y_posotion"]}')