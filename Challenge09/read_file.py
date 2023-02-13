file = open('test.txt', 'r', encoding='utf8') # To view the other file managements check out file_management.md
# print(file.read())

# # read a few characters
# print(file.read(3))
# print(file.read(13))

# # Read full lines
# print(file.readline())
# print(file.readline())

# # Iterate file
# for line in file:
#     print(line) # To check it, add a message to test.txt

# # Read lines
# print(file.readline())

# # Access a line of a list
# print(file.readline()[0])

# Open a new file
file2 = open('copy.txt','a',encoding='utf8')
file2.write(file.read())

file.close()
file2.close()
print('A copy file named copy.txt has been created.')