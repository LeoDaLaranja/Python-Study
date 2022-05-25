import random
n = 0 
counter = 0
rand_number = random.randint(1,5)

while n!=rand_number:
    counter += 1
    n = input("Guess a number between 1 and 5: ")
    if n.isnumeric() == False:
        print("Numbers only, please!")
        continue
    else: 
        n = int(n)
        if n < rand_number:
            print("Your guess is too low, please try again ")
        else:
            print("Your guess is too high, please try again ")
else:
    print(f'You guessed it in {counter} times!! ')