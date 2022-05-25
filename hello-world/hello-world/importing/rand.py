import random 
roll=0
count = 0
print("First person to roll a five wins!! ")

while roll !=5:
    name = input('enter a name, or \'q\' to quit: ')

    if name.strip() == '':
        continue

    if name.strip() == 'q':
        break
    
    count += 1
    roll = random.randint(1,10)
    print(f"{name} rolled {roll}")
else:
    print(f"{name} Wins!!!!")

print(f"You've rolled the dice {count} times")