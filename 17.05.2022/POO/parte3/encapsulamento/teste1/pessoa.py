class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome #Atributo público
        self.idade = idade #Atributo público
        self.__cpf = cpf #Atributo privado

    # Método público
    def print_cpf(self):
        print(self.__cpf)

   
p1 = Pessoa('Mauro', 32, 123123123)

# Teste de erro
# print(p1.__cpf)

p1.print_cpf()
# perceba que eu não consigo acessar mais o atributo,
# só consigo fazer isso com o método, 
# então eu estou protegendo o meu contéudo