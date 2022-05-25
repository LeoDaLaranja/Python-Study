frase = 'o rato roeu a roupa do rei de roma'
tamanho_frase = len(frase)
c = 0 
nova_string = ''

while c < tamanho_frase:
    letra = frase[c]
    print(letra)
    if letra == 'r':
        nova_string += 'R'
    elif letra == 'a':
        nova_string += '4'
    else:
        nova_string += letra

    c += 1 
print(nova_string)
