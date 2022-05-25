print('Jogo da forca! ')

palavra = 'perfume'
lista_letra = []
palavra_secreta = ''
chances = 3
while True:
    letra = input('Informe uma letra ')

    if len(letra)>1:
        print('Só é permitido uma letra por vez! ')
        continue
    lista_letra.append(letra)

    if letra in palavra:
        print('Voce acertou uma letra!')

    else:
        chances -=1
        print('Errou feio,errou rude!')
        if chances == 0:
            print('Suas chances chegaram ao fim!')
            print(f'A palavra secreta era {palavra}')
            break
        
        print(f'você tem {chances} chances')
        lista_letra.pop()
    secreto_temporario = ''

    for letra_secreta in palavra:
        if letra_secreta in lista_letra:
            secreto_temporario  += letra_secreta
        else: 
            secreto_temporario += '*'
    print(secreto_temporario)
    if secreto_temporario == palavra:
        print('Você ganhou!')
        break


    