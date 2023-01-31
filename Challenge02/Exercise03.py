# When a number is entered by the user, it must state whether the number is Odd or Even.
numA = int(input("Enter a number: "))
if numA % 2 == 0:
    print(f"The number {numA} Odd")
else:
    print(f"The number {numA} Even")
