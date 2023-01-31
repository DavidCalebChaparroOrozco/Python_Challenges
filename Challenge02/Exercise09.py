"""
Task instructions:
Prompt the user for two values, and determine which number is greater.
numA (int)
numB (int)
The larger of the two numbers must be printed (the output must be identical to the one below):
Enter numA:
Enter numB:
The greater number is: <greaterNumber>.
"""
numA = int(input("Enter numA: "))
numB = int(input("Enter numB: "))

if numA > numB:
    print(f"The number {numA} is greater than the number {numB}")
else:
    print(f"The number {numB} is greater than the number {numA}")