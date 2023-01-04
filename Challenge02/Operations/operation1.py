# Assign values to a variable
myVar = 10
print(f"Variable initial value: {myVar}")

# Form 1
myVar = myVar + 1
print(f"First form for by + : {myVar}")

# Form 2
myVar += 1
print(f"Second form for by += : {myVar}")

# or maybe with subtraction for example:
myVar = myVar - 1
print(f"First form for by - : {myVar}")

myVar -= 1
print(f"Second form for by -= : {myVar}")

# They can also be used for multiplication
myVar *= 3
print(f"Form for *= : {myVar}")

# Division
myVar /= 2
print(f"Form for /= : {myVar}")

# Exponentiation
print("Here I overwrote the variable to give clarity with the operation")
myVar = 12
print(f" The new value is: {myVar} ".center(50,"-")) 
myVar **=2
print(f"Form to **= : {myVar}")

# Integer Division
myVar //= 12
print(f"Form to //= : {myVar}")
