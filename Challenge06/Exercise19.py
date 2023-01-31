# Create a function to sum the received values of numeric type,
# using variable arguments *args as the function parameter
# and return as result the sum of all values passed as arguments.

def sum_values(*args) -> int:
    result = 0
    for value in args:
        # result = result + value
        result += value
    return result


print(sum_values(3, 6, 9, 2, 3, 1, 10))
