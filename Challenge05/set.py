# set
planets = {'Mars', 'Jupiter', 'Venus', 'Earth'}
print(planets) # The sets do not keep an order

# Len
print(len(planets))

# Check if an item is present
print('Mars' in planets)

# Add to item
planets.add('Saturn')
print(planets)

# Sets do not accept duplicated data
planets.add('Earth')
print(planets)

# delete item / It may throw an error
planets.remove('Earth')
print(planets)

# delete item without error
planets.discard('Jupiter')
print(planets)

# clear set
planets.clear()
print(planets)

# delete set
del planets