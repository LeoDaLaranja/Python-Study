print("What is the temperature in fahrenheit? ")
fahrenheit = input()
if fahrenheit.isnumeric():
    fahrenheit = float(fahrenheit)
    celsius = round((fahrenheit - 32) * 5/9)
    print("Temperature in celsius is "+str(celsius))
else:
    print("Input is not a number ")