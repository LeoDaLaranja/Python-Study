# Mutável : Dicionários, listas
# Imutável : Tuplas, stings, números, True, False, None

# na linha abaixo temos um problema que retorna a lista com novos nomes toda vez que a função é chamada
#def lista_de_clientes(clientes_iteraveis, lista_clientes  = []):

# Para resolver isso, precisamos passar como parâmetro None o segundo argumento ou qualquer um que possa vir a ser mutável
def lista_de_clientes(clientes_iteraveis, lista_clientes  = None):
    #dentro da função é jogada uma condição, caso verdadeira ela cria uma nova lista 
    if lista_clientes is None:
        lista_clientes = []
    lista_clientes.extend(clientes_iteraveis)
    return lista_clientes

clientes1 = lista_de_clientes(['Leo','Maria','Eduardo'])
clientes2 = lista_de_clientes(['Marcos','Jonas','Zico'])

print(clientes1)
print()
print(clientes2)