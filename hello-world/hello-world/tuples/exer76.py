produto = ('Laranja',70,'Banana',39.8)

for c in range(len(produto)):
   
    if c%2==0:
        print(f'{produto[c]:<20}',end='')
    else:
        print(f'R${produto[c]:>3}')