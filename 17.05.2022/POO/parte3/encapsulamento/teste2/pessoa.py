class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome #Atributo público
        self.idade = idade #Atributo público
        self.__cpf = cpf #Atributo privado

    # Método público
    def correr(self):
        print('Estou correndo')

    # Método público
    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')

    # Método privado
    def __apresentar_documento(self):
        print(self.__cpf)


p1 = Pessoa('Mauro', 32, 123123123)

p1.beber('cerveja')
p1.beber('coca-cola')