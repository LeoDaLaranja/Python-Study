'''


class Pessoa:
    def __init__(self,nome,idade,comendo = False, falando = False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

        #é possivel criar variaveis dentro da classe, porém ela só é
        #valida dentro do método
        variavel = 'Valor'
        # print(variavel)

    def comer(self,alimento):
        
        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return

        print(f'{self.nome} está comendo {alimento} ')
        self.comendo = True


    def falar(self,assunto):
        if self.comendo:
            print(f'{self.nome} não pode falar enquanto está comendo! ')
            return
        if self.falando:
            print(f'{self.nome} já está falando ')
            return

        print(f'{self.nome} está falando sobre {assunto}...')
        self.falando = True
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando nada')
            return
        print(f'{self.nome} parou de falar, ainda bem!')
        self.falando = False

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo nada')
            return 
        print(f'{self.nome} parou de comer')
        self.comendo = False'''



class Pessoa:
    #isso é uma variavel de classe, todos os atributos podem ver ela
    ano = 2022
    def __init__(self,nome,idade):
        self.nome = nome
        self.idade = idade
    def get_idade(self):
        print(self.ano - self.idade)