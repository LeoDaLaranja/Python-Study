lista = []
i=0
x = 0
y=0
while c != 'n':
   n = int(input("Informe um número "))
   c = input('Deseja continuar? ')
   
   lista.append(n)
   x+=1
   if 5 in(lista):
      print('Sim o valor foi digitado e ocupa a posição{pos.lista}')
      
print(f'Num total de itens na lista{x}')
print(lista.sort(reverse=True))