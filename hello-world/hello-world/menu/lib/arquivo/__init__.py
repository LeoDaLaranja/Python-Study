from lib.interface import *
def arquivoExiste(x):
    try:
        r = open(x,'rt')
        r.close()
    except FileNotFoundError: 
        return False
    else:
        return True
def criarArquivo(x):
    try: 
        r = open(x,'wt+')
        r.close()
    except:
        print('\033[0;31mHouve um erro na criação do arquivo! \033[m')
    else:
        print(f'Arquivo criado com sucesso! ')

def lerArquivo(x):
    try:
        r = open(x,'rt')
    except: 
        print('\033[0;31mErro ao ler o arquivo\033[m')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for linha in r:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n','')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        r.close()
    
def cadastrar(nome,pessoa = 'desconhecido',idade = 0):
    try:
        r = open(nome,'at')
    except:
        print('\033[0;31mErro na abertura do arquivo\033[m')
    else:
        try:
            r.write(f'{pessoa};{idade}\n')
        except:
            print('\033[0;31mErro ao inserir os dados\033[m')
        else:
            print(f'Novo registro de {pessoa} adicionado')
            r.close()