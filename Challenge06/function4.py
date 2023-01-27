# in this function, the function is becomes in tuple
def list_names(*names): # In the official documentation it is found as args
    for name in names:
        print(name)

list_names('Bender', 'Leela', 'Fry')
list_names('Amy', 'Zoidberg', 'Professor Hubert')