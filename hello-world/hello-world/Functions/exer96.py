
def area(a,b):
    print(f'A área do terreno será calculada com os seguintes parâmetros {a}m, {b}m')
    area = a*b
    print(f'A área calculada é de {area} m2')

a = float(input('Comprimento do terreno: '))
b = float(input('Largura do terreno: '))
area(a,b)