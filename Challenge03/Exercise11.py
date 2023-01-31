# Number to text conversion
numA = int(input('Enter a value between 1 and 3: '))
numText = ''

if numA == 1:
    numText= 'Number One'
elif numA == 2:
    numText = 'Number Two'
elif numA == 3:
    numText = 'Num Three'
else:
    numText = 'Out of range value'

print(f'Number provided: {numA}: {numText}')