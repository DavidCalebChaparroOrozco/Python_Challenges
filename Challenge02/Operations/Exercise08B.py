age = int(input('Enter your age: '))

#twenties = (age >= 20 and age < 30)
#print(twenties)
#
#thirties = (age >= 30 and age < 40)
#print(thirties)

if (age >= 20 and age < 30) or (age >= 30 and age < 40):
    print('Inside the range (20\'s) or (30\'s)')
    #if twenties:
    #    print('within Twenty')
    #elif thirties:
    #    print('within Thirty')
    #else:
    #    print('Out of range')
else:
    print("Is not among 20's or 30's")