# #funcao decoradora
# def master(funcao):
#     def slave(*args,**kwargs):
#         print('Agora estou decorada')
#         funcao(*args,**kwargs)
#     return slave

# #essa é a ideal -> vira um decorador
# @master
# def fala_oi():
#     print('oi')

# @master
# def outra_funcao(msg):
#     print(msg)

# outra_funcao('Eu sou o Leo')

    
# #isso decora de uma maneira normal, porém não é a ideal
# #fala_oi = master(fala_oi)

# fala_oi()


from time import sleep,time


def velocidade(funcao):
    def interna(*args,**kwargs):
        start_time = time()
        resultado = funcao(*args,**kwargs)
        end_time = time()
        tempo = round((end_time-start_time) * 1000,2)
        print(f'a funcao {funcao.__name__}levou {tempo}ms para executar')
        return resultado
    return interna



@velocidade
def demora():
    for i in range(10):
        print(i)


demora()