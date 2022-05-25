cpf = '479.519.678-82'
lista_num = []
for c in range(len(cpf)):
    numero  = cpf[c]
    lista_num.append(numero)
    if numero == '.' or numero == '-':
        lista_num.pop()
val_veri = []
final_cpf = lista_num[-2:]
#print(final_cpf)
novo_cpf = lista_num[:-2]
#print(novo_cpf)

reverso = 10 
total = 0 

for index in range(19):
    if index > 8:
        index -=9

    
    total += int(novo_cpf[index]) * reverso
   
    
    reverso -= 1
    if reverso <2:
        reverso = 11
        d = 11 - (total % 11)
        if d > 9:
            d = 0 
        
        total = 0 
        novo_cpf += str(d)

print(novo_cpf)

if novo_cpf == cpf:
    print('Válido')
else:
    print('Inválido')



