# Create a function to multiply received values of numeric type,
# using variable arguments *args as the function parameter
# and return as result the multiplication of all values passed as arguments.

def multiply_values(*numbers) ->int:
    result = 1
    for number in numbers:
        # result = result * value
        result *= number
    return result

print(multiply_values(3,6,9,2,3,1,10))