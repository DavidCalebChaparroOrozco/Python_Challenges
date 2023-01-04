numA = int(input('Enter the number: '))
valueMin = 0
valueMax = 5

inRange = (numA >= valueMin) and (numA <= valueMax)
if inRange:
    print(f'The value {numA} is within range')
else:
    print(f'The value {numA} not in range')