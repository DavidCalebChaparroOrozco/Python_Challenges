# When a number is entered by the user, it must state whether the number is Odd or Even.
ageAdult = 18
numA = int(input("Enter a number: "))
if numA >= ageAdult:
    print(f"The person with age {numA} is an Adult")
else:
    print(f"The person with age {numA} is under age")
