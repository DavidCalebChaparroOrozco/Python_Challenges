# Perform two functions to convert from degrees Celsius to fahrenheit and vice versa.

def celsius_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

celsius = float(input('Enter value in Celsius: '))
result = celsius_fahrenheit(celsius)
print(f'{celsius} C to F: {result:.2f}')

fahrenheit = float(input('Enter value in Fahrenheit: '))
result = fahrenheit_celsius(fahrenheit)
print(f'{celsius} F to C: {result:.2f}')