def percentual(num, per):
    x = num + (num * (per/100))
    return x 

print(percentual(10,10))

def fizzbuzz(x):
    
    if x%3 == 0 and x%5 == 0:
        return f'FizzBuzz'
    elif x %3 == 0:
        return f'Fizz'
    elif x % 5 == 0:
        return f'Buzz'

print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(9))