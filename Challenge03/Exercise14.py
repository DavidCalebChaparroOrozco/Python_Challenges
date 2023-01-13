# Create a rating system.
# The user will provide a value between 0 and 10.
# If the value is between 9 and 10: Print an A.
# If the value is between 8 and 9: Print a B
# If the value is between 7 and 8: Print a C
# If the value is between 6 and 7: Print a D
# If the value is between 0 and 6: Print an F
# Any other value should print: Incorrect value.
note = float(input('Enter the note between 0 and 10: '))

if 9 <= note <= 10:
    print('A')
elif 8 <= note < 9:
    print('B')
elif 7 <= note < 8:
    print('C')
elif 6 <= note < 7:
    print('D')
elif 0 <= note < 6:
    print('F')
else:
    print('Incorrect value...')