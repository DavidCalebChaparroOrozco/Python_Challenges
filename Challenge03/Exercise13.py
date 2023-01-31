# Provide a numeric value to provide your age. Depending on the value provided, we will perform the following checks:
# If you have provided a value between 0 and 10, then we send the message:
# 'Childhood is amazing.'
# If you provided an age value between 10 and 20, then we send the message:
# 'Many changes and a lot of study.'
# And if it provides a value between 20 and 30, we send the message:
# 'Love and work begins.'
# Any other value we send the message: 'Life stage NOT recognized.'
age = int(input('Enter the age: '))
message = None

if 0 <= age < 10:
    message = 'Childhood is amazing.'
elif 10 <= age < 20:
    message = 'Many changes and a lot of study.'
elif 20 <= age < 30:
    message = 'Love and work begins.'
else:
    message = 'Life stage NOT recognized.'
print(f'For the age {age}, {message}')
