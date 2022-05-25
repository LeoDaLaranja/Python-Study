'''
def 02
'''

'''
def funcao(var):
    #o comando print como forma de retorno não é viavel e não é convencional em um programa em python
    #print(var)
    return var

variavel = funcao('Valor que eu quero')
#retorna o valor da variavel, como na função não existe um tipo de retorno o retorno será None
#print(variavel)

#Aqui é possivel verificar se a variavel possui algum valor ou não

if variavel:
    print(variavel)
else:
    print("Nenhum valor na variavel")

def divisao(num, den):
    if den ==0:
        return f'This function will tend to infinity'
    else:
        valor = num/den
        return f'the resutl of the division is {valor:.2f}'

num = float(input('Insert the numerator of the division '))
den = float(input('Insert the denominator of the division '))

divi = divisao(num,den)
print(divi)'''


def dumb():
    return [1,2,3,4,5,6]
var = dumb()
print(var,type(var), id(var))