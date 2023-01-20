# Syntax of range(start<optional>, end<required, increment<optional>)
# Exercise17.1: Iterate a range from 0 to 10 and print numbers divisible by 3
print('Range 0 to 10 with numbers divisible by 3')
for i in range(11):
    if i % 3 ==0:
        print(i)

# Exercise17.2: Create a range of numbers from 2 to 20, and print them.
print('Range with start = 2 and end = 20')
rang = range(2,21)
for i in rang:
    print(i)

# Exercise17.3: Create a range from 3 to 15, but with an increment of 2 by 2.
print('Range with start = 3, end = 15, increment = 2')
rang = range(3,16,2)
for i in rang:
    print(i)