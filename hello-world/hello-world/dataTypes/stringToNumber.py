first_value = int(input('First Number: '))
second_value = int(input('Second number: '))
sum = first_value + second_value
print("Sum: " + str(sum))

print("\n----------//---------------//---------")
print("This function isnumeric() returns a boolean value its the codition is correct ")
numeric_value = '7'
print(numeric_value.isnumeric())

string_value = 'Bob'
print(string_value.isnumeric())

print("\n---------//--------------//----------")
first_value = input("First Number: ")
second_value = input("Second number: ")

if first_value.isnumeric() == False or second_value.isnumeric() == False:
    print("Value is not a number ")
    exit()

first_value = int(first_value)
second_value = int(second_value)
sum = first_value+second_value
print('Sum: '+ str(sum))


print("\n---------//--------------//----------")