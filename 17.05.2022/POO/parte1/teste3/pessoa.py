class Pessoa:
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade= idade
        self.comendo = comendo
        self.falando = falando

    def falar(self, assunto):
        # não falar comendo
        if self.comendo:
            print(f'{self.nome} não pode falar comendo')
            return

        # Já está falando
        if self.falando:
            print(f'{self.nome} já está falando')
            return
        
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True

    def parar_falar(self):
        # se não estiver falando não tem como para de falar
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        
        print(f'{self.nome} parou de falar')
        self.falando = False

    def comer(self, alimento):
        # Permitir que a pesso coma uma vez somente
        if self.comendo:
            print(f'{self.nome} já está comendo')
            return

        # Não pode comer falando
        if self.falando:
            print(f'{self.nome} não pode comer falando')
            return

        print('{} está comendo {}'.format(self.nome, alimento))
        self.comendo = True

    def para_comer(self):
        # se não estiver comendo não tem como para de comer
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        
        print(f'{self.nome} parou de comer')
        self.comendo = False