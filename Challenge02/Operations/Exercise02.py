# We are asked to calculate the area and perimeter of a rectangle. 
# we must create the following variables 
# height(int) 
# width(int) 

# The user must provide the values of length and width, and then the result must be 
# printed in the following format 
# should print the result in the following format 
# Provide the height: 
# Provides the width: 
# Area: <area> 
# Perimeter: <perimeter>.

# The formulas for calculating the area and perimeter of a rectangle are:
# Area : height * width 
# Perimeter: (height + width) * 2

height = int(input("Provide the height: "))
width = int(input("Provide the width: "))
area = height * width
Perimeter = (height + width) * 2

print(f'The area of rectangle is: {area}')
print(f'The perimeter of rectangle is: {Perimeter}')

