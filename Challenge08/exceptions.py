# # ZeroDivisionError
# result = None
# numA = 10
# numB = 0
# try:
#     result = numA/numB
# except ZeroDivisionError as zde:
#     print(f'An error occurred {zde}')
#
# print(f'Result: {result}')
# print('Continue to...')

# # Exception: In order of hierarchy, it can serve these types of errors
# result = None
# numA = '10'
# numB = 0
# try:
#     result = numA/numB
# except Exception as e:
#     print(f'An error occurred {e}')
#
# print(f'Result: {result}')
# print('Continue to...')

# # TypeError
# result = None
# numA = '10'
# numB = 0
# try:
#     result = numA/numB
# except ZeroDivisionError as zde:
#     print(f'An error occurred {zde}')
# except TypeError as te:
#     print(f'An error occurred {te}')
#
# print(f'Result: {result}')
# print('Continue to...')

# # Exception
# result = None
# try:
#     numA = int(input('Enter the first number: '))
#     numB = int(input('Enter the second number: '))
#     result = numA/numB
# except ZeroDivisionError as zde:
#     print(f'ZeroDivisionError - An error occurred: {zde}, {type(zde)}')
# except TypeError as te:
#     print(f'TypeError - An error occurred: {te}, {type(te)}')
# except Exception as e:
#     print(f'Exception - An error occurred: {e}, {type(e)}')
# # Remember to use the child classes first and then the more generic ones.
# else: # This is optional
#     print('There are no exceptions')
# finally:
#     print('Execution of finally block')
# print(f'Result: {result}')
# print('Continue to...')

# # Custom exceptions:
from IdenticalNumbersException import *

result = None
try:
    numA = int(input('Enter the first number: '))
    numB = int(input('Enter the second number: '))
    if numA == numB:
        raise IdenticalNumbersException('identical numbers') # raise: Used for any kind of exception
    result = numA/numB
except ZeroDivisionError as zde:
    print(f'ZeroDivisionError - An error occurred: {zde}, {type(zde)}')
except TypeError as te:
    print(f'TypeError - An error occurred: {te}, {type(te)}')
except Exception as e:
    print(f'Exception - An error occurred: {e}, {type(e)}')
else:
    print('There are no exceptions')
finally:
    print('Execution of finally block')
print(f'Result: {result}')
print('Continue to...')