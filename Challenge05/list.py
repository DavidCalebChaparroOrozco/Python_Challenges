# define a list of type str
name_simpson = ['Homer', 'Marge', 'Bart', 'Lisa', 'Maggie']

# print the list
print(name_simpson)

# access the items in the list
print(name_simpson[0])
print(name_simpson[1])

# access the list items in reverse order
print(name_simpson[-1])
print(name_simpson[-2])

# print a range
print(name_simpson[0:2]) # excluding index 2

# go from the top of the list to the index (not included)
print(name_simpson[:3])

# from the indicated index to the end
print(name_simpson[1:])

# change a value
name_simpson[2] = 'Hugo'
print(name_simpson)

# loop the list
for name in name_simpson:
    print(name)
else:
    print('There are no more Simpson family members')

# ask for list length
print(len(name_simpson))

# append item in the list
name_simpson.append('Bart')
print(name_simpson)

# insert an item into a specific index
name_simpson.insert(0,'Abraham')
print(name_simpson)

# remove an item
name_simpson.remove('Hugo')
print(name_simpson)

# remove the last item added
name_simpson.pop()
print(name_simpson)

# remove a specified index
del name_simpson[0]
print(name_simpson)

# clear the list
name_simpson.clear()
print(name_simpson)

# delete list completely
del name_simpson