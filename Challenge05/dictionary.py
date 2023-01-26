# dict (key, value)
dict = {
    'IDE': 'Integrated Development Enviroment',
    'OPP': 'Object Orient Programming',
    'DMBS': 'Database Management System'
}
print(dict)

# len
print(len(dict))

# access an element (key)
print(dict['IDE'])

# another way to recover an element
print(dict.get('OOP'))

# Modifying item
dict['IDE'] = 'integrated development enviroment'
print(dict)

# Go through all the elements
for i, value in dict.items():
    print(i,value)

for i in dict.keys():
    print(i)

for i in dict.values():
    print(i)

# Check if an item is present
print('IDE' in dict)

# Add to item
dict['PK'] = 'Primary Key'
print(dict)

# delete item
dict.pop('DMBS')
print(dict)

# clear dict
dict.clear()
print(dict)

# delete dict
del dict