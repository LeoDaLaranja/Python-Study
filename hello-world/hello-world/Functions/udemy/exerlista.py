'''
Faça uma lista de tarefas com as seguintes opções 
    adicionar uma tarefa 
    remover uma tarefa 
    opção de desfazer(a cada vez que chamamos, desfaz a ultima ação feita)
    opção de refazer(a cada vez que chamamos, refaz a ultima opção)


'''

def insere_lista(item,lista_afazeres = None):
    #
    lista_afazeres.append(item)
    return print(f'Item {item} adicionado com sucesso!'),lista_afazeres

def remove_lista(item,lista_afazeres = None):
    temp_item = item
    desfaz_lista(lista_afazeres)
    if lista_afazeres is None:
        return f'Não é possivel remover itens de uma lista vazia'
    for i in lista_afazeres:
        print(i)
        if item == i:
            lista_afazeres.remove(item)
        return print(f'Item: {item} removido com sucesso '),lista_afazeres

def desfaz_lista(lista_afazeres):
    backup_lista = lista_afazeres.copy()
    lista_afazeres.pop()
    return print(f'A lista antiga é {backup_lista}, a nova lista é {lista_afazeres}'), lista_afazeres
def refaz_lista():
    pass
lista_afazeres = ['Tomar banho']
lista_acao = []
last = 0
while True:
    print('=' * 20)
    print('Lista de afazeres')
    for c in range(len(lista_afazeres)):
        print('Você precisa fazer as seguintes coisas')
        print('[]',c,lista_afazeres[c])
        continue
    print('=' *20)
    op = input('Deseja fazer alguma coisa?: ')
    if op.upper() in 'SSIM':
        print('')
        print('Informe o que precisa ser feito: ')
        print('OP 1 - Inserir item na lista ')
        print('OP 2 - Remover item da lista')
        print('OP 3 - Desfazer a ação anterior')
        print('OP 4 - Refazer a ação anterior')
        op = input('Informe a opção desejada: ')
        if op =='1' or last == 1:
            item = input('Ação a ser inserida: ')
            insere_lista(item,lista_afazeres)
            lista_acao.append(op)
        elif op == '2' or last == 2:
            item = input('Item a ser removido: ')
            remove_lista(item,lista_afazeres)
            lista_acao.append(op)
        elif op == '3' or last ==3:
            print(desfaz_lista(lista_afazeres))
            lista_acao.append(op)

        elif op == '4' or last == 4:
            last = lista_acao.pop()
            continue

    else:
        break
