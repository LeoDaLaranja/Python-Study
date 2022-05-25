lista = []
c = 's'
while c != 'n':
   n = int(input("Informe um número "))
   c = input('Deseja continuar? ')
   
   
   if n in(lista):
      c = input('Número já adicionado na lista, deseja tentar outro?')
      
   else:
      lista.append(n)
      
print(lista.sort())