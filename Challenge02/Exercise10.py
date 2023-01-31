# For this exercise let's test what we have learned so far, we will create a book store, 
# if you want to add more data you can add them.
print(" Enter to the following book data ".center(50,"-"))
name = input("Enter the name of the book: ")
id = int(input("Enter the ID of the book: "))
price = float(input("Enter the price of the book: "))
free_delivery = input("Enter if the send is free (True/False): ")

if free_delivery == 'True':
    free_delivery = True
elif free_delivery == 'False':
    free_delivery = False
else:
    free_delivery = "Wrong value, enter True or False"

print(f'''
    Name: {name},
    Id: {id},
    Price: {price},
    Free delivery?: {free_delivery}
''')
