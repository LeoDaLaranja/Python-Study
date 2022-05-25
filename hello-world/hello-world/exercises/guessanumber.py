import random
n = 0
roll = 0
count = 0

rand_number = random.randint(1,3)
while n!=rand_number:
    
    print(rand_number)
    count += 1
    n = input("Guess a number between 1 and 5: ")
    if n.isnumeric() == False:
        n = input("Guess a number between 1 and 5: ")
    else:
        n = int(n)
   
        
    
else: 
    print(f"You guessed it in {count} times!")