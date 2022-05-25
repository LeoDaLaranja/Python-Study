def funcao():
    global n1
    n1 =4 
    '''
    Ao passar n1 como paremtro e alterando o valor dela aqui dentro eu passo 
    a ter uma variavel n1 local com o valor de 4, porém é possível usar uma função 
    e usar o valor local da váriavel 
    então n1 deixa de usar o valor 2 e passa a ter o valor 4
    '''
    #Aqui temos as varaveis locais e fora da função o seu valor global
    print(f'N1 dentro vale {n1}')

n1 = 2 
funcao()
#valor global de todas as variaveis são definidos aqui
print(f'N1 fora vale {n1}')