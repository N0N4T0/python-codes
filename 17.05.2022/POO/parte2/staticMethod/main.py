# Método estático
# Não recebe nem a instância nem a classe

from random import randint


class Pessoa:
    anoAtual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
    
    # Método de instância precisa do parâmetro self
    def get_ano_nascimento(self):
        print(self.anoAtual - self.idade)

    # Método de classe precisa do parÂmetro cls
    @classmethod
    def por_ano_nascimento(cls, nome, anoNascimento):
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)

    # Método estático
    @staticmethod
    def gera_id():
        rand = randint(10000, 19999)
        return rand

p1 = Pessoa('Luiz', 23)
print("Id gerado de p1: {}".format(p1.gera_id()))
print(Pessoa.gera_id())
