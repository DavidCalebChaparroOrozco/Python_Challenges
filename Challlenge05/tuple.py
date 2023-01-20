# Define a tuple
fruits = ('Orange', 'Banana', 'Apple')

# know the length
print(len(fruits))

# access an item
print(fruits[0])

# reverse navigation
print(fruits[-1])

# access to a range
print(fruits[0:1]) # Excluding last index

# loop elements
for fruit in fruits:
    print(fruit, end=' ')

# change value tuple
# fruits[0] = 'Pear'

fruitsList = list(fruits)
fruitsList[0] = 'Pear'
fruits = tuple(fruitsList)
print('\n',fruits)

# delete the tuple
del fruits