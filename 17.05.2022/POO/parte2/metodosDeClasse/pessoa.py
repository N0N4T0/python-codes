class Pessoa:
    # atributo disponível na classe, todo objeto ja vai ter ess attributo
    # atributo de classe ou variáveis de classe
    anoAtual = 2019

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade 
    
    # Método de instância precisa do parâmetro self
    def get_ano_nascimento(self):
        print(self.anoAtual - self.idade)

    # Método de classe precisa do parÂmetro cls
    # quando é um método da classe precisamos passar um decorador
    @classmethod
    def por_ano_nascimento(cls, nome, anoNascimento):
        # pode ser cls ou qualquer outro nome
        # o primeiro argumento é a classe, e não a instância
        idade = cls.anoAtual - anoNascimento
        return cls(nome, idade)
        # retorna a própria classe com nome e idade
        # baseado nos parâmetros do por_ano_nascimento


p1 = Pessoa.por_ano_nascimento('Luiz', 23)

print(p1.anoAtual)

# Método de classe x método de instância
# É relacionada a classe em geral ou a instância (específico de cada objeto)?
# Método de classe = disponível para todos os objetos 
# Método de instância = disponível para o objeto que instanciar o método