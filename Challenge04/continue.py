# Print even numbers given a range entered by the user.

# for i in range(6):
#     if i % 2==0:
#         print(f'Enter value: {i}')

max = int(input('Enter the max value: '))
for i in range(max):
    if i % 2 !=0:
        continue
    print(f'Value: {i}')