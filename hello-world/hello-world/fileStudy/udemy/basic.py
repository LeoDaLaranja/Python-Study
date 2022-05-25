#abrir um arquivo

file = open('filestudy/udemy/abc.txt','w+') #isso permite criar/escrever nesse arquivo

file.write('Linha 1\n')
file.write('Linha 2\n')
file.write('Linha 3\n')


file.seek(0,0)#para procurar, geralmente usamos 0 em ambos para ir ao inicio

print('Lendo linhas: ')
print(file.read())
print('===========')

file.seek(0,0) # sempre bom voltar o cursor ao começo do arquivo


print(file.readline())#lendo linha por linha
print('=========')
file.seek(0,0)

print(file.readlines())#retorna uma lista com todas as linhas, inclusive com as quebras de linhas impostas no código
print('===========')
print('Linha com o for')
file.seek(0,0)
for linha in file.readlines():
    print(linha)


file.close()