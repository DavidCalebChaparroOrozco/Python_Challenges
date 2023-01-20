# Given a tuple, create a list that only includes numbers less than 5
tupleA = (13, 1, 8, 3, 2, 5, 8)

# define a list
listA = []
# Filter out elements less than 5 from the tuple
for element in tupleA:
    if element < 5:
        listA.append(element)
print(listA)