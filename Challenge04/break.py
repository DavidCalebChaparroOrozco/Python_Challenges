# Finding the first 5 multiples of a given number using a for loop
number = int(input('Enter a number: '))

counter = 0
for i in range(1, 100):
    if number * i > 100:
        break
    if counter < 5:
        print(number * i)
        counter += 1
