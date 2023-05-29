class Pessoa:
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} Não pode falar comendo')
            return

        if self.falando:
            print(f'{self.nome} ja está falando')
            return

        print(f'{self.nome} está Falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} Não está falando.')
            return

        print(f'{self.nome} parou de falar. ')
        self.falando = False

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} {self.idade} anos, ja está comendo {alimento}.')
            return

        if self.falando:
            print(f'{self.nome} Não pode comer falando')
            return

        print(f'{self.nome} {self.idade} anos, está comendo {alimento}')
        self.comendo = True

    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} Não está comendo')
            return

        print(f'{self.nome} parou de comer. ')
        self.comendo = False
