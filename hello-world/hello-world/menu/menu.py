from lib.interface import *
from lib.arquivo import *
from time import sleep





arq = 'menu\pessoas.txt'
# verificação e criação de um arquivo 
if not arquivoExiste(arq):
    criarArquivo(arq)
    


while True:

    resposta = menu(['Ver pessoas cadastradas ', 'Cadastra Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        #Opção para listar um novo conteúdo de um arquivo 
        lerArquivo(arq)
    elif resposta == 2:
        #Opção para cadastro de uma nova pessoa
        cabecalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)

    elif resposta == 3:
        print('Saindo do sistema...')
        sleep(2)
        cabecalho('Sistema finalizado com sucesso!')
        break
    else:
        print('\033[0;31mERRO! Informe uma opção válida \033[m')
    sleep(2)