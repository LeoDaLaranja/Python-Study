print("Simple Calulator ")

print("First Number: ")
first_number = input()

print("Operation: ")
operation = input()

print("Second Number: ")
second_number = input()

if first_number.isnumeric() == False and second_number.isnumeric() == False:
    print("Is not a number ")
elif operation.isalnum() == False:
    print("Operation not recognized") 
else:
     first_number = float(first_number)
     second_number = float(second_number)
     if operation == "+":
       sum = first_number + second_number
       print(f'The sum of {first_number} + {second_number} is equal to {sum}')   
       exit()
     elif operation == "-":
        sum = first_number - second_number 
        print(f'The subtract of {first_number} - {second_number} is equal to {sum}')
        exit()
     elif operation == "*":
         sum = first_number * second_number
         print("The multiplication of {first_number} * {second_number} is equal to {sum}")
         exit()
     elif operation == "/":
         sum = first_number / second_number
         print("The division of {first_number} / {second_number} is equal to {sum}")
         exit()
     elif operation == "%":
         sum = first_number % second_number
         print("The module of {first_number} % {second_number} is equal to {sum}")
         exit()
     elif operation == "**":
         sum = first_number ** second_number
         print("The Expoent of {first_number} % {second_number} is equal to {sum}")
         exit()
        
     

